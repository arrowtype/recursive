from vanilla.dialogs import *
from mojo.UI import AskString

newLayer = AskString('Layer to copy all existing glyphs to, e.g. "overlap"')

f = CurrentFont()

glyphsToCopyToNewLayer = f.selectedGlyphNames

for name in glyphsToCopyToNewLayer:
    for font in AllFonts():
        font[name].layers[0].copyLayerToLayer("foreground", newLayer)
        print(f"Glyphs copied to {newLayer}! Please save font to keep changes.")

