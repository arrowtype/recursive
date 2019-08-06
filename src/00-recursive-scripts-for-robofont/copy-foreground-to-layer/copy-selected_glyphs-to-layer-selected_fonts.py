from vanilla.dialogs import *
import os
from mojo.UI import AskString

newLayer = AskString('Layer to copy selected glyphs to, e.g. "overlap"')

files =  getFile("Select files to update", allowsMultipleSelection=True, fileTypes=["ufo"])

font = CurrentFont()

glyphsToCopyToNewLayer = font.selectedGlyphNames

for file in files:
    font = OpenFont(file)
    
    for name in glyphsToCopyToNewLayer:
        font[name].layers[0].copyLayerToLayer("foreground", newLayer)
        font[name].layers[-1].width = font[name].layers[0].width
        print(
            f"Glyphs copied to {newLayer}! Please save font to keep changes.")
