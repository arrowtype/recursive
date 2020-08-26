"""
    Swap fraction & fraction.split, hopefully to make VF fractions work in more apps.

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

    # update names
    font['fraction'].name = "fraction.solid"
    font['fraction.split'].name = "fraction"
    font['slash.split'].name = "slash.solid"

    # TODO? update unicodes? Probably shouldn’t have to... but maybe

    font['fraction'].unicodes = (8260,)
    font['fraction.solid'].unicodes = ()


    # for fraction in fractions:
    #     for comp in font[fraction].components:
    #         if comp.baseGlyph == "fraction.split":
    #             comp.decompose()


    font.save()
    font.close()
