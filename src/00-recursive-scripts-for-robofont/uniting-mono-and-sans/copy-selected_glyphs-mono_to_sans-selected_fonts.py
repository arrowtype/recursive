'''
    options:
        override? if not, append '.copy' suffix
        monoToSans? if not, will go sans to mono
    
    get list of fonts
    pair fonts by stylename (mono & sans linear slanted A, mono & sans casual B, etc)

    check: copy glyphs 'a, b, c.italic' from selected mono to sans fonts?
    
    for glyph in selection of current font
        go through fontPairs
            copy glyph from mono to sans
            mark glyph with color (orange?)
'''

from vanilla.dialogs import *
import os
from mojo.UI import AskString

# glyphsToCopy = CurrentFont().selection

print("hello rf")

files = getFile("Select UFOs to copy glyphs between",
                allowsMultipleSelection=True, fileTypes=["ufo"])

# fonts = {
#         "Casual A" = (monoFontCasualA, sansFontCasualA)
# }

fonts = {}

# TODO: strip 'Mono' or ''Sans from initial style name to keep mono&sans together in fonts dict

for path in files:
    f = OpenFont(path, showInterface=False)
    style = f.info.styleName
    if style not in fonts.keys():
        fonts[style] = []

    if fonts[style] == []:
        fonts[style].append(f)
    elif fonts[style] != []:
        # if 'Mono' already in list, put 'Sans' second
        if 'Mono' in fonts[style][0].info.styleName:
            fonts[style].append(f)
        # else put 'Mono' first
        else:
            fonts[style] = [f] + fonts[style]

print(fonts)

for style in fonts.keys():
    for f in fonts[style]:
        f.close()