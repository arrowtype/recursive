from vanilla.dialogs import *
import os
from mojo.UI import AskString

f = CurrentFont()

# help(f)

f.__setitem__("a.test",f["a"])

glyphsToCopy = f.selectedGlyphNames

files =  getFile("Select files to update", allowsMultipleSelection=True, fileTypes=["ufo"])

# get selection of glyphs

# ask for selection of fonts


for file in files:
    otherFont = OpenFont(file)
    print("----------------------------------------")
    print(otherFont)
    for glyphName in glyphsToCopy:
        # if glyph not in font, add to font
        if glyphName not in otherFont.glyphOrder:
            # adds glyph top foreground
            otherFont.__setitem__(glyphName,f[glyphName])
            otherFont[glyphName].layers[0].copyLayerToLayer("foreground", "background")
            otherFont[glyphName].layers[0].__delitem__(glyphName)
            print(f"\t {glyphName} is created!")

    font.save()
    font.close()