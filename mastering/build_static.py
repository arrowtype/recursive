import os
import shutil
import re
from ufoProcessor import DesignSpaceProcessor
from fontParts.fontshell import RFont as Font
from ufo2ft import compileTTF
from utils import getFiles, printProgressBar

# Family specific data

# Maps weight name from postscript full name to
# (OS/2 weight, Panose weight) values
weightMap = {
             "XBlk": (1000, 11),
             "Blk": (900, 10),
             "XBd": (800, 9),
             "Bold": (700, 8),
             "SmBd": (600, 7),
             "Med": (500, 6),
             "Regular": (400, 5),
             "Lt": (300, 4),
            }


def buildNameMap():
    """
    To keep data in one place, we store how we want to break the static
    familes apart in the instance_names.csv file. Read this to get the
    corrent family and style names for the static fonts.
    """
    import csv
    names = {}
    with open('data/instance_names.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            varFamily = row["Var Instance Family Name"]
            varStyle = row["Var Instance Style Name"]
            staticFamily = row["Static Family Name"]
            staticStyle = row["Static Style Name"]
            familymap = row["familymap"]
            stylemap = row["stylemap"]
            if stylemap != "Regular":
                fn = f"{familymap} {stylemap}"
            else:
                fn = f"{familymap}"
            names[(varFamily, varStyle)] = (staticFamily, staticStyle, fn)

    return names


def getBlueScale(fonts):
    """
    Calculates the correct blue scale for the family based on the max
    blue zone height. Also sets the `font.info.postscriptBlueFuzz` to
    0, which should be the default value, but it does this just to be
    sure that the value is set correctly (some UFO versions have this
    set to a different value).

    Returns a `float` that is the blueScale value. If no PS zones are
    set, it falls back to the default value (0.039625)

    *font* is a font object (Defcon or FontParts)
    """
    maxZoneHeight = 0
    blueScale = 0.039625

    for font in fonts:
        font.info.postscriptBlueFuzz = 0
        blues = font.info.postscriptBlueValues
        otherBlues = font.info.postscriptOtherBlues
        if blues:
            assert len(blues) % 2 == 0
            for x, y in zip(blues[:-1:2], blues[1::2]):
                maxZoneHeight = max(maxZoneHeight, abs(y-x))
        if otherBlues:
            assert len(otherBlues) % 2 == 0
            for x, y in zip(otherBlues[:-1:2], otherBlues[1::2]):
                maxZoneHeight = max(maxZoneHeight, abs(y-x))

    if maxZoneHeight != 0:
        blueScale = float(3)/float((4*maxZoneHeight))

    return blueScale


def fillInPanoseValues(font, weight):
    """
    Fills in the Panose values for a font based on the style name.
    Uses the  panoseWeightMap to set weight values, the presense of
    'Mono' to set if it's monospaced, and the presense of 'Italic' to
    set if it's oblique. 'Casual' and 'Linear' trigger settings for
    the style.

    *font* is a font object (Defcon or FontParts)
    *weight* is a `string` of the font's weight value
    """
    names = font.info.postscriptFullName.split()

    if names[1] == "Mono":
        prop = 9
    else:
        prop = 4

    if "Italic" in names:
        form = 11
    else:
        form = 4

    wght = weightMap[weight][1]

    if names[2] == "Csl":
        font.info.openTypeOS2Panose = [2, 15, wght, prop, 5, 5, 2, form, 3, 4]
    else:
        font.info.openTypeOS2Panose = [2, 11, wght, prop, 4, 2, 2, form, 2, 4]


def makeTTF(ufos):
    pass


def fixStandardStems(font):
    """
    List of standard stems in source UFOs are sometimes duplicated
    so that all masters have interpolatable lists for the instances.
    This shortens the list of standard stems by removing duplicates.

    For italic fonts, the Type 1 spec states that only one vertical
    stem should be set, this is pulled from the lowercase straight
    vertical.

    *font* is a font object (Defcon or FontParts)
    """

    from collections import OrderedDict
    hStems = font.info.postscriptStemSnapH
    newHStems = list(OrderedDict.fromkeys(hStems))
    font.info.postscriptStemSnapH = newHStems
    vStems = font.info.postscriptStemSnapV
    if "Italic" in font.info.styleName.split():
        font.info.postscriptStemSnapV = [vStems[2]]
    else:
        newVStems = list(OrderedDict.fromkeys(vStems))
        font.info.postscriptStemSnapV = newVStems


def writeKerning(font, path):
    """
    Uses ufo2ft to write out the *font*'s kerning feature file to the *path*

    *font* is a font object (Defcon or FontParts)
    *path* is a `string` of the path to write the kerning feature file
    """
    from ufo2ft.featureWriters.kernFeatureWriter import KernFeatureWriter, ast

    feaFile = ast.FeatureFile()
    w = KernFeatureWriter()
    w.write(font, feaFile)
    with open(path, "w") as f:
        f.write(str(feaFile))


def buildFontInfo(stylename, dir):
    """
    Makes the fontinfo file for the Adobe FDK

    Setting 'IsOS/2OBLIQUE' causes weird things to happen with italic fonts
    so we never set that to true.

    *stylename* is a `string` of the font's style (font.info.styleName)
    *dir* is a `string` of the path to the directory where the UFO is
    """
    style = stylename.split()
    bold = italic = "false"
    if "Bold" in style:
        bold = "true"
    if "Italic" in style:
        italic = "true"
    fontinfo = (f"IsBoldStyle {bold}\n"
                f"IsItalicStyle {italic}\n"
                "PreferOS/2TypoMetrics true\n"
                "IsOS/2WidthWeigthSlopeOnly true\n"
                "IsOS/2OBLIQUE false\n")
    path = os.path.join(dir, "fontinfo")
    with open(path, "w") as f:
        f.write(fontinfo)


def writeFeature(font):
    """
    Write the font specific features file

    *font* is a font object (Defcon or FontParts)
    """
    path = os.path.join(os.path.split(font.path)[0], "features")
    hhea = (f"table hhea {{\n"
            f"    Ascender {font.info.openTypeHheaAscender};\n"
            f"    Descender {font.info.openTypeHheaDescender};\n"
            f"    LineGap {font.info.openTypeHheaLineGap};\n"
            f"}} hhea;\n\n")
    os2 = (f"table OS/2 {{\n"
           f"    FSType 0;\n"
           f"    Panose {' '.join(str(x) for x in font.info.openTypeOS2Panose)};\n"
           f"    TypoAscender {font.info.openTypeOS2TypoAscender};\n"
           f"    TypoDescender {font.info.openTypeOS2TypoDescender};\n"
           f"    TypoLineGap {font.info.openTypeOS2TypoLineGap};\n"
           f"    winAscent {font.info.openTypeOS2WinAscent};\n"
           f"    winDescent {font.info.openTypeOS2WinDescent};\n"
           f"    XHeight {font.info.xHeight};\n"
           f"    CapHeight {font.info.capHeight};\n"
           f"    WeightClass {font.info.openTypeOS2WeightClass};\n"
           f"    WidthClass {font.info.openTypeOS2WidthClass};\n"
           f'    Vendor "{font.info.openTypeOS2VendorID}";\n'
           f"}} OS/2;\n\n")
    includes = ("include (../../features.family);\n"
                "include (../../features.fea);\n"
                "include (kern.fea);\n")
    out = hhea + os2 + includes
    with open(path, "w") as f:
        f.write(out)


def buildFamilyFeatures(root, features, version):
    fea_root = os.path.split(features)[0]
    regex = re.compile(r'/.+/(.+\.fea)')
    feature = []
    with open(features, 'r') as f:
        for l in f:
            if l.startswith("languagesystem"):
                feature.append(l)
            elif l.startswith("#"):
                pass
            elif l.startswith("include"):
                match = regex.search(l)
                path = os.path.join(fea_root, "features", match.group(1))
                with open(path, 'r') as fea:
                    for l in fea:
                        feature.append(l.replace("\t", "    "))
                feature.append("\n\n")
            else:
                feature.append(l)
    path = os.path.join(root, "features.fea")
    with open(path, 'w') as f:
        f.write("".join(feature))

    head = ("table head {\n"
            f"    FontRevision {version};\n}}"
            "head;\n")
    base = (
            "table BASE {\n"
            "    HorizAxis.BaseTagList       ideo  romn;\n"
            "    HorizAxis.BaseScriptList    DFLT    romn    -250 0,\n"
            "                                latn    romn    -250 0;\n"
            "} BASE;\n"
            )
    name = (
            "table name {\n"
            '    nameid 0 "Copyright 2019 The Recursive Project Authors (github.com/arrowtype/recursive).";\n'
            '    nameid 0 1 "Copyright 2019 The Recursive Project Authors (github.com/arrowtype/recursive)";\n'
            "} name;\n"
            )
    path = os.path.join(root, "features.family")
    with open(path, "w") as f:
        f.write("\n".join([head, base, name]))
    print("🏗  Made Family features")


def buildInstances(designspacePath, root, name_map):
    doc = DesignSpaceProcessor()
    doc.useVarlib = True
    doc.roundGeometry = True
    doc.read(designspacePath)
    for i in doc.instances:
        fn, sn, _ = name_map[(i.familyName, i.styleName)]
        path = os.path.join(root,
                            fn.strip().replace(" ", ""),
                            sn.strip().replace(" ", ""),
                            os.path.split(i.filename)[1].strip().replace(" ", ""))
        i.path = path
    print("🏗  Generating instance UFOs")
    doc.generateUFO()

    ufos = getFiles(root, ".ufo")
    fonts = [Font(ufo) for ufo in ufos]

    print("🏗  Getting blueScale")
    blueScale = getBlueScale(fonts)

    print("🏗  Setting values, removing overlap, writing files")
    length = len(fonts)
    printProgressBar(0, length, prefix='  ', suffix='Complete', length=50)
    for i, font in enumerate(fonts):
        font_dir = os.path.split(font.path)[0]

        # Font info
        # Get and set PS Font Full Name
        fullname = name_map[(font.info.familyName, font.info.styleName)][2]
        font.info.postscriptFullName = fullname

        # Get weight value based on fullname
        # 'Regular' is not part of the fullname so we do a try/except
        # that will throw an IndexError if the fullname is a Regular
        # style ("Recursive Mono Csl", "Recursive Mono Lnr",
        # "Recursive Sans Csl", or "Recursive Sans Lnr"). We know then
        # that the font weight value should be 400. Likewise, if the
        # fourth item in the name is "Italic", the weight should be
        # 400, so we catch that here too.
        try:
            weight = fullname.split()[3]
            if weight == "Italic":
                weight = "Regular"
        except IndexError:
            weight = "Regular"

        # Set weight class
        font.info.openTypeOS2WeightClass = weightMap[weight][0]

        # Set Panose
        fillInPanoseValues(font, weight)

        # Set fixed pitch if font is Mono
        if fullname.split()[0] == "Mono":
            font.info.postscriptIsFixedPitch = True

        # Fix standard stems
        fixStandardStems(font)

        # Set blueScale
        font.info.postscriptBlueScale = blueScale

        # Font cleanup
        # Remove overlap in the font
        for glyph in font:
            glyph.removeOverlap()
        font.save(font.path)

        # External files
        # Write out the `fontinfo` file
        buildFontInfo(font.info.styleName, font_dir)

        # Write out the kerning feature file
        path = os.path.join(font_dir, "kern.fea")
        writeKerning(font, path)

        # Write out the font feature file
        writeFeature(font)

        printProgressBar(i + 1, length, prefix='  ',
                         suffix='Complete', length=50)

    print("✅ Made UFO instances")


def buildFolders(designspace, root, name_map):
    """
    Makes folder structure for static mastering
    """
    familyNames = {}
    for i in designspace.instances:
        fn, sn, _ = name_map[(i.familyName, i.styleName)]
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

    for i in designspace.instances:
        fn, sn, m1 = name_map[(i.familyName, i.styleName)]
        out = (f"[{i.postScriptFontName}]\n"
               f"    f={fn}\n"
               f"    s={sn}\n"
               f"    l={i.styleMapFamilyName}\n"
               f"    m=1,{m1}\n\n"
               )

    path = os.path.join(root, "FontMenuNameDB")
    with open(path, "w") as f:
        f.write(out)

    print("🏗  Made FontMenuDB")


def buildGlyphOrderAndAlias(fontPath, root):
    font = Font(fontPath)
    order = font.glyphOrder
    mapping = font.lib["public.postscriptNames"]
    path = os.path.join(root, "GlyphOrderAndAliasDB")
    with open(path, "w") as f:
        for name in order:
            if name in font.keys():
                glyph = font[name]
                finalName = mapping[name]
                if len(glyph.unicodes) > 1:
                    unicodes = [f"uni{uni:04X}" for uni in glyph.unicodes]
                    out = f"{finalName}\t{name}\t{','.join(unicodes)}\n"
                else:
                    out = f"{finalName}\t{name}\n"
                f.write(out)
        f.write("\n")


def makeOTF(root):


def buildStatic(root, otf=True, ttf=True):
    """
    Reads designspace file, generates instance UFOs,
    builds mastering files for the Adobe FDK, then
    builds files.

    *designspacePath* is the path to the designspace file.
    *outputPath* is the path for file builds.

    """
    print("Building Static fonts")
    name_map = buildNameMap()
