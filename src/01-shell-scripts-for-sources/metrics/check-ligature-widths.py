"""
    Check ligature widths to find where they don’t match added width of characters included.
    
    https://github.com/arrowtype/recursive/issues/431
"""

import sys
import os
from fontParts.world import *

ligaturesToCheck = "f_f fi fl f_f_i f_f_l".split()

# make list of UFOs in directory
try:
    if sys.argv[1]:
        dirToCheck = sys.argv[1]
        print(f"Getting UFO paths in dir: {dirToCheck}")
        subDirs = next(os.walk(dirToCheck))[1]
        ufosToCheck = [path for path in subDirs if path.endswith(".ufo")]
        head = dirToCheck

except IndexError:
    print("Please include path to directory containing UFOs")

# compare lig widths vs component characters
def compareWidths(font, lig, subChars):
    subCharsWidth = sum([font[char].width for char in subChars])
    if font[lig].width == subCharsWidth:
        pass
    else:
        print(f"  - {lig} is {font[lig].width}, should be {subCharsWidth}")

# go through UFOs to check lig widths
for ufo in sorted(ufosToCheck):
    ufoPath = f"{head}/{ufo}"

    font = OpenFont(ufoPath, showInterface=False)

    print(f"\n- {font.info.familyName} {font.info.styleName}")

    for lig in ligaturesToCheck:
        if lig in font.keys():
            if lig in ["fi","fl"]:
                compareWidths(font,lig,["f","i"])
            else:
                subChars = [subChar for subChar in lig.split("_")]
                compareWidths(font, lig, subChars)

