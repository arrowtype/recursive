# setting vertical metrics in Recursive

'''
    Sets underline & strikethrough metrics for all UFOs within a directory.

    Run of the command line:
        
    python src/01-shell-scripts-for-sources/metrics/set-underline_strikethrough-values.py src/ufo/mono
'''

import sys
import os
from fontParts.world import *

# values are shared between upright and slanted fonts, but tailored to Weight & Casual styles
underStrikeVals = {
    "Casual A": {
        "openTypeOS2StrikeoutSize": 45,
        "openTypeOS2StrikeoutPosition": 282,
        "postscriptUnderlineThickness": 45,
        "postscriptUnderlinePosition": -205,
    },
    "Casual B": {
        "openTypeOS2StrikeoutSize": 110,
        "openTypeOS2StrikeoutPosition": 320,
        "postscriptUnderlineThickness": 110,
        "postscriptUnderlinePosition": -175,
    },
    "Casual C": {
        "openTypeOS2StrikeoutSize": 80,
        "openTypeOS2StrikeoutPosition": 309,
        "postscriptUnderlineThickness": 150,
        "postscriptUnderlinePosition": -145,
    },
    "Linear A": {
        "openTypeOS2StrikeoutSize": 45,
        "openTypeOS2StrikeoutPosition": 284,
        "postscriptUnderlineThickness": 45,
        "postscriptUnderlinePosition": -205,
    },
    "Linear B": {
        "openTypeOS2StrikeoutSize": 110,
        "openTypeOS2StrikeoutPosition": 324,
        "postscriptUnderlineThickness": 110,
        "postscriptUnderlinePosition": -175,
    },
    "Linear C": {
        "openTypeOS2StrikeoutSize": 80,
        "openTypeOS2StrikeoutPosition": 314,
        "postscriptUnderlineThickness": 150,
        "postscriptUnderlinePosition": -145,
    },
}


try:
    if sys.argv[1]:
        dirToUpdate = sys.argv[1]
        print(f"Getting UFO paths in dir: {dirToUpdate}")
        subDirs = next(os.walk(dirToUpdate))[1]
        ufosToAdjust = [ path for path in subDirs if path.endswith(".ufo")]

        head = dirToUpdate

except IndexError:
    print("Please include path to directory containing UFOs")

print(ufosToAdjust)

for ufo in sorted(ufosToAdjust):
    ufoPath = f"{head}/{ufo}"

    font = OpenFont(ufoPath, showInterface=False)

    print('\n\n--------------------------------------------------------')
    fontName = f"{font.info.familyName} {font.info.styleName}"
    print(fontName)

    subFam = "Casual A"

    ## only useful if fontmake builds values into MVAR table
    # if "Casual A" in fontName or "Casual Light" in fontName:
    # 	subFam = "Casual A"
    # if "Casual B" in fontName or "Casual Light" in fontName:
    # 	subFam = "Casual B"
    # if "Casual C" in fontName or "Casual Light" in fontName:
    # 	subFam = "Casual C"
    # if "Linear A" in fontName or "Casual Light" in fontName:
    # 	subFam = "Linear A"
    # if "Linear B" in fontName or "Casual Light" in fontName:
    # 	subFam = "Linear B"
    # if "Linear C" in fontName or "Casual Light" in fontName:
    # 	subFam = "Linear C"

    print('\nStrikethrough ------------------------------------------')

    print("openTypeOS2StrikeoutSize was \t\t\t", str(font.info.openTypeOS2StrikeoutSize).rjust(6))
    print("openTypeOS2StrikeoutPosition was \t\t", str(font.info.openTypeOS2StrikeoutPosition).rjust(6))


    font.info.openTypeOS2StrikeoutSize = underStrikeVals[subFam]["openTypeOS2StrikeoutSize"]
    font.info.openTypeOS2StrikeoutPosition = underStrikeVals[subFam]["openTypeOS2StrikeoutPosition"]

    print("openTypeOS2StrikeoutSize is now \t\t", str(font.info.openTypeOS2StrikeoutSize).rjust(6))
    print("openTypeOS2StrikeoutPosition is now \t\t", str(font.info.openTypeOS2StrikeoutPosition).rjust(6))

    print('\nUnderline ----------------------------------------------')

    print("postscriptUnderlineThickness was \t\t", str(font.info.postscriptUnderlineThickness).rjust(6))
    print("postscriptUnderlinePosition was \t\t", str(font.info.postscriptUnderlinePosition).rjust(6))

    font.info.postscriptUnderlineThickness = underStrikeVals[subFam]["postscriptUnderlineThickness"]
    font.info.postscriptUnderlinePosition = underStrikeVals[subFam]["postscriptUnderlinePosition"]

    print("postscriptUnderlineThickness is now \t\t", str(font.info.postscriptUnderlineThickness).rjust(6))
    print("postscriptUnderlinePosition is now \t\t", str(font.info.postscriptUnderlinePosition).rjust(6))

    font.save()
    font.close()

