'''
    For selected fonts, make a space-separated list of suffixed glyphs into defaults, 
    replacing the suffixed versions to with copies
'''

from vanilla.dialogs import *
import os
from mojo.UI import AskString
import datetime


files = getFile("Select files to update",
                allowsMultipleSelection=True, fileTypes=["ufo"])


# get currently selected glyphs as a list
glyphsToMakeDefault = AskString(
    'Space-separated list of glyphs to make default').split(" ")

# if the user cancels or inputs an empty string, cancel the script
if glyphsToMakeDefault == "":
    print("canceled")

# if the script is valid, keep going
else:
    for file in files:
        f = OpenFont(file)
        for altGlyph in glyphsToMakeDefault:

            splitAltGlyphName = f[altGlyph].name.split('.')

            # check that selected glyph
            if len(splitAltGlyphName) == 2:
                # get unicode of default glyph
                defaultUnicodes = f[splitAltGlyphName[0]].unicodes

                # get default glyph (with no suffix) and make duplicate of it with current timestamp
                now = datetime.datetime.now()
                dupedDefaultGlyphName = splitAltGlyphName[0] + \
                    "." + now.strftime("%y%m%d-%H_%M")

                # hardto read
                # dupedDefaultGlyphName = splitAltGlyphName[0] + "." + "replaced_with_" + splitAltGlyphName[1]

                # if the new glyph name already exists, don't overwrite it with the new one
                if dupedDefaultGlyphName in f.keys():
                    print("sorry," + dupedDefaultGlyphName + " already exists.")

                # if the new glyph name doesn't already exist..
                if dupedDefaultGlyphName not in f.keys():

                    # duplicate the selected glyph with the new glyph name
                    f.insertGlyph(f[splitAltGlyphName[0]],
                                  dupedDefaultGlyphName)
                    f[dupedDefaultGlyphName].unicode = None

                    # get suffixed glyph and use it to replace the former default

                    f.insertGlyph(f[altGlyph], splitAltGlyphName[0])

                    # attach stored default unicodes to newly-created default glyph
                    f[splitAltGlyphName[0]].unicodes = defaultUnicodes

                    # now that it has been made the default, delete the suffixed glyph
                    if altGlyph in f.keys():
                        f.removeGlyph(altGlyph)

                    # the new default is at the end, so this will re-apply a "smart sort" to the font
                    newGlyphOrder = f.naked().unicodeData.sortGlyphNames(f.templateGlyphOrder, sortDescriptors=[
                        dict(type="cannedDesign", ascending=True, allowPseudoUnicode=True)])
                    f.templateGlyphOrder = newGlyphOrder
            else:
                print("sorry, '" + altGlyph +
                      "' is already a default (non-suffixed) glyph")
