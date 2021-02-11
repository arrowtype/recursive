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
        dirToCheck = sys.argv[1]
        print(f"Getting UFO paths in dir: {dirToCheck}")
        subDirs = next(os.walk(dirToCheck))[1]
        ufosToAdjust = [ path for path in subDirs if path.endswith(".ufo")]

        head = dirToCheck

except IndexError:
    print("Please include path to directory containing UFOs")

minY, maxY = 0, 0

tallFont = ""
tallGlyph = ""
lowFont = ""
lowGlyph = ""

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
                lowFont = f"{font.info.familyName} {font.info.styleName}"
                lowGlyph = glyph.name

            if glyphMaxY > maxY:
                maxY = glyphMaxY
                tallFont = f"{font.info.familyName} {font.info.styleName}"
                tallGlyph = glyph.name


        except:
            pass

print()
print(f"maxY of UFOs in {head} is {maxY}")
print(f"Font with maxY is {tallFont}")
print(f"\t in {tallGlyph}")
print()

print()
print(f"minY of UFOs in {head} is {minY}")
print(f"Font with minY is {lowFont}")
print(f"\t in {lowGlyph}")
print()
