"""
    Decomposing new code ligatures to prevent spacing/positioning weirdness from components in Sans sources.

    Dec 9, 2020.
"""

ligs = "less_less_hyphen.code less_less_asciitilde.code".split()

for name in ligs:
    print(name)

from vanilla.dialogs import *

inputFonts = getFile("select masters to add non-exporting glyphs to", allowsMultipleSelection=True, fileTypes=["ufo"])
        
for fontPath in inputFonts:
    f = OpenFont(fontPath, showInterface=False)

    for name in ligs:
        f[name].decompose()

    f.save()
    f.close()