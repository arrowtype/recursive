"""
    Decompose fraction bar in fractions, useful for Recursive Sans
"""

from vanilla.dialogs import *

# settings below --------------------------------

fractions = "onequarter threequarters onethird twothirds oneeighth threeeighths fiveeighths seveneighths onequarter.afrc threequarters.afrc onethird.afrc twothirds.afrc oneeighth.afrc threeeighths.afrc fiveeighths.afrc seveneighths.afrc".split()

# settings above --------------------------------

files = getFile("Select files to modify", allowsMultipleSelection=True, fileTypes=["ufo"])

for file in files:
    font = OpenFont(file, showInterface=False)
    # font = OpenFont(file, showInterface=True)

    for fraction in fractions:
        for comp in font[fraction].components:
            if comp.baseGlyph == "fraction.split":
                comp.decompose()


    font.save()
    font.close()
