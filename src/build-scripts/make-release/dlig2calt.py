"""
    A script to change dlig features to calt features, 
    to make code ligatures on by default in Rec Mono for Code.
"""

from fontTools import ttLib
import fire

# def makeLigGlyph(font):
#     # copy /space glyph
#     # rename as "LIG"



# TODO: make all glyphs 600 units wide, cropping on left
    # make dictionary of width units while you do this
    # advance_sb_pair = 600, 600-prevWidth

# TODO: update dlig code

codeLigs = {}

def dlig2calt(fontPath, inplace=False):
    font = ttLib.TTFont(fontPath)

    unitWidth = font['hmtx']['space'][0] # 600 for most monospace fonts w/ UPM=1000

    # make "LIG" glyph
    # __setitem__(self, glyphName, glyph)
    font['glyf'].__setitem__('LIG', font['glyf']['space'])

    # __setitem__(self, glyphName, advance_sb_pair)
    font['hmtx'].__setitem__('LIG', font['hmtx']['space'])

    for glyphName in font.getGlyphNames():
        if font['hmtx'][glyphName][0] > 600:
            print(glyphName, font['hmtx'][glyphName])

            # add to dict for later
            codeLigs[glyphName] = font['hmtx'][glyphName][0]

            # set width to space (e.g. 600), then offset left side to be negative
            font['hmtx'].__setitem__(glyphName, (unitWidth, unitWidth - font['hmtx'][glyphName][0]))

    # update dlig feature to 'calt'
    featureRecords = font['GSUB'].table.FeatureList.FeatureRecord
    for fea in featureRecords:
        if fea.FeatureTag == 'dlig':
            fea.FeatureTag = 'calt'
            print('Updated feature "dlig" to be "calt".')


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
