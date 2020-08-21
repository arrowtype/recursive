"""
    This is a script to set all superior & inferior glyphs to 400, then center them.

    Meant specifically for Recursive Sans.
"""

from vanilla.dialogs import *

# settings below --------------------------------

newWidth = 0
substringsToFind = "fraction.split"

# settings above --------------------------------

files = getFile("Select files to build glyphs in", allowsMultipleSelection=True, fileTypes=["ufo"])

for file in files:
    # font = OpenFont(file, showInterface=False)
    f = OpenFont(file, showInterface=True)

    tinyFigs = [g.name for g in f if any(substring in g.name for substring in substringsToFind.split(" "))]

    for gname in tinyFigs:
        g = f[gname]
        g.width = newWidth

        # center glyph
        totalMargin = g.leftMargin + g.rightMargin
        g.leftMargin = totalMargin / 2
        g.rightMargin = totalMargin / 2

        # enforce width
        g.width = newWidth

    print()
    print("--------------------------------------------------------------")
    print()
    print(f.info.familyName, f.info.styleName)
    print()
    print(f"Set the following to {newWidth}:")
    print(tinyFigs)

    # font.save()
    # font.close()
