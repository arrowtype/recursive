# setting vertical metrics in Recursive
import sys
from fontParts.world import *

try:
    if sys.argv[1]:
        print("Copying from UFO to UFOs in another Directory")
        dirToCopyTo = sys.argv[1]
        ufosToAdjust = next(os.walk(dirToCopyTo))[1]

        head = dirToCopyTo
except IndexError:
    print("Please include directory containing UFOs")

for ufo in sorted(ufosToAdjust):
    ufoPath = f"{head}/{ufo}"

    font = OpenFont(fontPath, showInterface=False)

    print(font.info.styleName)

    # f = CurrentFont()

    newTopAscenderValue = 950

    print('--------------------------------------------------------')
    print(font.info.styleName)

    print(font.info.openTypeOS2TypoAscender)
    print(font.info.openTypeHheaAscender)

    font.info.openTypeOS2TypoAscender = newTopAscenderValue
    font.info.openTypeHheaAscender = newTopAscenderValue


    print(font.info.openTypeOS2TypoAscender)
    print(font.info.openTypeHheaAscender)
