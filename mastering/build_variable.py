import os
from plistlib import dump as plDump
from fontTools.designspaceLib import DesignSpaceDocument


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
        "Slant":
        {
            0: "Upright",
            -15: "Italic"
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
        if axis.name not in ["Italic"]:
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
            else:
                for value, name in styles["Slant"].items():
                    if value != 0:
                        locations.append({"name": name, "value": value})
                    else:
                        locations.append({"name": name,
                                          "value": value,
                                          "linked_value": -15,
                                          "flags": ["ElidableAxisValueName"]
                                          })
            a["locations"] = locations
        else:
            a = {"name": axis.name, "tag": axis.tag}
        axes.append(a)

    stat = {"axes": axes}
    path = os.path.join(directory, "Recursive.stylespace")
    with open(path, 'wb') as fp:
        plDump(stat, fp, sort_keys=False)

    print("🏗  Made stylespace")


def build_variable(designspacePath, root):

    doc = DesignSpaceDocument.fromfile(designspacePath)

    # Fix default value for weight axis in design space file
    for axis in doc.axes:
        if axis.name == "Weight":
            axis.default = 300

    # Still in memory, but need to save for other operations
    doc.write(doc)


    #  Variable font build
    #print("Building Variable fonts")

    # Fix default va
    # fontmake -m $DS -o variable --output-path $outputDir/$fontName--$date.ttf
