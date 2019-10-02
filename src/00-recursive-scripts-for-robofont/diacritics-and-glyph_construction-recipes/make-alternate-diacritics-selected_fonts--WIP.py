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

for file in files:
    font = OpenFont(file, showInterface=False)

    ## ANCHORS
    # make list of all alternates that are common between fonts
    # make set of base glyphs baseGlyphs
    # copy anchors to alternates, if not already present

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

    font.save()
    font.close()
