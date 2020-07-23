"""
    A script to change dlig features to calt features, 
    to make code ligatures on by default in Rec Mono for Code.
"""

from babelfont import OpenFont
from fontTools import ttLib
from fontTools.feaLib import builder
from fontTools.pens import basePen
from fontTools.pens import ttGlyphPen
from fontTools.pens.recordingPen import DecomposingRecordingPen

import fire

# def makeLigGlyph(font):
#     # copy /space glyph
#     # rename as "LIG"



# TODO: make all glyphs 600 units wide, cropping on left
    # make dictionary of width units while you do this
    # advance_sb_pair = 600, 600-prevWidth

# TODO: update dlig code

codeLigs = {}

## attempt to use babelFont; didn’t work: https://github.com/simoncozens/babelfont/issues/6
# def decomposeCodeLigs(fontPath, inplace=False):
#     font = OpenFont(fontPath)
#     for glyph in font:
#         print(glyph.name, glyph.width)
#         if glyph.width > 600:
#             for comp in glyph.components:
#                 comp.decompose()
#     # then save

def decomposeGlyph(font, glyphName):

    components = (font['glyf'][glyphName].getComponentNames(font['glyf']))

    ## BASIC IDEA (not yet working)
    # for component in glyph
        # record tt points of component base
        # draw points to glyph
    
    glyphset = font.getGlyphSet()

    for comp in components:
        glyph = glyphset[comp]
        pen = ttGlyphPen.TTGlyphPen(glyph)
        help(pen)
        # font['glyf'][glyphName].drawPoints(pen, font['glyf'])
        font['glyf'][glyphName].draw(pen, font['glyf'])


    ## Also tried:

    # glyphset = font.getGlyphSet()
    # glyph = glyphset[glyphName]
    # print(glyph)
    # # pen = basePen.DecomposingPen(glyph)
    # pen = DecomposingRecordingPen(glyph)
    # print(pen.value)
    # ttpen = ttGlyphPen.TTGlyphPen(pen)
    # glyph.draw(ttpen)

# def decomposeGlyph(font,glyphName):
#     glyph = font.getGlyphSet()[glyphName]
#     pen = basePen.DecomposingPen(glyph)
#     glyph.draw(pen)

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

            decomposeGlyph(font, glyphName)

            # add to dict for later
            codeLigs[glyphName] = font['hmtx'][glyphName][0]

            # set width to space (e.g. 600), then offset left side to be negative
            # lsb = oldLSB - oldWidth
            oldLSB = font['hmtx'][glyphName][1]
            oldWidth = font['hmtx'][glyphName][0]
            newLSB = oldLSB - (oldWidth - unitWidth)
            font['hmtx'].__setitem__(glyphName, (unitWidth, newLSB))


    # add new feature code, using calt rather than dlig

    # builder.addOpenTypeFeatures(font,"src/features/features.fea",tables="GSUB")
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
