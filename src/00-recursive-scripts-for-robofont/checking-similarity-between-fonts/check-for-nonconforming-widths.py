'''
    Lets you check that glyphs maintain a similar width unit between all selected UFOs.
    Assumes you want each glyph to keep the same width between all selected UFOs.
'''


# get filename, check if "mono" or "sans"
from mojo.UI import OutputWindow
from vanilla.dialogs import *
import os
from mojo.UI import AskString
import pprint

debug = False # will print full dictionaries

widthUnit = AskString('Width unit to check for (e.g. 600, 50, 10)')

duplexing = AskString('Check that widths are duplexed between all files? (y/n)')

files = getFile(f"Select files to check glyph widths for units of {widthUnit}",
                allowsMultipleSelection=True, fileTypes=["ufo"])

fonts = []

OutputWindow().show()
OutputWindow().clear()

print("\nSUPERPLEXING REPORT: GLYPH WIDTH SIMILIARITY\n\n")

fonts=[]
badWidthGlyphs = {}
glyphWidthDict = {}

for file in files:
    font = OpenFont(file, showInterface=False)
    fontName = f"{font.info.styleName}"
    badWidthGlyphs[fontName] = {}

    fonts.append(fontName)

    for glyph in font:
        if glyph.width % int(widthUnit) != 0:
            badWidthGlyphs[fontName][glyph.name] = glyph.width

    if duplexing.lower() == "y":
        for glyph in font:
            if glyph.name not in glyphWidthDict:
                glyphWidthDict[glyph.name] = []
            if glyph.name in glyphWidthDict:
                glyphWidthDict[glyph.name].append(str(glyph.width))

    font.close()

print("Checking fonts:")

for fontName in fonts:
    print("• ", fontName)

print("")

# check if there are problem-width glyphs, print to markdown-ready tables
for i in sorted(badWidthGlyphs.keys()):
    if len(badWidthGlyphs[i].keys()) != 0:
        print(f"\n### {i} – glyphs not in units of {widthUnit}\n")
        print(f"| {'**Glyph**'.ljust(20)} | **width** |")
        print(f"| {'-'.ljust(20,'-')} | {'-'.ljust(8,'-')}: |")
        for j in sorted(badWidthGlyphs[i].keys()):
            print(f"| {j.ljust(20)} | {str(badWidthGlyphs[i][j]).rjust(9)} |")

        print()


if debug:
    pp = pprint.PrettyPrinter(indent=2, width=200)
    print("bad width glyphs")
    pp.pprint(badWidthGlyphs)
    print("glyph widths")
    pp.pprint(glyphWidthDict)

fontInitials = []

for fontName in sorted(fonts):
    fontWords = fontName.split()
    letters = [word[0] for word in fontWords]
    
    # make "s" lowercase for "Slanted"
    if letters[-1] is "S":
        letters[-1] = "s"

    # remove "M" for "Mono" or "S" for "Sans"
    if letters[0] is "M" or letters[0] is "S":
        letters.pop(0)
    fontInitials.append("".join(letters))

# table headers for master names: LA LAi LB LBi LC LCi CA CAi CB CBi CC CCi
# take first initials of style name
nameLength = 20  # max(map(len, glyphWidthDict))
abbrevLength = 5



print("\nglyph".ljust(nameLength), end="")

## TODO: probably, flip the axis here and just print a clearer list with each glyph.
# for name in fontInitials:
#     print(name.rjust(abbrevLength), end="")

print("\n--------------------------------------------------------------------------------------")

# glyphsToCheck = "A B C D E F G H I J K L M N O P R S T U V W X Y Z a b c d e f g h k l m n o p q r s t u v w x y z germandbls at ampersand a.italic c.italic d.italic e.italic f.italic g.italic h.italic k.italic l.italic m.italic n.italic r.italic s.italic u.italic v.italic w.italic x.italic y.italic z.italic dotlessi.italic dotlessj.italic l.sans one.sans f.mono i.mono l.mono r.mono".split(" ")

# for glyphName in sorted(glyphWidthDict.keys()):
#     if glyphName in glyphsToCheck:
#         if set(glyphWidthDict[glyphName].keys()) > 1:

if duplexing.lower() == "y":
    for glyphName in sorted(glyphWidthDict.keys()):
        # if glyphName in glyphsToCheck and len(set(glyphWidthDict[glyphName])) > 1:
        if len(set(glyphWidthDict[glyphName])) > 1:
            print(glyphName.ljust(nameLength), end="")
            for glyphWidth in glyphWidthDict[glyphName]:
                print(glyphWidth.rjust(abbrevLength), end="")
            print("\n")
    #     if len(glyphWidthDict[i].keys()) != 0:
    #         print(f"\n### {i} – glyphs with different widths between masters\n")


# TODO: check for widths that different in a glyph, between masters
    # note... this script might be already written

# TODO: write checks for kerning units (in this or a separate script)