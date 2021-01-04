'''
    Finds min and max Y coordinates in all UFOs within a directory.

    Run of the command line:
        
    python src/01-shell-scripts-for-sources/metrics/find-min_max_y_vals.py src/ufo/mono
'''

import sys
import os
from fontParts.world import *

try:
    if sys.argv[1]:
        dirToUpdate = sys.argv[1]
        print(f"Getting UFO paths in dir: {dirToUpdate}")
        subDirs = next(os.walk(dirToUpdate))[1]
        ufosToAdjust = [ path for path in subDirs if path.endswith(".ufo")]

        head = dirToUpdate

except IndexError:
    print("Please include path to directory containing UFOs")

minY, maxY = 0, 0

print("Finding group min & max Y")

for ufo in sorted(ufosToAdjust):
    ufoPath = f"{head}/{ufo}"

    font = OpenFont(ufoPath, showInterface=False)

    print(f"Checking {font.info.familyName} {font.info.styleName}...")

    # BaseGlyph.bounds - The bounds of the glyph in the form (x minimum, y minimum, x maximum, y maximum)

    for glyph in font:
        try:
            glyphMinY, glyphMaxY = glyph.bounds[1], glyph.bounds[3]

            if glyphMinY < minY:
                minY = glyphMinY

            if glyphMaxY > maxY:
                maxY = glyphMaxY
        except:
            pass

print()
print(f"Group minY is {minY}")
print(f"Group maxY is {maxY}")
print()