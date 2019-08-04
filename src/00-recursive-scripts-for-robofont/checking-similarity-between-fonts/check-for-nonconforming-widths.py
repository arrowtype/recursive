'''
    Lets you check that glyphs maintain a similar width unit between all selected UFOs.
    Assumes you want each glyph to keep the same width between all selected UFOs.
'''


# get filename, check if "mono" or "sans"
from mojo.UI import OutputWindow
from vanilla.dialogs import *
import os
from mojo.UI import AskString

widthUnit = AskString('Width unit to check for (e.g. 600, 50, 10)')

duplexing = AskString('Check that widths are duplexed between all files? (y/n)')

files = getFile(f"Select files to check glyph widths for units of {widthUnit}",
                allowsMultipleSelection=True, fileTypes=["ufo"])

badWidthGlyphs = {}

glyphWidthDict = {}

for file in files:
    font = OpenFont(file)
    fontName = f"{font.info.familyName} {font.info.styleName}"
    badWidthGlyphs[fontName] = {}
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

OutputWindow().show()

# check if there are problem-width glyphs, print to markdown-ready tables
for i in badWidthGlyphs.keys():
    if len(badWidthGlyphs[i].keys()) != 0:
        print(f"\n### {i} – glyphs not in units of {widthUnit}\n")
        print(f"| {'**Glyph**'.ljust(20)} | **width** |")
        print(f"| {'-'.ljust(20,'-')} | {'-'.ljust(8,'-')}: |")
        for j in badWidthGlyphs[i].keys():
            print(f"| {j.ljust(20)} | {str(badWidthGlyphs[i][j]).rjust(9)} |")

        print()


# table headers for master names: LA LAi LB LBi LC LCi CA CAi CB CBi CC CCi
# take first initials of style name

if duplexing.lower() == "y":
    nameLength = 15  # max(map(len, glyphWidthDict))
    print(nameLength)
    for i in glyphWidthDict.keys():

        if len(set(glyphWidthDict[i])) > 1:
            print(i.ljust(nameLength), end=" ")
            for j in glyphWidthDict[i]:
                print(j, end=" ")
            print("")
    #     if len(glyphWidthDict[i].keys()) != 0:
    #         print(f"\n### {i} – glyphs with different widths between masters\n")


# TODO: check for widths that different in a glyph, between masters
    # note... this script might be already written

# TODO: write checks for kerning units (in this or a separate script)
