"""
    A script to remove a list of glyphs from selected fonts
"""

import os
from mojo.UI import AskString
from vanilla.dialogs import *

# copy-paste to fill this list with whatever glyphs fontMake flags as not being interpolatable
# glyphsToDelete = ['LISTOFGLYPHSHERE']

glyphsToRemove = AskString(
    'Input glyphnames to remove, then select UFOs').replace("'", "").replace(",", "").split(" ")

# help(CurrentFont().removeGlyph())

instruction = f"select masters to remove {glyphsToRemove} from"

inputFonts = getFile(
    instruction, allowsMultipleSelection=True, fileTypes=["ufo"])

# copy space-separated glyph names here
# glyphsToRemove = list(f.selectedGlyphNames)

def removeGlyphs(glyphsToRemove,f):

    # LAYERS --------------------------------------------------

    for layerName in f.layerOrder:
        layer = f.getLayer(layerName)
        for glyphToRemove in glyphsToRemove:
            if glyphToRemove in layer:
                del layer[glyphToRemove]
            # else:
            #     print("%s does not contain a glyph named '%s'" %
            #           (layerName, glyphToRemove))


    # GLYPH ORDER ---------------------------------------------

    glyphOrder = f.glyphOrder

    for glyphName in glyphsToRemove:
        if glyphName in glyphOrder:
            glyphOrder.remove(glyphName)

    f.glyphOrder = glyphOrder

    # KERNING -----------------------------------------------------------

    for glyphName in glyphsToRemove:
        # iterate over all kerning pairs in the font
        for kerningPair in f.kerning.keys():

            # if glyph is in the kerning pair, remove it
            if glyphName in kerningPair:
                print('removing kerning pair (%s, %s)...' % kerningPair)
                del f.kerning[kerningPair]

    # COMPONENTS -------------------------------------------------------

    # iterate over all glyphs in the font
    for glyph in f:

        # skip glyphs which components
        if not glyph.components:
            continue

        # iterate over all components in glyph
        for component in glyph.components:

            # if the base glyph is the glyph to be removed
            if component.baseGlyph in glyphsToRemove:
                # delete the component
                glyph.removeComponent(component)
                
    # FONT KEYs -----------------------------------------------

    # clean up the rest of the data
    for glyphName in glyphsToRemove:
        print(glyphName)
        # remove from keys
        #if glyphName in f:
        if glyphName in f.keys():
            del f[glyphName]
        else:
            print("font does not contain a glyph named '%s'" % glyphName)

    # clearing this list so it's not saved...
    glyphsToRemove = []

for fontPath in inputFonts:
    f = OpenFont(fontPath, showInterface=False)
    
    removeGlyphs(glyphsToRemove, f)

    print("done!")
    f.save()
    f.close()
