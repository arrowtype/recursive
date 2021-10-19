"""
    Add a Unicode value for a given glyph name to UFOs in the source dirs.
"""

import os
from fontParts.world import OpenFont
import ufonormalizer

monoDir = "src/ufo/mono"
sansDir = "src/ufo/sans"

# get source UFO paths
ufoPaths = [os.path.join(monoDir, path) for path in os.listdir(monoDir) if ".ufo" in path] + [os.path.join(sansDir, path) for path in os.listdir(sansDir) if ".ufo" in path]

# setting as integers in tuple format, because I know this already
unicodesToSet = {
    "beta": (946,),
    "minus.superior": (8315,),
}

for fontPath in ufoPaths:
    print(fontPath)
    f = OpenFont(fontPath, showInterface=False)

    for name, unicodes in unicodesToSet.items():

        f[name].unicodes = unicodes

    f.save(fontPath)

    
    ufonormalizer.normalizeUFO(fontPath, writeModTimes=False)