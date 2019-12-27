import os
import shutil
from ufoProcessor import DesignSpaceProcessor
from fontParts.fontshell import RFont as Font

# Family specific data

weightMap = {
             "ExtraBlack": 1000,
             "Black": 900,
             "ExtraBold": 800,
             "Bold": 700,
             "SemiBold": 600,
             "Medium": 500,
             "Regular": 400,
             "Light": 300,
            }


def buildNameMap():
    """
    To keep data in one place, we store how we want to break the static
    familes apart in the instance_names.csv file. Read this to get the
    corrent family and style names for the staticleac fonts.
    """
    import csv
    names = {}
    with open('data/instance_names.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            names[(row["Var Instance Family Name"],
                   row["Var Instance Style Name"])] = (row["Static Family Name"],
                                                       row["Static Style Name"])
    return names


def fillInPanoseValues(font):
    """
    Fills in the Panose values for a font based on the style name.
    Uses the  panoseWeightMap to set weight values, the presense of
    'Mono' to set if it's monospaced, and the presense of 'Italic' to
    set if it's oblique. 'Casual' and 'Linear' trigger settings for
    the style.
    """

    panoseWeightMap = {
                       "ExtraBlack": 11,
                       "Black": 10,
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

    print("✅  Filled in Panose Values")


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

    print("✅  Fixed standard stems")


def buildInstances(designspacePath, root, name_map):
    doc = DesignSpaceProcessor()
    doc.useVarlib = True
    doc.roundGeometry = True
    doc.read(designspacePath)
    for i in doc.instances:
        fn, sn = name_map[(i.familyName, i.styleName)]
        path = os.path.join(root,
                            fn.strip().replace(" ", ""),
                            sn.strip().replace(" ", ""),
                            os.path.split(i.filename)[1])
        i.path = path
    print("🏗  Generating instance UFOs")
    doc.generateUFO()

    print("🏗  Decomposing and removing overlap")
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

    print("🏗  Seting Panose, weight, and standard stems")
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

    print("✅  Made UFO instances")


def buildFolders(designspace, root, name_map):
    """
    Makes folder structure for static mastering
    """
    print("🏗  Making folders for static fonts")
    familyNames = {}
    for i in designspace.instances:
        fn, sn = name_map[(i.familyName, i.styleName)]
        if fn not in familyNames.keys():
            familyNames[fn] = [sn]
        else:
            styles = familyNames[fn]
            styles.append(sn)
            familyNames[fn] = styles
    for family, styles in familyNames.items():
        basePath = os.path.join(root, family.strip().replace(" ", ""))
        if os.path.exists(basePath):
            shutil.rmtree(basePath)
        for style in styles:
            stylePath = os.path.join(basePath, style.strip().replace(" ", ""))
            os.makedirs(stylePath)

    print("🏗  Made folders for static fonts")


def buildFontMenuDB(designspace, root, name_map):
    """
    Pulls the postscript, and the mapping names from the designspace.
    Transforms the family name from "Recursive" to either "Recursive Sans"
    or "Recursive Mono" for the static fonts.
    """

    out = ""

    for i in designspace.instances:
        fn, sn = name_map[(i.familyName, i.styleName)]
        out += f"[{i.postScriptFontName}]\n"
        out += f"    f={fn}\n"
        out += f"    s={sn}\n"
        out += f"    l={i.styleMapFamilyName}\n"
        if i.styleMapStyleName != "Regular":
            out += f"    m=1,{i.styleMapFamilyName} {i.styleMapStyleName}\n\n"
        else:
            out += f"    m=1,{i.styleMapFamilyName}\n\n"

    path = os.path.join(root, "FontMenuNameDB")
    with open(path, "w") as f:
        f.write(out)

    print("🏗  Made FontMenuDB")


def buildGlyphOrderAndAlias(designspace):
    pass


def buildFontInfo(font):
    pass


def buildFeatures(font):
    pass


def buildStatic(designspacePath, outputPath):
    """
    Reads designspace file, generates instance UFOs,
    builds mastering files for the Adobe FDK, then
    builds files.

    *designspacePath* is the path to the designspace file.
    *outputPath* is the path for file builds.

    """
    print("Building Static fonts")
    name_map = buildNameMap()
    buildFolders(doc, static_root, name_map)
    buildFontMenuDB(doc, static_root, name_map)
    buildInstances(src, static_root, name_map)
