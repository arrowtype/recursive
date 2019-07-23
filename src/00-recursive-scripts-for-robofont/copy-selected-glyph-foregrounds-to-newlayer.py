from vanilla.dialogs import *
import os
from mojo.UI import AskString

files =  getFile("Select files to update", allowsMultipleSelection=True, fileTypes=["ufo"])

newLayer = AskString('Layer to copy all existing glyphs to, e.g. "overlap"')

f = CurrentFont()

glyphsToCopyToNewLayer = f.selectedGlyphNames

for file in files:
    font = OpenFont(file)
    for name in glyphsToCopyToNewLayer:
        font[name].layers[0].copyLayerToLayer("foreground", newLayer)
        print(f"Glyphs copied to {newLayer}! Please save font to keep changes.")

