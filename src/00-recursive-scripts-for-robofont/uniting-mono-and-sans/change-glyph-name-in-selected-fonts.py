'''
    For selected fonts, change name of single glyph
'''

from vanilla.dialogs import *
import os
from mojo.UI import AskString


files = getFile("Select files to update",
                allowsMultipleSelection=True, fileTypes=["ufo"])

# get currently selected glyphs as a list
oldName = AskString('name of glyph to update (only one)').split(" ")

newName = AskString('new name for glyph').split(" ")


# if the user cancels or inputs an empty string, cancel the script
if len(oldName) > 1 or len(newName) > 1:
    print("Error: enter only one glyph and one new name")
    print("\t oldName: ", oldName)
    print("\t newName: ", newName)

# if the script is valid, keep going
else:
    for file in files:
        font = OpenFont(file, showInterface=False)

        if oldName[0] in font.keys():
            font.renameGlyph(oldName[0], newName[0], renameComponents=True,
                            renameGroups=True, renameKerning=True, renameGlyphOrder=True)

            print(f"{oldName[0]} changed to {newName[0]} in {font.info.styleName}")
        else:
            print(f"{oldName[0]} not in {font.info.styleName}")

        font.save()
        font.close()
