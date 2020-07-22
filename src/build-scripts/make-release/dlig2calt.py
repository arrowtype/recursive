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

# TODO: update dlig code


def dlig2calt(fontPath, inplace=False):
    font = ttLib.TTFont(fontPath)

    # make "LIG" glyph
    # __setitem__(self, glyphName, glyph)
    font['glyf'].__setitem__('LIG', font['glyf']['space'])

    # __setitem__(self, glyphName, advance_sb_pair)
    font['hmtx'].__setitem__('LIG', font['hmtx']['space'])

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
