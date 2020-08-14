# A script to quickly add _top anchor ringbelowcomb.


from vanilla.dialogs import *
from mojo.UI import OutputWindow


OutputWindow().show()
OutputWindow().clear()
files = getFile("Select files to build glyphs in", allowsMultipleSelection=True, fileTypes=["ufo"])


def addMissingAnchors(font):
    print("\n\n-----------------------------------------------")
    print(font.info.styleName)

    g = font["ringbelowcomb"]


    g.removeAnchor(g.anchors[0])

    g.appendAnchor("_bottom", (0, 0))

# find suffixes needed for recipeGlyphs
for file in files:
    font = OpenFont(file, showInterface=False)

    addMissingAnchors(font)

    font.save()

    font.close()
