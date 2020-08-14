# setting vertical metrics in Recursive

'''
    Sets vertical metrics in UFOs within a directory.

    Run of the command line:
    
    python src/01-shell-scripts-for-sources/metrics/set-v_metrics.py src/ufo/mono <--save>
'''

import sys
import os
from fontParts.world import *

# new values to save in
newTopAscenderValue = 950
newDescenderValue = -250


# get font dir
try:
    if sys.argv[1]:
        print("Getting UFO paths")
        dirToUpdate = sys.argv[1]
        subDirs = next(os.walk(dirToUpdate))[1]
        ufosToAdjust = [ path for path in subDirs if path.endswith(".ufo")]

        head = dirToUpdate

except IndexError:
    print("Please include directory containing UFOs")

# check whether to save new results
save = False
try:
    if sys.argv[2] == "-s" or sys.argv[2] == "--save" :
        print("Saving new vertical metrics to fonts")
        save = True

except IndexError:
    print("Dry run. Add second arg of --save or -s to save new vertical metrics.")

# run program
for ufo in sorted(ufosToAdjust):
    ufoPath = f"{head}/{ufo}"

    font = OpenFont(ufoPath, showInterface=False)

    print(font.info.styleName)

    print('--------------------------------------------------------')
    print(font.info.styleName)

    # ascenders

    print("openTypeOS2TypoAscender is \t\t", font.info.openTypeOS2TypoAscender)
    print("openTypeHheaAscender is \t\t", font.info.openTypeHheaAscender)

    font.info.openTypeOS2TypoAscender = newTopAscenderValue
    font.info.openTypeHheaAscender = newTopAscenderValue

    print("openTypeOS2TypoAscender is now \t\t", font.info.openTypeOS2TypoAscender)
    print("openTypeHheaAscender is now \t\t", font.info.openTypeHheaAscender)
    
    # descenders

    print("openTypeOS2TypoDescender is \t\t", font.info.openTypeOS2TypoDescender)
    print("openTypeHheaDescender is \t\t", font.info.openTypeHheaDescender)

    font.info.openTypeOS2TypoDescender = newDescenderValue
    font.info.openTypeHheaDescender = newDescenderValue

    print("openTypeOS2TypoDescender is now \t\t", font.info.openTypeOS2TypoDescender)
    print("openTypeHheaDescender is now \t\t", font.info.openTypeHheaDescender)

    if save:
        font.save()
    font.close()
