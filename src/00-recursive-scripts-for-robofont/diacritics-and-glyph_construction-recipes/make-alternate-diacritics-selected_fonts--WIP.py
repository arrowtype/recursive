'''
If base letters (a, g, i, etc) have alternates (a.italic, g.italic, i.mono) and component diacritics (/agrave, /gcommaaccent, /iacute, etc), there should also be diacritics for the alternates (/agrave.italic, /gcommaaccent.italic, /iacute.mono, etc). 

This script does three primary things:
    → Copies anchors from base letters to alternates, if they are not yet added.
    → Uses Glyph Construction to build the alternate diacritics.
    → Generates designspace rules (this may be best to split into a separate script... TBD)

BEFORE USING:
    - Use 'src/00-recursive-scripts-for-robofont/checking-similarity-between-fonts/check-anchor-similarity-alt_glyphs-select_fonts.py' to make sure alt glyphs have similar anchors to defaults
'''
from vanilla.dialogs import *
from mojo.UI import OutputWindow
import re
OutputWindow().show()
OutputWindow().clear()

# from glyphConstruction import ParseGlyphConstructionListFromString, GlyphConstructionBuilder

files = getFile("Select files to build glyphs in", allowsMultipleSelection=True, fileTypes=["ufo"])
# recipeFile = getFile("Select Glyph Recipes .txt file", allowsMultipleSelection=False, fileTypes=["txt"])
recipeFile = "/Users/stephennixon/type-repos/recursive/src/00-recursive-scripts-for-robofont/diacritics-and-glyph_construction-recipes/diacritic-recipes-for-recursive.txt"

relevantSuffixes = "mono italic sans".split()

recipeGlyphs = {}

def lineIsRecipe(line):
    if '=' in line \
        and line[0] is not '#' \
        and line[0] is not '$' \
        and '.' not in line.split('=')[0]:
        
        return True

# actually, you should start with this
def getRecipesToCopyForAlts():
    with open(recipeFile, 'r') as recipe:
        for line in recipe:
            line = line.replace(' ','')
            if lineIsRecipe(line):
                
                composedGlyph = line.replace('?','').split('=')[0]

                parentGlyph = line.split('=')[1].split('+')[0]

                if parentGlyph not in recipeGlyphs.keys():
                    recipeGlyphs[parentGlyph] = {
                        'recipes': [],
                        'suffixes': []
                    }

                recipeGlyphs[parentGlyph]['recipes'].append(composedGlyph)


def getSuffixes(f):

    defaultGlyphsWithDiacritics = [key for key in recipeGlyphs.keys()]

    for g in f:
        if '.' in g.name:
            baseName, suffix = g.name.split('.')[0], g.name.split('.')[1]
            if baseName in defaultGlyphsWithDiacritics and \
                suffix in relevantSuffixes and \
                suffix not in recipeGlyphs[baseName]['suffixes']:

                recipeGlyphs[baseName]['suffixes'].append(suffix)


getRecipesToCopyForAlts()

print("recipeGlyphs")
print(recipeGlyphs)



# find suffixes needed for recipeGlyphs

for file in files:
    f = OpenFont(file, showInterface=False)

    getSuffixes(f)

    f.close()

print("recipeGlyphs")
print(recipeGlyphs)

altRecipeFile = open(recipeFile.replace('.txt','-generated-with_alts.txt'),"w+")

def duplicateRecipesForAlts():
    with open(recipeFile, 'r') as recipe:
        for line in recipe:
            line = line.replace(' ','')
            if lineIsRecipe(line):
                composedGlyph = line.replace('?','').split('=')[0]
                parentGlyph = line.split('=')[1].split('+')[0]

                recipes = [line]

                for suffix in recipeGlyphs[parentGlyph]['suffixes']:
                    # print(parentGlyph, suffix)

                    altComposition = line.split('=')[0] + '.' + suffix
                    altRecipe = re.sub('\=(.*?)\+', r"\1" + '.' + suffix + '+', '=' + line.split('=')[1])

                    altLine = altComposition + '=' + altRecipe

                    recipes.append(altLine)

                # line = line + '\n' + altLine
                line = '\n'.join(recipes)

                altRecipeFile.write(line + '\n')

                print(line)

                print('\n---------------------------\n')
            


duplicateRecipesForAlts()

altRecipeFile.close()

# TODO: there are things to not make alt diacritics of. How should these be handled?
    # ydot italic (wouldn't fit)
    # g.mono top accents (best with flat-top, "sans" form)
    # should /g vs /g.mono be treated specially (because /g.mono already has an "accent" with its ear)?


## TODO: (manually?) add 'top_viet' anchor to o and u, to avoid glyph construction transformations
    # Done in Mono
    # TODO in Sans

## DESIGNSPACE RULES
    # diacriticsDict = dictionary of each baseGlyph with list of its diacritics
    # in rules table, line by line:
        # if referenced glyph in diacriticsDict.keys()
            # for each item in key list, duplicate rule for diacritic, but keep suffixes



# for file in files:
#     f.save()
#     f.close()
