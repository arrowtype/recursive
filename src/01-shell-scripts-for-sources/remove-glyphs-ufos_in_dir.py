import sys
import os
import subprocess
from fontParts.world import *
import defcon

# copy-paste to fill this list with whatever glyphs fontMake flags as not being interpolatable
glyphsToDelete = 'verticallinelowmod'.split(' ')

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

# run program
for ufo in sorted(ufosToAdjust):
    ufoPath = f"{head}/{ufo}"

    # font = defcon.Font(ufoPath)
    font = OpenFont(ufoPath, showInterface=False)

    removeGlyphs(glyphsToDelete, font)

    print("done!")
    font.save()
    font.close()