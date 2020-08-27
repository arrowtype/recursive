"""
    This is a script to set all superior & inferior glyphs to 400, then center them.

    Meant specifically for Recursive Sans.
"""

from vanilla.dialogs import *
from mojo.UI import OutputWindow


OutputWindow().show()
OutputWindow().clear()

# settings below --------------------------------

newWidth = 0 # sans fraction
# newWidth = 400 # sans
# newWidth = 600 # mono
substringsToFind = "superior inferior"
widthExpected = 400
# substringsToFind = "fraction"


# settings above --------------------------------

files = getFile("Select files to check", allowsMultipleSelection=True, fileTypes=["ufo"])


for file in files:
    font = OpenFont(file, showInterface=False)

    # tinyFigs = [g.name for g in font if any(substring in g.name for substring in substringsToFind.split(" "))]

    tinyFigs = "uni00B9 uni00B2 uni00B3 uni2070 uni2074 uni2075 uni2076 uni2077 uni2078 uni2079 uni2080 uni2081 uni2082 uni2083 uni2084 uni2085 uni2086 uni2087 uni2088 uni2089".split()

    print()
    print("--------------------------------------------------------------")
    print()
    print(font.info.familyName, font.info.styleName)
    print()
    for name in tinyFigs:
        try:
            if font[name].width != widthExpected:
                print(name, f[name].width)
    print()

    # font.save()
    font.close()
