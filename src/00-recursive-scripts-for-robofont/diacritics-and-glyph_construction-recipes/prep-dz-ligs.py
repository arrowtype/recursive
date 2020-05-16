"""
    A single-purpose script to handle DZ ligatures generated from DZcaron ligatures

    See https://github.com/arrowtype/recursive/issues/343
"""

from vanilla.dialogs import *

glyphsToFix = "DZ Dz dz dz.italic".split(" ")


# Open all fonts
files = getFile("Select files to build glyphs in", allowsMultipleSelection=True, fileTypes=["ufo"])

# Set to False to open fonts with RoboFont UI (e.g. to visually check changes before saving)
skipInterface = True

for fontFile in files:

    if skipInterface:
        font = OpenFont(fontFile, showInterface=False)
    else:
        font = OpenFont(fontFile, showInterface=True)

    for glyphName in glyphsToFix:

        g = font[glyphName]

        g.decompose()

        # delete caron contour
        for contour in g.contours:
            if len(contour) == len(font["circumflexcomb"].contours[0]):
                g.removeContour(contour)

    if skipInterface:
        font.save()
        font.close()