'''

    Make JSON file from the glyph widths in a font. Currently ignores 600-unit-wide glyphs, because this is specifically written to find widths in Recursive Sans.

    0. You must have FontTools installed (https://github.com/fonttools/fonttools)
    1. In your terminal, 

        python <path>/set-versioned-font-names.py <path>/<font>.ttf

'''

import os
import argparse
import pprint
import json
from fontTools.ttLib import TTFont
import unicodedata

parser = argparse.ArgumentParser(description='Add version numbering to font name IDs')

parser.add_argument('fonts', nargs="+")

def saveToJSON(dictionary, path):
    with open(path, 'w') as fp:
        json.dump(dictionary, fp, indent=4, sort_keys=True)

    print(f'Glyph width data saved to "{path}"')

# find glyph name
# use cmap table to find unicode
# save JSON that is unicode: width


def main():
    args = parser.parse_args()

    for font_path in args.fonts:

        glyphWidths = {}

        print("\n-----------------------------------------\n")
        print(font_path)
        ttfont = TTFont(font_path)

        print(type(ttfont["cmap"].getBestCmap()))

        unicodesDict = {}

        # key is the glyph number
        # cmap[key] is the glyph name


        for key in ttfont["cmap"].getBestCmap().keys():
            print(key, ttfont["cmap"].getBestCmap()[key])
            glyphName = ttfont["cmap"].getBestCmap()[key]
            # unicodesDict[glyphName] = '%04x' % key
            unicodesDict[glyphName] = key

        print('unicodesDict')
        print(unicodesDict)

        for glyphName in ttfont.getGlyphNames():

            if ttfont['hmtx'][glyphName][0] == 600:
                print(".")
            else:
                # print(glyphName)
                # print(ttfont['hmtx'][glyphName][0])

                if glyphName in unicodesDict.keys():
                    glyphUnicode = str(unicodesDict[glyphName])
                    # glyphWidths[glyphUnicode] = [ttfont['hmtx'][glyphName][0], glyphName]
                    glyphWidths[glyphUnicode] = ttfont['hmtx'][glyphName][0]
                # else:
                #     glyphWidths[glyphName] = [ttfont['hmtx'][glyphName][0]]

        
        filename, file_extension = os.path.splitext(font_path)
        jsonPath = f'{filename}-glyph_widths.json'
        saveToJSON(glyphWidths, jsonPath)




if __name__ == '__main__':
    main()
