'''
    Generate designspace rules for diacritics.

    This script is meant to be used outside of RoboFont. It requires fontParts to be installed.
'''
import os
import sys
from fontParts.world import OpenFont, RFont, RGlyph

try:
    fontPath = (sys.argv[1])
except IndexError:
    print("no arg; using pre-written font path")
    fontPath = '/Users/stephennixon/type-repos/recursive/src/masters/mono/Recursive Mono-Casual A.ufo'



suffixes = ["italic", "mono", "sans"]

italicsNotInSans = "c f r j s z".split()

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


head, tail = os.path.split(fontPath)

newPath = head + '/gsub-rules.txt'

GSUBrules = open(newPath,"w+")

def printWrite(line):
    print(line)
    GSUBrules.write(line)

font = OpenFont(fontPath, showInterface=False)

def makeRules():
    for suffix in suffixes:
        printWrite(f'\n'.ljust(80,'-') + '\n')
        printWrite(f'{suffix} '.ljust(80,'-') + '\n')
        printWrite('\n')
        for g in font:
            if '.' in g.name and g.name.split('.')[1] == suffix:
                # print(g)
                baseName = g.name.split('.')[0]
                rule = f'<sub name="{baseName}" with="{g.name}" />'
                printWrite(rule + '\n')

def makeSansItalicRules():
    printWrite(f'\n'.ljust(80,'-') + '\n')
    printWrite(f'sans italic '.ljust(80,'-') + '\n')
    printWrite('\n')
    for g in font:
        if '.' in g.name and\
            g.name.split('.')[1] == 'italic' and\
            g.name.split('.')[0][0] not in italicsNotInSans:

            baseName = g.name.split('.')[0]
            rule = f'<sub name="{baseName}" with="{g.name}" />'
            printWrite(rule + '\n')

makeRules()
makeSansItalicRules()

font.close()

GSUBrules.close()

# go through glyph construction recipes and pull out all suffixed glyphs
# OR go through the charset of a UFO and find all suffixes that have dict rules
# print(suffix)
# print(f"<sub name="{baseDiacritic}" with="{baseDiacritic}.{suffix}" />")


# only do this for diacritics which have bases in certain rule set

# TODO: limit these rules to what bases are already in a selected designspace?
    # sans: do not italicize
    # c
    # f
    # s
    # r
    # z