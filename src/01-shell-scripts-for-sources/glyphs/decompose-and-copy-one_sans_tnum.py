"""
    A script to decompose one.sans_tnum in each Mono source, then copy this (with tabular width) into related Sans source.
"""

import os
# from ufoLib2 import Font
from fontParts.world import OpenFont

sourcesPath = "src/ufo"
monoDir = os.path.join(sourcesPath, "mono")
sansDir = os.path.join(sourcesPath, "sans")

monoGlyphToCopyName = "one.sans_tnum"

for path in os.listdir(os.path.join(sourcesPath, "mono")):
    if ".ufo" in path:
        ufoPath = os.path.join(monoDir, path)
        print(ufoPath)

        cwd = os.getcwd()

        font = OpenFont(os.path.join(cwd, ufoPath))

        sansPath = ufoPath.replace("mono", "sans").replace("Mono", "Sans")

        sansFont = OpenFont(os.path.join(cwd, sansPath))

        sansFont[monoGlyphToCopyName].clear()

        glyphToCopy = font[monoGlyphToCopyName]
        glyphToCopy.decompose()

        if monoGlyphToCopyName not in sansFont:
            fontToSesansFontndTo.newGlyph(monoGlyphToCopyName)

        glyphToCopyTo = sansFont[monoGlyphToCopyName].getLayer("foreground")

        # get the point pen of the layer glyph
        pen = glyphToCopyTo.getPointPen()
        # draw the points of the imported glyph into the layered glyph
        glyphToCopy.drawPoints(pen)

        glyphToCopyTo.width = glyphToCopy.width

        glyphToCopyTo.markColor = (1, 1, 0, 0.5)

        font.save()
        sansFont.save()
