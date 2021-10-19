"""
    Mark specific glyphs as exporting glyphs.
"""

import os
from fontParts.world import OpenFont
import ufonormalizer

monoDir = "src/ufo/mono"
sansDir = "src/ufo/sans"

# get source UFO paths
ufoPaths = [os.path.join(monoDir, path) for path in os.listdir(monoDir) if ".ufo" in path] + [os.path.join(sansDir, path) for path in os.listdir(sansDir) if ".ufo" in path]

# setting as integers in tuple format, because I know this already
glyphsToExport = "fi fl".split(" ")

for fontPath in ufoPaths:
    print(fontPath)
    f = OpenFont(fontPath, showInterface=False)

    for name in glyphsToExport:
        if name in f.lib["public.skipExportGlyphs"]:
            f.lib["public.skipExportGlyphs"].remove(name)

    f.save(fontPath)

    ufonormalizer.normalizeUFO(fontPath, writeModTimes=False)
