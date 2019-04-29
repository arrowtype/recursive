from vanilla.dialogs import *
import os
from mojo.UI import AskString

files =  getFile("Select files to update", allowsMultipleSelection=True, fileTypes=["ufo"])

newLayer = AskString('Layer to copy all existing glyphs to, e.g. "overlap"')

for file in files:
    font = OpenFont(file)
    for glyph in font:
        glyph.layers[0].copyLayerToLayer("foreground", newLayer)
    font.close()