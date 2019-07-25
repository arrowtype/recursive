# import AskString from robofont's mojo UI library
from mojo.UI import AskString

f = CurrentFont()

newLayer = AskString('Layer to copy all existing glyphs to, e.g. "overlap"')

for glyph in f:
    glyph.layers[0].copyLayerToLayer("foreground", newLayer)