import os
import shutil
from ufoProcessor import DesignSpaceProcessor
from fontParts.fontshell import RFont
from fontTools.designspaceLib import DesignSpaceDocument
from defcon import Font


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
    print('\r%s |%s| %s%% %s'%(prefix, bar, percent, suffix), end='\r')
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

    out = ""

    for i in designspace.instances:
        out += f"[{i.postScriptFontName}]\n"
        out += f"    f={i.familyName}\n"
        out += f"    s={i.styleName}\n"
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
    l = len(ufos)
    printProgressBar(0, l, prefix='Progress:', suffix='Complete', length=50)
    for i, ufo in enumerate(ufos):
        font = RFont(ufo)
        for glyph in font:
            glyph.decompose()
        for glyph in font:
            glyph.removeOverlap()
        printProgressBar(i + 1, l, prefix='Progress:', suffix='Complete', length=50)


def buildFeatures():
    pass


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
    src = os.path.join(root, "src", "recursive-prop_xprn_weight_slnt_ital.designspace")

    static_root = os.path.join(root, "static")
    var_root = os.path.join(root, "var")

    doc = DesignSpaceDocument()
    doc.read(src)

    # Fix default value for weight axis in design space file
    for axis in doc.axes:
        if axis.name == "Weight":
            axis.default = 300

    # Make STAT table info


    # Still in memory, but need to save for other operations
    doc.write(src)

    # Sort glyph order

    #  Variable font build
    print("Building Variable fonts")

    # Fix default va
    # fontmake -m $DS -o variable --output-path $outputDir/$fontName--$date.ttf


    # Static font build
#    print("Building Static fonts")
#    buildFolders(doc, static_root)
#    buildFontMenuDB(doc, static_root)
#    buildInstances(src, static_root)


if __name__ == "__main__":
    main()
