'''
    Generate designspace rules for diacritics.

    This script is meant to be used outside of RoboFont. It requires fontParts to be installed.
'''

import sys
from fontParts.world import OpenFont, RFont, RGlyph

try:
    fontPath = (sys.argv[1])
except IndexError:
    print("no arg; using pre-written font path")
    fontPath = '/Users/stephennixon/type-repos/recursive/src/masters/recursive-varfontprep-2019_10_31-11_00_21/Recursive Mono-Casual B.ufo'

font = OpenFont(fontPath, showInterface=False)

suffixes = ["italic", "mono", "sans"]



rules = {
    "mono": {
        "Monospace": ("0.49", "1"),
        "Slant": ("-7.490000", "0"),
        "Italic": ("0", "0.890000"),
    },
    "mono roman": {
        "Monospace": ("0.49", "1"),
        "Italic": ("0", "0.090000"),
    },
    "mono autoitalic": {
        "Monospace": ("0.49", "1"),
        "Slant": ("-15", "-7.500000"),
        "Italic": ("0.100000", "1"),
    },
    "mono italic": {
        "Monospace": ("0.49", "1"),
        "Italic": ("0.900000", "1"),
    },
    "sans": {
        "Monospace": ("0", "0.49"),
        "Slant": ("-15", "0"),
    },
    "sans autoroman": {
        "Monospace": ("0", "0.49"),
        "Slant": ("-7.490000", "0"),
        "Italic": ("0", "0.890000"),
    },
    "sans roman": {
        "Monospace": ("0", "0.49"),
        "Italic": ("0", "0.090000"),
    },
    "sans autoitalic": {
        "Monospace": ("0", "0.49"),
        "Slant": ("-15", "-7.500000"),
        "Italic": ("0.100000", "1"),
    },
    "italic": {
        "Monospace": ("0", "0.49"),
        "Italic": ("0.900000", "1"),
    }
}

for g in font:
    if '.' in g.name and g.name.split('.')[1] in suffixes:
        # print(g)
        print(f"<sub name="{g.name.split('.')[0]}" with="{g.name}" />")

font.close()

# go through glyph construction recipes and pull out all suffixed glyphs
# OR go through the charset of a UFO and find all suffixes that have dict rules
# print(suffix)
# print(f"<sub name="{baseDiacritic}" with="{baseDiacritic}.{suffix}" />")


# only do this for diacritics which have bases in certain rule set
