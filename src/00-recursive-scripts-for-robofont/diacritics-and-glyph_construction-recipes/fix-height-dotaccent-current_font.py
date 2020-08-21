"""
    Fix dotaccentcomb positioning.

    https://github.com/arrowtype/recursive/issues/390
"""

from vanilla.dialogs import *
from mojo.UI import OutputWindow

files = getFile("Select files to check for dotaccentcomb positioning", allowsMultipleSelection=True, fileTypes=["ufo"])


OutputWindow().show()
OutputWindow().clear()

# f = CurrentFont()

af = AllFonts()

fix = True

threshold = 20

for file in files:
    f = OpenFont(file, showInterface=False)
    print()
    print("----------------------------------------------------")
    print()
    print(f.info.styleName)
    print()
    print(f"\t yPos of 'dotaccentcomb' in composed glyphs, if not 0 or greater than {threshold}:")
    print()
    for g in f:
        if len(g.components) > 0:
            for c in g.components:
                if c.baseGlyph == 'dotaccentcomb' and g.name != 'dotaccentcomb.case':
                    if c.offset[1] != 0 and c.offset[1] <= threshold:
                        print("\t", g.name, "yPos: ", c.offset[1])

                        if fix:
                            c.offset = (c.offset[0], 0)
                            print("\t\t → yPos now ", c.offset[1])

    if fix:
        f.save()

    f.close()