'''
If base letters (a, g, i, etc) have alternates (a.italic, g.italic, i.mono) and component diacritics (/agrave, /gcommaaccent, /iacute, etc), there should also be diacritics for the alternates (/agrave.italic, /gcommaaccent.italic, /iacute.mono, etc). 

This script does three primary things:
    → Copies anchors from base letters to alternates, if they are not yet added.
    → Uses Glyph Construction to build the alternate diacritics.
    → Generates designspace rules (this may be best to split into a separate script... TBD)
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

def duplicateRecipesForAlts():
    with open(recipeFile, 'r') as recipe:
        for line in recipe:
            line = line.replace(' ','')
            if lineIsRecipe(line):
                composedGlyph = line.replace('?','').split('=')[0]
                parentGlyph = line.split('=')[1].split('+')[0]

                for suffix in recipeGlyphs[parentGlyph]['suffixes']:
                    print(parentGlyph, suffix)

                    # TODO: find a way to insert suffixes on at composed glyph name and parent glyph reference
                    ## (not yet working)
                    # recipeGlyph = line.split('=')[1].split('+')[0]
                    altComposition = line.split('=')[0] + '.' + suffix
                    altRecipe = re.sub('\=(.*?)\+', r"\1" + '.' + suffix + '+', '=' + line.split('=')[1])

                    altLine = altComposition + '=' + altRecipe

                    line = line + '\n' + altLine

                    print(line)

duplicateRecipesForAlts()


## TODO: COPY ANCHORS TO ALTS (if not present)
# make list of all alternates that are common between fonts
# copy anchors to alternates, if not already present


## GLYPH CONSTRUCTION
# baseDiacritics = make list of all component glyphs that contain baseGlyphs
# eliminate glyphs that aren't common between fonts
# read glyph construction recipes file (first: fix vietnamese weight-specific code?)
# line by line: if first word is in baseDiacritics
    # duplicate that line
    # add alt suffix to first word and to baseGlyph in recipe

#   save new glyphrecipes file

## DESIGNSPACE RULES
# diacriticsDict = dictionary of each baseGlyph with list of its diacritics
# in rules table, line by line:
    # if referenced glyph in diacriticsDict.keys()
        # for each item in key list, duplicate rule for diacritic, but keep suffixes



# for file in files:
#     f.save()
#     f.close()
