'''
    for selected fonts, copy mono-specific glyphs to glyphs with ".mono" suffixes
'''

from vanilla.dialogs import *
import os
from mojo.UI import AskString


files = getFile("Select files to update",
                allowsMultipleSelection=True, fileTypes=["ufo"])


# get the current font
# f = CurrentFont()

# ask user for a suffix to add to duplicated glyphs
newGlyphSuffix = AskString(
    'Enter a new suffix for duplicate glyphs, e.g. "alt1"')

# get currently selected glyphs as a list
glyphsToCopy = AskString(
    'Space-separated list of glyphs to copy with suffix').split(" ")

# if the user cancels or inputs an empty string, cancel the script
if newGlyphSuffix == "" or glyphsToCopy == "":
    print("canceled")

# if the script is valid, keep going
else:
    for file in files:
        f = OpenFont(file)
        # loop through list of selected glyphs
        for glyph in glyphsToCopy:

            # get the base name of the glyph (before the period)
            baseNameOfGlyph = glyph.split('.')[0]

            # form the new glyph name
            newGlyphName = baseNameOfGlyph + "." + newGlyphSuffix

            # if the new glyph name already exists, don't overwrite it with the new one
            if newGlyphName in f.glyphOrder:
                print("sorry," + newGlyphName + " already exists.")

            # if the new glyph name doesn't already exist..
            if newGlyphName not in f.glyphOrder:

                # duplicate the selected glyph with the new glyph name
                f.insertGlyph(f[glyph], newGlyphName)

                # delete unicode value from new glyph (if you don't, it causes issues elsewhere)
                f[newGlyphName].unicode = None

                # let the user know it was made
                print(newGlyphName + " is created!")
