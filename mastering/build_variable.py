import os
from plistlib import dump as plDump
import fontTools.ttLib
from fontmake.font_project import FontProject
from fontTools.designspaceLib import DesignSpaceDocument
from statmake.lib import apply_stylespace_to_variable_font
from statmake.classes import Stylespace


def makeSTAT(directory, designspace):
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
        "Italic":
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
        if axis.name not in ["Italic", "Slant"]:
            a = {}
            a["name"] = axis.name
            a["tag"] = axis.tag
            locations = []
            if axis.name == "Weight":
                for value, name in styles["Weight"].items():
                    if value != 400:
                        locations.append({"name": name, "value": value})
                    else:
                        locations.append({"name": name,
                                          "value": value,
                                          "linked_value": 700,
                                          "flags": ["ElidableAxisValueName"]
                                          })
            elif axis.name == "Monospace":
                for value, name in styles["Monospace"].items():
                    locations.append({"name": name, "value": value})
            elif axis.name == "Casual":
                for value, name in styles["Casual"].items():
                    if value != 0:
                        locations.append({"name": name, "value": value})
                    else:
                        locations.append({"name": name,
                                          "value": value,
                                          })
            a["locations"] = locations
        else:
            a = {"name": axis.name, "tag": axis.tag}
        axes.append(a)

    locations = []
    for values, name in styles["Italic"].items():
        location = {}
        location["name"] = name
        axis_values = {}
        axis_values["Slant"] = values[0]
        axis_values["Italic"] = values[1]
        location["axis_values"] = axis_values
        if values[0] == 0:
            location["flags"] = ["ElidableAxisValueName"]
        locations.append(location)

    stat = {"axes": axes, "locations": locations}
    path = os.path.join(directory, "Recursive.stylespace")
    with open(path, 'wb') as fp:
        plDump(stat, fp, sort_keys=False)

    print("🏗  Made stylespace")
    return path


def build_variable(designspacePath,
                   stylespacePath=None,
                   out=None,
                   verbose="ERROR",
                   ):

    if out is None:
        out = os.path.splitext(os.path.basename(designspacePath))[0] + "-VF.ttf"

    print("🏗  Constructing variable font")
    fp = FontProject(verbose=verbose)
    fp.build_variable_font(designspacePath,
                           output_path=out,
                           useProductionNames=True)

    if stylespacePath is not None:
        print("🏗  Adding STAT table")
        ds = DesignSpaceDocument.fromfile(designspacePath)
        additional_locations = ds.lib.get("org.statmake.additionalLocations",
                                          {})
        font = fontTools.ttLib.TTFont(out)
        stylespace = Stylespace.from_file(stylespacePath)
        apply_stylespace_to_variable_font(stylespace,
                                          font,
                                          additional_locations)
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
