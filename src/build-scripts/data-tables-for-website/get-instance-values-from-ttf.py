'''

    In a variable font, for each Named Instance, get:
    - style name
    - axis values

    ...and save into a JSON file.

    Usage:

    0. You must have FontTools installed (https://github.com/fonttools/fonttools)
    1. In your terminal, 

        python <path>/get-instance-values-from-ttf.py <path>/<font>.ttf

'''

import os
import argparse
import pprint
import json
from fontTools.ttLib import TTFont

parser = argparse.ArgumentParser(description='Add version numbering to font name IDs')

parser.add_argument('fonts', nargs="+")

def saveToJSON(dictionary, path):
    with open(path, 'w') as fp:
        json.dump(dictionary, fp, indent=4, sort_keys=True)

    print(f'Glyph width data saved to "{path}"')


def getFontNameID(font, ID, platformID=3, platEncID=1):
    name = str(font['name'].getName(ID, platformID, platEncID))
    return name


def main():
    args = parser.parse_args()

    for font_path in args.fonts:

        namedInstances = {}

        print("\n-----------------------------------------\n")
        print(font_path)
        ttfont = TTFont(font_path)

        print(type(ttfont["cmap"].getBestCmap()))

        for idx, instance in enumerate(ttfont['fvar'].instances):

            styleName = getFontNameID(ttfont, instance.subfamilyNameID)

            namedInstances[styleName] = instance.coordinates
            print(idx, instance)
            print(instance.coordinates)
            print(list(instance.coordinates.values())[0], instance.subfamilyNameID)

            # help(ttfont['name'])
            # print()

        print(namedInstances)

        
        filename, file_extension = os.path.splitext(font_path)
        jsonPath = f'{filename}-instance_vals.json'
        saveToJSON(namedInstances, jsonPath)




if __name__ == '__main__':
    main()
