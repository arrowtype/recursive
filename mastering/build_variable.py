import os
import fontTools.ttLib
import shutil
from fontmake.font_project import FontProject
from fontTools.designspaceLib import DesignSpaceDocument
from fontParts.fontshell import RFont as Font
from fontTools.otlLib.builder import buildStatTable
from utils import getFiles, make_mark_mkmk_gdef_feature


def buildFeatures(src):
    """
    Replaces the features.fea file in the UFO with the external
    features.fea file

    *src* is the source directory with the UFOs and external features.fea file
    """
    ufos = getFiles(src, "ufo")
    feature = os.path.join(src, "features.fea")
    for ufo in ufos:
        shutil.copy(feature, ufo)
    print("🏗  Moved features into UFOs")
    for ufo in ufos:
        font = Font(ufo)
        mark_mkmk_gdef = make_mark_mkmk_gdef_feature(font)
        font.features.text += mark_mkmk_gdef
        font.save(font.path)
    print("🏗  Added mark, mkmk, and GDEF to features")


def makeSTAT(font, designspace):
    """
    Uses fontTools.otlLib.builder.buildStatTable to build the STAT table.

    *font* is a `fontTools` font object.
    *designspace* is a `DesignSpaceDocument` object
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
            900: "Black",
            1000: "ExtraBlack"
        },
        "Monospace":
        {
            0: "Sans",
            1: "Mono"
        },
        "Casual":
        {
            0: "Linear",
            1: "Casual"
        },
        "Slant":
        {
            (0, 0.5): "Upright",
            (-15, 1): "Italic"
        }
    }

    axes = []
    for axis in designspace.axes:
        # Axes are in the order we want (Proportion, Expression, Weight,
        # Slant/Italic), so we can just walk down the list and make a
        # Stylespace file to use. If you need to change values, change the
        # above dictorary of style naming info.
        #
        # Recursive is unusual in that it has both a Italic and Slant
        # axis that need to be linked. This is dealt with at the end.
        if axis.name not in ["Cursive", "Slant"]:
            a = {}
            a["tag"] = axis.tag
            a["name"] = axis.name
            locations = []
            if axis.name == "Weight":
                for value, name in styles["Weight"].items():
                    if value != 400:
                        locations.append({"name": name, "value": value})
                    else:
                        locations.append({"name": name,
                                          "value": value,
                                          "linkedValue": 700,
                                          "flags": 0x2
                                          })
            else:
                for value, name in styles[axis.name].items():
                    locations.append({"name": name, "value": value})
            a["values"] = locations
        else:
            a = {"name": axis.name, "tag": axis.tag}
        axes.append(a)

    locations = []
    for values, name in styles["Slant"].items():
        location = {}
        location["name"] = name
        axis_values = {}
        axis_values["slnt"] = values[0]
        axis_values["CRSV"] = values[1]
        location["location"] = axis_values
        if values[0] == 0:
            location["flags"] = 0x2
        locations.append(location)

    buildStatTable(font, axes, locations)


def build_variable(designspacePath,
                   out=None,
                   verbose="ERROR",
                   ):
    """
    Builds a variable font from a designspace using fontmake.
    Post applies the STAT table using a stylespace if given.

    *designspacePath* a `string` of the path to the designspace
    *stylespacePath* a `string` of the path to the stylespace
    *out* a `string` of the path where the varible font should be saved
    *verbose* sets the verbosity level for fontmake. Defaults to "ERROR"
    """

    if out is None:
        out = os.path.splitext(os.path.basename(designspacePath))[0] + "-VF.ttf"

    else:
        if not os.path.exists(os.path.split(out)[0]):
            os.mkdir(os.path.split(out)[0])

    print("🏗  Constructing variable font")
    fp = FontProject(verbose=verbose)
    fp.build_variable_font(designspacePath,
                           output_path=out,
                           useProductionNames=True)

    print("🏗  Adding STAT table")
    ds = DesignSpaceDocument.fromfile(designspacePath)
    font = fontTools.ttLib.TTFont(out)
    makeSTAT(font, ds)
    font.save(out)

    font = fontTools.ttLib.TTFont(out)

    print("🏗  Add gasp table")
    gasp = fontTools.ttLib.newTable("gasp")
    gasp.gaspRange = {0xFFFF: 15}
    font["gasp"] = gasp

    print("🏗  Fix prep table")
    program = fontTools.ttLib.tables.ttProgram.Program()

    assembly = ['PUSHW[]',
                '511',
                'SCANCTRL[]',
                'PUSHB[]',
                '4',
                'SCANTYPE[]']
    program.fromAssembly(assembly)
    prep = fontTools.ttLib.newTable("prep")
    prep.program = program
    font["prep"] = prep

    print("🏗  Add dsig table")
    dsig = fontTools.ttLib.newTable("DSIG")
    dsig.ulVersion = 1
    dsig.usFlag = 0
    dsig.usNumSigs = 0
    dsig.signatureRecords = []
    font["DSIG"] = dsig

    print("🏗  Set fsType to 0")
    font["OS/2"].fsType = 0

    font.save(out)

    print("✅ Built variable font")


if __name__ == "__main__":
    import argparse
    description = "Builds the Recursive variable font."
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("designspacePath",
                        help="The path to a designspace file")
    parser.add_argument("-s", "--stylespace",
                        help="Path to the stylespace file")
    parser.add_argument("-o", "--out",
                        help="Output path")
    args = parser.parse_args()
    designspacePath = args.designspacePath
    stylespacePath = args.stylespace
    out = args.out

    build_variable(designspacePath, stylespacePath=stylespacePath, out=out)
