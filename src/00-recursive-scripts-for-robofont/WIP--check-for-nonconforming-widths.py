# get filename, check if "mono" or "sans"

from vanilla.dialogs import *
import os
from mojo.UI import AskString

files = getFile("Select files to update",
                allowsMultipleSelection=True, fileTypes=["ufo"])

widthUnit = AskString('Width unit to check for (e.g. 600, 50, 10)')

badWidthGlyphs = {}

for font in files:
    font = OpenFont(file)
    fontName = font.info.familyName + font.info.styleName
    for glyph in font:
        if glyph.width % widthUnit != 0:
            badWidthGlyphs[fontName][glyph.name] = glyph.width

    font.close()

OutputWindow().show()
print(badWidthGlyph)

# if mono
# find any glyphs that are not multiples of 600
# add these glyphs to "badWidths"

# elif sans
# find any glyphs that are not multiples of 50
# add these glyphs to "badWidths"

# for name in badWidthGlyphs:
# print(name + " ️️️☠️ is bad width ☠️ \t \t" + f[name].width )
# mark glyph in (1,0,0,1) # bright red
