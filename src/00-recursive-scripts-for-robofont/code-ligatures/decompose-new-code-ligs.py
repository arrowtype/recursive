"""
    Decomposing new code ligatures to prevent spacing/positioning weirdness from components in Sans sources.

    Dec 9, 2020.
"""

ligs = "less_greater.code less_equal_greater.code less_less_equal.code greater_greater_equal.code bar_equal.code exclam_asciitilde.code equal_asciitilde.code bar_greater.code slash_equal.code less_bar_greater.code less_bar.code less_asterisk_greater.code less_asterisk.code less_dollar_greater.code less_plus_greater.code equal_less_less.code hyphen_less.code greater_hyphen.code hyphen_less_less.code greater_greater_hyphen.code".split()

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