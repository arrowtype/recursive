# setting vertical metrics in Recursive

'''
    Sets vertical metrics in UFOs within a directory.

    Run of the command line:
    
    python src/01-shell-scripts-for-sources/metrics/set-v_metrics.py src/masters/mono
'''

import sys
import os
from fontParts.world import *

newTopAscenderValue = 950

try:
    if sys.argv[1]:
        print("Copying from UFO to UFOs in another Directory")
        dirToUpdate = sys.argv[1]
        subDirs = next(os.walk(dirToUpdate))[1]
        ufosToAdjust = [ path for path in subDirs if path.endswith(".ufo")]

        head = dirToUpdate

except IndexError:
    print("Please include directory containing UFOs")

print(ufosToAdjust)

for ufo in sorted(ufosToAdjust):
    ufoPath = f"{head}/{ufo}"

    font = OpenFont(ufoPath, showInterface=False)

    print(font.info.styleName)

    print('--------------------------------------------------------')
    print(font.info.styleName)

    print("openTypeOS2TypoAscender is \t\t", font.info.openTypeOS2TypoAscender)
    print("openTypeHheaAscender is \t\t", font.info.openTypeHheaAscender)

    font.info.openTypeOS2TypoAscender = newTopAscenderValue
    font.info.openTypeHheaAscender = newTopAscenderValue

    print("openTypeOS2TypoAscender is now \t\t", font.info.openTypeOS2TypoAscender)
    print("openTypeHheaAscender is now \t\t", font.info.openTypeHheaAscender)

    font.save()
    font.close()
