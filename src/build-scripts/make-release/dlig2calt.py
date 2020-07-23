"""
    A script to change dlig features to calt features, 
    to make code ligatures on by default in Rec Mono for Code.
"""

from fontTools import ttLib
from fontTools.feaLib import builder
from fontTools.pens.recordingPen import DecomposingRecordingPen
from fontTools.pens.ttGlyphPen import TTGlyphPen

import fire # alternative to argparse, used to easily fire the script

try:
    import pathops
except ImportError:
    sys.exit(
        "This script requires the skia-pathops module. "
        "`pip install skia-pathops` and then retry."
    )

def decomposeAndRemoveOverlap(font, glyphName):

    glyfTable = font["glyf"]
    glyphSet = font.getGlyphSet()

    # record TTGlyph outlines without components
    dcPen = DecomposingRecordingPen(glyphSet)
    glyphSet[glyphName].draw(dcPen)

    # replay recording onto a skia-pathops Path
    path = pathops.Path()
    pathPen = path.getPen()
    dcPen.replay(pathPen)

    # remove overlaps
    path.simplify()

    # create new TTGlyph from Path
    ttPen = TTGlyphPen(None)
    path.draw(ttPen)
    glyfTable[glyphName] = ttPen.glyph()


# codeLigs = {} # probably not needed

def dlig2calt(fontPath, inplace=False):

    font = ttLib.TTFont(fontPath)

    unitWidth = font['hmtx']['space'][0] # 600 for most monospace fonts w/ UPM=1000

    # make "LIG" glyph
    # __setitem__(self, glyphName, glyph)
    font['glyf'].__setitem__('LIG', font['glyf']['space'])

    # __setitem__(self, glyphName, advance_sb_pair)
    font['hmtx'].__setitem__('LIG', font['hmtx']['space'])

    # update code ligature widths to be single units with left overhang
    for glyphName in font.getGlyphNames():
        if font['hmtx'][glyphName][0] > 600:

            decomposeAndRemoveOverlap(font, glyphName)

            # add to dict for later?
            # codeLigs[glyphName] = font['hmtx'][glyphName][0]

            # set width to space (e.g. 600), then offset left side to be negative
            # lsb = oldLSB - oldWidth
            oldLSB = font['hmtx'][glyphName][1]
            oldWidth = font['hmtx'][glyphName][0]
            newLSB = oldLSB - (oldWidth - unitWidth)
            font['hmtx'].__setitem__(glyphName, (unitWidth, newLSB))


    # add new feature code, using calt rather than dlig
    builder.addOpenTypeFeatures(font,"src/features/features/calt-generated--code_fonts_only.fea")


    # save font
    if inplace:
        font.save(fontPath)
        print("Saved font inplace with feature 'dlig' changed to 'calt'.")
    else:
        newPath = fontPath.replace('.ttf','.calt_ligs.ttf')
        font.save(newPath)
        print("Saved font with feature 'dlig' changed to 'calt' at ", newPath)


if __name__ == '__main__':
    fire.Fire(dlig2calt)
