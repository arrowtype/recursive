"""
    It’s possible that double-dot suffixes are breaking the build (Issue #486).

    This script will find such glyphs and change the second period to an underscore.

    six.ss01.pnum nine.ss01.pnum zero.slash.pnum zero.dotted.pnum zero.sans.pnum one.sans.tnum
"""

import os
from fontParts.world import OpenFont

monoDir = "src/ufo/mono"
sansDir = "src/ufo/sans"

# get source UFO paths
ufoPaths = [os.path.join(monoDir, path) for path in os.listdir(monoDir) if ".ufo" in path] + [os.path.join(sansDir, path) for path in os.listdir(sansDir) if ".ufo" in path]

for fontPath in ufoPaths:
    print(fontPath)
    f = OpenFont(fontPath, showInterface=False)

    for name in f.keys():
        # if more than two periods are in the glyph name...
        if len([c for c in name if c is "."]) > 2:
            # this is unexpected. Say so:
            raise ValueError(f'Glyph /{name} contains more than 2 periods in its name – extend the script to handle this.')

        # if more than one period is in the glyph name...
        if len([c for c in name if c is "."]) > 1:
            # rename with an underscore in place of the second period
            f[name].name = f'{name.split(".")[0]}.{name.split(".")[1]}_{name.split(".")[2]}'

    f.save(fontPath)