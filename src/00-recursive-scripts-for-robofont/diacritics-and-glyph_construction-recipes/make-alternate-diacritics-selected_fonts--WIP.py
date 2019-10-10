'''
If base letters (a, g, i, etc) have alternates (a.italic, g.italic, i.mono) and component diacritics (/agrave, /gcommaaccent, /iacute, etc), there should also be diacritics for the alternates (/agrave.italic, /gcommaaccent.italic, /iacute.mono, etc). 

This script does three primary things:
    → Copies anchors from base letters to alternates, if they are not yet added.
    → Uses Glyph Construction to build the alternate diacritics.
    → Generates designspace rules (this may be best to split into a separate script... TBD)
'''
from vanilla.dialogs import *
from mojo.UI import OutputWindow
# from glyphConstruction import ParseGlyphConstructionListFromString, GlyphConstructionBuilder

files = getFile("Select files to build glyphs in", allowsMultipleSelection=True, fileTypes=["ufo"])
# recipeFile = getFile("Select Glyph Recipes .txt file", allowsMultipleSelection=False, fileTypes=["txt"])
recipeFile = "/Users/stephennixon/type-repos/recursive/src/00-recursive-scripts-for-robofont/diacritics-and-glyph_construction-recipes/diacritic-recipes-for-recursive.txt"

OutputWindow().show()
OutputWindow().clear()

## TODO: COPY ANCHORS TO ALTS (if not present)
# make list of all alternates that are common between fonts
# copy anchors to alternates, if not already present

alternates = []
altsDict = {}
defaultGlyphs = []
defaultGlyphsWithDiacritics = {}
diacriticsWithDefaultGlyphs = []

relevantAlts = "mono italic sans".split()

# TODO: do these need to be in *all* fonts? check back on it
def getAlts(f):
    for g in f:
        if "." in g.name and g.name not in alternates and g.name.split(".")[1] in relevantAlts:
            alternates.append(g.name)

        if "." in g.name:
            base, suffix = g.name.split(".")[0], g.name.split(".")[1]
            
            if base not in altsDict.keys() and suffix in relevantAlts:
                altsDict[base] = []
            
            if suffix in relevantAlts and suffix not in altsDict[base]:
                altsDict[base].append(suffix)

def getDefaultGlyphs(f):
    for alt in alternates:
        base = alt.split(".")[0]
        if base not in defaultGlyphs and base in f.keys():
            defaultGlyphs.append(base)

def getBaseGlyphs(f):
    for g in f:
        for comp in g.components:
            parent = comp.baseGlyph
            if parent in defaultGlyphs and parent not in defaultGlyphsWithDiacritics.keys():
                defaultGlyphsWithDiacritics[parent] = []
            if parent in defaultGlyphs and g.name not in diacriticsWithDefaultGlyphs:
                defaultGlyphsWithDiacritics[parent].append(g.name)

recipesToCopyForAlts = []

def getRecipesToCopyForAlts(f):
    with open(recipeFile, 'r') as recipe:
        for line in recipe:
            if \
                '=' in line and \
                '#' not in line and \
                line.replace('?','').split('=')[0] in diacriticsWithDefaultGlyphs and \
                line not in recipesToCopyForAlts:

                recipesToCopyForAlts.append(line)

for file in files:
    f = OpenFont(file, showInterface=False)

    getAlts(f)
    getDefaultGlyphs(f)
    getBaseGlyphs(f)

    getRecipesToCopyForAlts(f)

    f.save()
    f.close()

print("alternates:")
print(sorted(alternates))
print("")
print("defaultGlyphs:")
print(sorted(defaultGlyphs))
# print("")
# print("defaultGlyphsWithDiacritics:")
# print(sorted(defaultGlyphsWithDiacritics))
# print("")
# print("diacriticsWithDefaultGlyphs:")
# print(sorted(diacriticsWithDefaultGlyphs))


print("\n--------------------------------------alternates:\n")
for key in altsDict:
    print(key,altsDict[key],"\n")

print("\n--------------------------------------defaultGlyphsWithDiacritics:\n")
for key in defaultGlyphsWithDiacritics:
    print(key,defaultGlyphsWithDiacritics[key],"\n")
# print(defaultGlyphsWithDiacritics)

# for L in sorted(recipesToCopyForAlts):
#     print(L)



    # you need a dict that has suffixes to diacrtics needed
        # mono
            # dotlessi
                # iacute.mono=dotlessi.mono+acutecomb@top
                # ibreve.mono=dotlessi.mono+brevecomb@top
                # icircumflex.mono=dotlessi.mono+circumflexcomb@top
                # idieresis.mono=dotlessi.mono+dieresiscomb@top
                # idotbelow.mono=dotlessi.mono+dotbelowcomb@bottom+dotaccentcomb@dotlessi:top
                # igrave.mono=dotlessi.mono+gravecomb@top
                # ihook.mono=dotlessi.mono+hookcomb@hook
                # imacron.mono=dotlessi.mono+macroncomb@top
                # itilde.mono=dotlessi.mono+tildecomb@top
            # dotlessj
                # j.mono=dotlessj.mono+dotaccentcomb@top
                # jcircumflex.mono=dotlessj.mono+circumflexcomb@top
            # ETC


    # dict glyphAlts
        # i
            # mono
            # italic
            # sans
        # m
            # italic
        # ETC


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
