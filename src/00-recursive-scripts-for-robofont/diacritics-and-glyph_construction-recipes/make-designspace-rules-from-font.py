'''
    Generate designspace rules for diacritics.

    This script is meant to be used outside of RoboFont. It requires fontParts to be installed.
'''
import os
import sys
from fontParts.world import OpenFont, RFont, RGlyph
from datetime import datetime



try:
    fontPath = (sys.argv[1])
except IndexError:
    print("no arg; using pre-written font path")
    fontPath = '/Users/stephennixon/type-repos/recursive/src/ufo/mono/Recursive Mono-Casual A.ufo'


# timestamp = datetime.now().strftime("%Y-%m-%d")

# textFileOutput = sys.argv[1].replace(".py", f"{timestamp}.txt")

suffixes = ["italic", "mono", "sans"]

# add glyphs that should be exluded based on their name's first letter
# also add glyphs like Nj that would be missed by this filter
italicsNotInSans = "c f r j lj Lj Nj s z".split()

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

rules = {}

def printWrite(line):
    rules.append(line)
    

font = OpenFont(fontPath, showInterface=False)

# TODO: add exclusion for g mono rules, e.g. gmacron

def makeRules():
    for suffix in suffixes:
        rules[suffix] = []

        for g in font:
            if '.' in g.name and g.name.split('.')[1] == suffix:
                # print(g)
                baseName = g.name.split('.')[0]
                rule = f'<sub name="{baseName}" with="{g.name}" />'
                rules[suffix].append(rule)

def makeSansItalicRules():
    rules['sans italic'] = []
    for g in font:
        if '.' in g.name and\
            g.name.split('.')[1] == 'italic' and\
            g.name.split('.')[0] not in italicsNotInSans and\
            g.name.split('.')[0][0] not in italicsNotInSans:

            baseName = g.name.split('.')[0]
            rule = f'<sub name="{baseName}" with="{g.name}" />'
            rules['sans italic'].append(rule)

def addSortedRules(rules):
    with open(newPath,"w+") as GSUBrules:
        for suffix in rules.keys():
            GSUBrules.write(f'\n\n'.ljust(80,'-') + '\n')
            GSUBrules.write(f'{suffix} '.ljust(80,'-') + '\n')

            for rule in sorted(rules[suffix]):
                GSUBrules.write(f'\n{rule}')


makeRules()
makeSansItalicRules()
addSortedRules(rules)

font.close()

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