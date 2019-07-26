
# get filename, check if "mono" or "sans"
from mojo.UI import OutputWindow
from vanilla.dialogs import *
import os
from mojo.UI import AskString

widthUnit = AskString('Width unit to check for (e.g. 600, 50, 10)')

files = getFile(f"Select files to check glyph widths for units of {widthUnit}",
                allowsMultipleSelection=True, fileTypes=["ufo"])

badWidthGlyphs = {}

for file in files:
    font = OpenFont(file)
    fontName = f"{font.info.familyName} {font.info.styleName}"
    badWidthGlyphs[fontName] = {}
    for glyph in font:
        if glyph.width % int(widthUnit) != 0:
            badWidthGlyphs[fontName][glyph.name] = glyph.width

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


# TODO: check for widths that different in a glyph, between masters
    # note... this script might be already written
