"""
    A script to decompose one.sans_tnum in each Mono source, then copy this (with tabular width) into related Sans source.
"""

import os
from ufoLib2 import Font

sourcesPath = "src/ufo"

monoGlyphToCopyName = "one.sans_tnum"

for path in os.listdir(os.path.join(sourcesPath, "mono")):
    if ".ufo" in path:
        ufoPath = os.path.join(sourcesPath, path)
        print(ufoPath)

        font = Font(ufoPath)

        sansPath = ufoPath.replace("mono", "sans").replace("Mono", "Sans")

        sansFont = Font(sansPath)

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

        glyphToCopy.markColor(1,1,0,0.5)
