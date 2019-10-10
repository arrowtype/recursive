'''
If base letters (a, g, i, etc) have alternates (a.italic, g.italic, i.mono) and component diacritics (/agrave, /gcommaaccent, /iacute, etc), there should also be diacritics for the alternates (/agrave.italic, /gcommaaccent.italic, /iacute.mono, etc). 

This script does three primary things:
    → Copies anchors from base letters to alternates, if they are not yet added.
    → Uses Glyph Construction to build the alternate diacritics.
    → Generates designspace rules (this may be best to split into a separate script... TBD)
'''
from vanilla.dialogs import *
# from glyphConstruction import ParseGlyphConstructionListFromString, GlyphConstructionBuilder

files = getFile("Select files to build glyphs in", allowsMultipleSelection=True, fileTypes=["ufo"])


## ANCHORS
# make list of all alternates that are common between fonts
# make set of base glyphs baseGlyphs
# copy anchors to alternates, if not already present
alternates = []
baseGlyphs = []

# IF suffix is mono, italic, or sans

def getAlts(f):
    for g in f:
        if "." in g.name and g.name not in alternates:
            alternates.append(g.name)

def getBases(f):
    for alt in alternates:
        base = alt.split(".")[0]
        if base not in baseGlyphs and base in f.keys():
            baseGlyphs.append(base)

for file in files:
    f = OpenFont(file, showInterface=False)

    getAlts(f)
    getBases(f)

    f.save()
    f.close()

print("alternates:")
print(alternates)
print("")
print("baseGlyphs:")
print(baseGlyphs)

    # for g in f:
    #     if g not in alternates:
    #         alternates.append(g)

# for file in files:
#     f = OpenFont(file, showInterface=False)
#     for alt in alternates:
#         if f[alt]

    ## GLYPH CONSTRUCTION
    # baseDiacritics = make list of all component glyphs that contain baseGlyphs
    # eliminate glyphs that aren't common between fonts
    # read glyph construction recipes file (first: fix vietnamese weight-specific code?)
    # line by line: if first word is in baseDiacritics
        # duplicate that line
        # add alt suffix to first word and to baseGlyph in recipe
    
    ## DESIGNSPACE RULES
    # diacriticsDict = dictionary of each baseGlyph with list of its diacritics
    # in rules table, line by line:
        # if referenced glyph in diacriticsDict.keys()
            # for each item in key list, duplicate rule for diacritic, but keep suffixes

# for file in files:
#     f.save()
#     f.close()
