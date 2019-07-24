from vanilla.dialogs import *

inputFonts = getFile(
    "select UFOs", allowsMultipleSelection=True, fileTypes=["ufo"])


def addFeatureCode(f):
    f.features.text = feaText


for fontPath in inputFonts:
    f = OpenFont(fontPath, showInterface=False)

    for g in f:
        # add anchors to dictionary, like "g: casual A: top, bottom, left"

    f.save()
    f.close()
