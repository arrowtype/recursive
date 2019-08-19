#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ========================================================
# vf2s.py
# Copyright 2019 Google, LLC
# Apache License, v2.0
#
# A variable font to static font instance generator
# + unique name table writer
# =======================================================

# PyInstaller build for macOS architecture
#
# pyinstaller -c --onefile --hidden-import=fontTools --clean --distpath="dist/macos64" -n vf2s vf2s.py

import os
import sys
import argparse

from fontTools.ttLib import TTFont
from fontTools.varLib.mutator import instantiateVariableFont

SCRIPT_VERSION = "v0.6.1"

# Define font name for font path and name table re-writes

FONTNAME = "Recursive SemiCasual"

# Default axis values (when not explicitly included on the command line)
DEFAULT_EXPRESSION = 0.0
DEFAULT_WEIGHT = 400
DEFAULT_SLANT = 0.0
DEFAULT_ITALIC = 0.5

# Min/Max of design axis range values for validity checking command line entries
EXPRESSION_MIN = 0
EXPRESSION_MAX = 1

WEIGHT_MIN = 300
WEIGHT_MAX = 900

SLANT_MIN = 0.0
SLANT_MAX = -15.0

ITALIC_MIN = 0.0
ITALIC_MAX = 1.0


# macOS rendering bit
# used for workaround fix for fontTools varLib.mutator bug
MAC_OVERLAP_RENDERING_BIT = 1 << 6

# nncnnoocoo
def set_mac_overlap_rendering_bit(font):
    """Sets the bit6 macOS overlap rendering bit."""
    glyf = font["glyf"]
    for glyph_name in glyf.keys():
        glyph = glyf[glyph_name]
        # Only needs to be set for glyphs with contours
        if glyph.numberOfContours > 0:
            glyph.flags[0] |= MAC_OVERLAP_RENDERING_BIT
    return font


def main():
    parser = argparse.ArgumentParser(
        description="A variable font to static instance generator."
    )
    parser.add_argument(
        "-x",
        "--expression",
        default=DEFAULT_EXPRESSION,
        type=float,
        help="Expression axis value ({}-{})".format(EXPRESSION_MIN, EXPRESSION_MAX),
    )  # xprn
    parser.add_argument(
        "-w",
        "--weight",
        default=DEFAULT_WEIGHT,
        type=int,
        help="Weight axis value ({}-{})".format(WEIGHT_MIN, WEIGHT_MAX),
    )  # wght
    parser.add_argument(
        "-s",
        "--slant",
        default=DEFAULT_SLANT,
        type=float,
        help="Slant axis value ({}-{})".format(SLANT_MIN, SLANT_MAX),
    )  # slnt
    parser.add_argument(
        "-i",
        "--italic",
        default=DEFAULT_SLANT,
        type=float,
        help="Italic axis value ({}-{})".format(ITALIC_MIN, ITALIC_MAX),
    )  # slnt
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="vf2s {}".format(SCRIPT_VERSION),
        help="Display application version",
    )
    parser.add_argument(
        "--style",
        default="Regular",
        type=str,
        help="Style linking style name: Italic, Bold, Bold Italic, etc (default is 'Regular')",
    )
    parser.add_argument("path", help="Variable font path")

    args = parser.parse_args()

    instance_location = {}
    # axis value validity testing and location definitions
    if args.weight is not None:
        if args.weight < WEIGHT_MIN or args.weight > WEIGHT_MAX:
            sys.stderr.write(
                "Weight axis value must be in the range {} - {}{}".format(
                    WEIGHT_MIN, WEIGHT_MAX, os.linesep
                )
            )
            sys.exit(1)
        else:
            instance_location["wght"] = args.weight
    if args.expression is not None:
        if args.expression < EXPRESSION_MIN or args.expression > EXPRESSION_MAX:
            sys.stderr.write(
                "Expression axis value must be in the range {} - {}{}".format(
                    EXPRESSION_MIN, EXPRESSION_MAX, os.linesep
                )
            )
            sys.exit(1)
        else:
            instance_location["XPRN"] = args.expression
    if args.slant is not None:
        # slant is negative, 0 to -15
        # SLANT_MIN = 0.0
        # SLANT_MAX = -15.0
        if args.slant > SLANT_MIN or args.slant < SLANT_MAX:
            sys.stderr.write(
                "Slant axis value must be in the range {} - {}{}".format(
                    SLANT_MIN, SLANT_MAX, os.linesep
                )
            )
            sys.exit(1)
        else:
            instance_location["slnt"] = args.slant
        instance_location["slnt"] = args.slant
    if args.italic is not None:
        if args.italic < ITALIC_MIN or args.italic > ITALIC_MAX:
            sys.stderr.write(
                "Italic axis value must be in the range {} - {}{}".format(
                    ITALIC_MIN, ITALIC_MAX, os.linesep
                )
            )
            sys.exit(1)
        else:
            instance_location["ital"] = args.italic

    # variable font path check
    if not os.path.exists(args.path):
        sys.stderr.write(
            "{} does not appear to be a valid path to a variable font{}".format(
                args.path, os.linesep
            )
        )
        sys.exit(1)

    # instantiate the variable font with the requested values
    font = TTFont(args.path)
    instantiateVariableFont(font, instance_location, inplace=True, overlap=False)
    print(f"Generating static instance at {instance_location}")

    # ---------------------------------------------------------------
    # rewrite name table records with new name values for A/B testing
    # ---------------------------------------------------------------

    namerecord_list = font["name"].names

    # create a name string from the axis location parameters
    axis_param_string = ""
    for axis_value in instance_location:
        axis_param_string += "{}{}".format(axis_value, instance_location[axis_value])

    # map axis name to an abbreviation in font path and name table record string values
    axis_param_string = axis_param_string.replace("XPRN", "xp")
    axis_param_string = axis_param_string.replace("wght", "wg")
    axis_param_string = axis_param_string.replace("slnt", "sl")
    axis_param_string = axis_param_string.replace("ital", "it")

    # name definitions (NEEDS TO BE MODIFIED TO SUPPORT STYLES OTHER THAN REGULAR)
    nameID1_name = "{}".format(FONTNAME)
    nameID2_name = "{}".format(args.style)
    nameID4_name = "{} {}".format(FONTNAME, args.style)
    nameID6_name = "{}-{}".format(FONTNAME, args.style)
    outfont_name = "{}-{}-{}.ttf".format(FONTNAME, axis_param_string, args.style)
    outfont_path = os.path.join(
        os.path.dirname(os.path.abspath(args.path)), outfont_name.replace(" ", "_")
    )

    # TODO: update unique font identifier, name 3

    for record in namerecord_list:
        if record.nameID == 1:
            record.string = nameID1_name
        elif record.nameID == 2:
            record.string = nameID2_name
        elif record.nameID == 4:
            record.string = nameID4_name
        elif record.nameID == 6:
            record.string = nameID6_name.replace(" ","")
        elif record.nameID == 16:
            record.string = nameID1_name
        elif record.nameID == 17:
            record.string = nameID2_name

    # Set the macOS overlap rendering bit
    # addresses bug in overlap path rendering on macOS web browsers
    font = set_mac_overlap_rendering_bit(font)

    # write the instance font to disk
    try:
        font.save(outfont_path)
        print("[New instance]: {}".format(outfont_path))
    except Exception as e:
        sys.stderr.write(
            "Failed to write font file {} with error: {}{}".format(
                outfont_name, str(e), os.linesep
            )
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
