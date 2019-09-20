'''
    Go through a font to find all alternate glyphs
    Find the accented versions of these in a txt file of glyph recipes

'''

import argparse
import os

parser = argparse.ArgumentParser(description='Add version numbering to font name IDs')

parser.add_argument('recipes', nargs="+")

# altGlyphs = []

# f = CurrentFont()

# for g in f:
#     if "." in g.name:
#         altGlyphs.append(g.name)

# import and open file to write

# filepath = args[0] # look up how to do this
# recipes = read filepath

# for name in altGlyphs:
#     baseGlyph = name.split('.')[0]
#     suffix = name.split('.')[1]
#     for line in recipes:
#         if name === line[0]:
#             # copy line 
#             # add suffix to first word
#             # find baseGlyph in line, add suffix
        
# # save file with suffix

# just get glyph names from glif files in UFO dir?

def main():
    args = parser.parse_args()

    for recipeFile in args.recipes:
        print(recipeFile)
        # help(os.open)
        with open(recipeFile, 'r') as recipe:
            for line in recipe:
                print(line)

if __name__ == '__main__':
    main()


