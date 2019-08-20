'''

    Font versions often clash in software. The simplest way to avoid that is to add a version number to new fonts, e.g.

        "Recursive Mono Beta v1.014"

    ...but this can be annoying to add to new files. This script makes it simple. To use:

    0. You must have FontTools installed (https://github.com/fonttools/fonttools)
    1. In your terminal, 

        python <path>/set-versioned-font-names.py <path>/<font>.ttf

'''

import os
import argparse
import pprint
import json
from fontTools.ttLib import TTFont

parser = argparse.ArgumentParser(description='Add version numbering to font name IDs')

parser.add_argument('fonts', nargs="+")

def saveToJSON(fontPath, widthDict):
    filename, file_extension = os.path.splitext(fontPath)

    jsonPath = f'{filename}-glyph_widths.json'

    with open(jsonPath, 'w') as fp:
        json.dump(widthDict, fp, indent=4, sort_keys=True)

    print(f'Glyph width data saved to {jsonPath}')



def main():
    args = parser.parse_args()

    for font_path in args.fonts:

        glyphWidths = {}

        print("\n-----------------------------------------\n")
        print(font_path)
        ttfont = TTFont(font_path)

        for glyphName in ttfont.getGlyphNames():
            print(".")

            if ttfont['hmtx'][glyphName][0] != 600:
                print(glyphName)
                print(ttfont['hmtx'][glyphName][0])
                glyphWidths[glyphName] = ttfont['hmtx'][glyphName][0]


        saveToJSON(font_path, glyphWidths)

        

        



if __name__ == '__main__':
    main()
