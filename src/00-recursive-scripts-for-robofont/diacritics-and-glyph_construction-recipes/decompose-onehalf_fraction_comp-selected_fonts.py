'''
    Prebuild fractions in Recursive have decomposed fraction bars (probably due to the Mono/Sans variations, but I don’t 100% remember).

    I’ve rebuild the onehalf and onehalf.afrc fractions in Sans sources because they were messed up. This will decompose the fraction bar.

'''
from vanilla.dialogs import *
from glyphConstruction import ParseGlyphConstructionListFromString, GlyphConstructionBuilder

files = getFile("Select files to build glyphs in", allowsMultipleSelection=True, fileTypes=["ufo"])


fractionsToFix = "onehalf onehalf.afrc".split(" ")

for filepath in files:
    font = OpenFont(filepath, showInterface=False)

    for name in fractionsToFix:
        for comp in font[name].components:
            if comp.baseGlyph == "fraction":
                comp.decompose()

    font.save()
