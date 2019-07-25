
# get filename, check if "mono" or "sans"
from mojo.UI import OutputWindow
from vanilla.dialogs import *
import os
from mojo.UI import AskString

widthUnit = AskString('Width unit to check for (e.g. 600, 50, 10)')

files = getFile("Select files to check glyph widths in",
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

for i in badWidthGlyphs.keys():
    # check if there are problem-width glyphs
    if len(badWidthGlyphs[i].keys()) != 0:
        print(f"\n### {i}\n")
        print(f"| {'Glyph with bad width'.ljust(20)} | width |")
        print(f"| {'-'.ljust(20,'-')} | {'-'.ljust(4,'-')}: |")
        for j in badWidthGlyphs[i].keys():
            print(f"| {j.ljust(20)} | {str(badWidthGlyphs[i][j]).rjust(5)} |")

    print()

# if mono
# find any glyphs that are not multiples of 600
# add these glyphs to "badWidths"

# elif sans
# find any glyphs that are not multiples of 50
# add these glyphs to "badWidths"

# for name in badWidthGlyphs:
# print(name + " ️️️☠️ is bad width ☠️ \t \t" + f[name].width )
# mark glyph in (1,0,0,1) # bright red
