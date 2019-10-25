import os
import shutil
from plistlib import dump as plDump
from ufoProcessor import DesignSpaceProcessor
from fontParts.fontshell import RFont
from fontTools.designspaceLib import DesignSpaceDocument
from defcon import Font

# Family specific data

weightMap = {
             "Black": 900,
             "UltraBold": 850,
             "ExtraBold": 800,
             "Bold": 700,
             "SemiBold": 600,
             "Medium": 500,
             "Regular": 400,
             "Light": 300,
            }


# Helper functions
def getFiles(path, extension):
    """
    Walks down all directories starting at *path* looking for files
    ending with *extension*. Knows that UFOs are directories and stops
    the walk for any found UFO.
    """
    if not extension.startswith('.'):
        extension = '.' + extension
    if extension == '.ufo':
        return [dir for (dir, dirs, files) in os.walk(path)
                if dir[-len(extension):] == extension]
    else:
        return [os.sep.join((dir, file)) for (dir, dirs, files)
                in os.walk(path) for file in files if
                file[-len(extension):] == extension]


def printProgressBar(iteration, total, prefix='', suffix='',
                     decimals=1, length=100, fill='█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)

    Nabbed, of course, from Stack Overflow
    (https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console)
    """
    percent = ("{0:."+str(decimals)+"f}").format(100*(iteration/float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end='\r')
    # Print New Line on Complete
    if iteration == total:
        print()


def buildStatic(designspacePath, outputPath):
    """
    Reads designspace file, generates instance UFOs,
    builds mastering files for the Adobe FDK, then
    builds files.

    *designspacePath* is the path to the designspace file.
    *outputPath* is the path for file builds.

    """
    pass


def buildFontMenuDB(designspace, root):
    """
    Pulls the postscript, and the mapping names from the designspace.
    Transforms the family name from "Recursive" to either "Recursive Sans"
    or "Recursive Mono" for the static fonts.
    """

    out = ""

    for i in designspace.instances:
        fn = i.familyName + " " + i.styleName.split()[0]
        sn = " ".join(i.styleName.split()[1:])
        out += f"[{i.postScriptFontName}]\n"
        out += f"    f={fn}\n"
        out += f"    s={sn}\n"
        out += f"    l={i.styleMapFamilyName}\n"
        out += f"    m=1,{i.styleMapFamilyName} {i.styleMapStyleName}\n\n"

    path = os.path.join(root, "FontMenuNameDB")
    with open(path, "w") as f:
        f.write(out)


def buildGlyphOrderAndAlias(designspace):
    pass


def buildFontInfo(font):
    pass


def buildFeatures(font):
    pass


def fillInPanoseValues(font):
    """
    Fills in the Panose values for a font based on the style name.
    Uses the  panoseWeightMap to set weight values, the presense of
    'Mono' to set if it's monospaced, and the presense of 'Italic' to
    set if it's oblique. 'Casual' and 'Linear' trigger settings for
    the style.
    """

    panoseWeightMap = {
                       "Black": 11,
                       "UltraBold": 10,
                       "ExtraBold": 9,
                       "Bold": 8,
                       "SemiBold": 7,
                       "Medium": 6,
                       "Regular": 5,
                       "Light": 4,
                      }

    names = font.info.styleName.split()

    if names[0] == "Mono":
        prop = 9
    else:
        prop = 4

    if names[3]:
        form = 11
    else:
        form = 4

    wght = panoseWeightMap[names[2]]

    if names[1] == "Casual":
        font.info.openTypeOS2Panose = [2, 15, wght, prop, 5, 5, 2, form, 3, 4]
    else:
        font.info.openTypeOS2Panose = [2, 11, wght, prop, 4, 2, 2, form, 2, 4]


def fixStandardStems(font):
    from collections import OrderedDict
    hStems = font.info.postscriptStemSnapH
    newHStems = list(OrderedDict.fromkeys(hStems))
    font.info.postscriptStemSnapH = newHStems
    vStems = font.info.postscriptStemSnapV
    if font.info.styleName.split()[3]:
        font.info.postscriptStemSnapV = vStems[2]
    else:
        newVStems = list(OrderedDict.fromkeys(vStems))
        font.info.postscriptStemSnapV = newVStems


def buildInstances(designspacePath, root):
    doc = DesignSpaceProcessor()
    doc.useVarlib = True
    doc.roundGeometry = True
    doc.read(designspacePath)
    for i in doc.instances:
        path = os.path.join(root,
                            i.familyName.strip().replace(" ", ""),
                            i.styleName.strip().replace(" ", ""),
                            os.path.split(i.filename)[1])
        i.path = path
    print("Generating instance UFOs")
    doc.generateUFO()

    print("Decomposing and removing overlap")
    ufos = getFiles(root, ".ufo")
    length = len(ufos)
    printProgressBar(0, length, prefix='Progress:', suffix='Complete', length=50)
    for i, ufo in enumerate(ufos):
        font = RFont(ufo)

        for glyph in font:
            glyph.decompose()
        for glyph in font:
            glyph.removeOverlap()

        font.save(ufo)
        printProgressBar(i + 1, length, prefix='Progress:', suffix='Complete', length=50)

    print("Seting Panose, weight, and standard stems")
    length = len(ufos)
    printProgressBar(0, length, prefix='Progress:', suffix='Complete', length=50)
    for i, ufo in enumerate(ufos):
        font = RFont(ufo)
        fillInPanoseValues(font)
        font.info.openTypeOS2WeightClass = weightMap[font.info.styleName.split()[2]]
        if font.info.styleName.split()[0] == "Mono":
            font.info.postscriptIsFixedPitch = True
        fixStandardStems(font)
        font.save(ufo)
        printProgressBar(i + 1, length, prefix='Progress:', suffix='Complete', length=50)


def buildFolders(designspace, root):
    """
    Makes folder structure for static mastering
    """
    print("Making folders")
    familyNames = {}
    for i in designspace.instances:
        if i.familyName not in familyNames.keys():
            familyNames[i.familyName] = [i.styleName]
        else:
            styles = familyNames[i.familyName]
            styles.append(i.styleName)
            familyNames[i.familyName] = styles
    for family, styles in familyNames.items():
        basePath = os.path.join(root, family.strip().replace(" ", ""))
        if os.path.exists(basePath):
            shutil.rmtree(basePath)
        for style in styles:
            stylePath = os.path.join(basePath, style.strip().replace(" ", ""))
            os.makedirs(stylePath)


def makeSTAT(directory, doc):
    """
    Create a stylespace.plist for https://github.com/daltonmaag/statmake.
    This is a bit more rational than dealing with TTX files for the STAT
    table, though it still requires a bit of font specific logic in this
    function, ideally one could parse more of the designspace file to get
    the style information, but writing parsing code would take more effort,
    and run into design specific challeges too, so this ends up a bit cleaner.

    Put the axis specific information in the styles dictionary, let the rest
    of the code be generic, save for the special sauce Recursive needs for
    Italic.
    """

    # Style naming info
    styles = {
        "Weight":
        {
            300: "Light",
            400: "Regular",
            500: "Medium",
            600: "SemiBold",
            700: "Bold",
            800: "ExtraBold",
            850: "UltraBold",
            900: "Black"
        },
        "Proportion":
        {
            0: "Sans",
            1: "Mono"
        },
        "Expression":
        {
            0: "Normal",
            1: "Casual"
        },
        "Slant":
        {
            0: "Upright",
            -15: "Italic"
        }
    }

    axes = []
    for axis in doc.axes:
        # Axes are in the order we want (Proportion, Expression, Weight,
        # Slant/Italic), so we can just walk down the list and make a
        # Stylespace file to use. If you need to change values, change the
        # above dictorary of style naming info.
        #
        # Recursive is unusual in that it has both a Italic and Slant
        # axis that need to be linked. This is dealt with at the end.
        if axis.name not in ["Italic", "Slant"]:
            a = {}
            a["name"] = axis.name
            a["tag"] = axis.tag
            locations = []
            if axis.name is "Weight":
                for value, name in styles["Weight"]:
                    if value != 400:
                        locations.append({"name": name, "value": value})
                    else:
                        locations.append({"name": name,
                                          "value": value,
                                          "linked_value": 700,
                                          "flags": ["ElidableAxisValueName"]
                                          })
            elif axis.name is "Proportion":
                for value, name in styles["Proportion"]:
                    locations.append({"name": name, "value": value})
            elif axis.name is "Expression":
                for value, name in styles["Expression"]:
                    if value != 0:
                        locations.append({"name": name, "value": value})
                    else:
                        locations.append({"name": name,
                                          "value": value,
                                          "flags": ["ElidableAxisValueName"]
                                          })
            else:
                for value, name in styles["Slant"]:
                    if value != 0:
                        locations.append({"name": name, "value": value})
                    else:
                        locations.append({"name": name,
                                          "value": value,
                                          "flags": ["ElidableAxisValueName"]
                                          })
            a["locations"] = locations
        else:
            a = {"name": axis.name, "tag": axis.tag}
        axes.append(a)

    stat = {"axes": axes, "locations": locations}
    path = os.path.join(directory, "Recursive.stylespace")
    with open(path, 'wb') as fp:
        plDump(stat, fp)


def main():
    root = os.path.join(os.getcwd(), "build")

    if os.path.exists(root):
        shutil.rmtree(root)

    # Copy files from src/masters, as we need to edit them
    ignore = shutil.ignore_patterns(".git",
                                    ".git*",
                                    "*designspaces*",
                                    "recursive-mono*.designspace",
                                    "recursive-sans*.designspace",
                                    "*varfontprep*",
                                    )
    shutil.copytree("../src/masters", os.path.join(root, "src"), ignore=ignore)
    src = os.path.join(root, "src", "recursive-MONO_XPRN_wght_slnt_ital.designspace")

    static_root = os.path.join(root, "static")
    var_root = os.path.join(root, "var")

    doc = DesignSpaceDocument()
    doc.read(src)

    # Fix default value for weight axis in design space file
    for axis in doc.axes:
        if axis.name == "Weight":
            axis.default = 300

    # Still in memory, but need to save for other operations
    doc.write(src)

    # Make STAT table
    #makeSTAT(src, doc)

    # Sort glyph order


    #  Variable font build
    #print("Building Variable fonts")

    # Fix default va
    # fontmake -m $DS -o variable --output-path $outputDir/$fontName--$date.ttf


    # Static font build
    print("Building Static fonts")
    buildFolders(doc, static_root)
    buildFontMenuDB(doc, static_root)
    buildInstances(src, static_root)


if __name__ == "__main__":
    main()
