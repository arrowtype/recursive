'''
Build accented glyphs in RoboFont3 using Glyph Construction.

'''
from vanilla.dialogs import *
from glyphConstruction import ParseGlyphConstructionListFromString, GlyphConstructionBuilder

# define glyph constructions
# e.g. equal_equal.code = equal & equal
# i=dotlessi+dotaccentcomb@top
# i.mono=dotlessi.mono+dotaccentcomb@top
# i.italic=dotlessi.italic+dotaccentcomb@top
# j=dotlessj+dotaccentcomb@top
# j.italic=dotlessj.italic+dotaccentcomb@top
# iogonek = dotlessi + ogonekcomb@ogonek + dotaccentcomb@dotlessi:top
# iogonek.mono = dotlessi.mono + ogonekcomb@ogonek + dotaccentcomb@dotlessi.mono:top
# iogonek.italic = dotlessi.italic + ogonekcomb@ogonek + dotaccentcomb@dotlessi.italic:top
# txt = '''\
# apple=.notdef|F8FF
# '''


# zerosuperior.slash = zerosuperior
# zeroinferior.slash = zeroinferior
# zeroinferiorslash.afrc = zerosuperior.afrc
# zerosuperiorslash.afrc = zeroinferior.afrc
txt = '''\
ringbelowcomb=ringcomb | 0325
'''

# recipeFile = "/Users/stephennixon/type-repos/recursive/src/00-recursive-scripts-for-robofont/diacritics-and-glyph_construction-recipes/diacritic-recipes-for-recursive-generated-with_alts.txt"
# with open(recipeFile, 'r') as recipe:
#     for line in recipe:
#         line = line.replace(' ','')
#         if len(line) > 1:
#             txt += line

print(txt)
# get the actual glyph constructions from text
constructions = ParseGlyphConstructionListFromString(txt)



files = getFile("Select files to build glyphs in", allowsMultipleSelection=True, fileTypes=["ufo"])

# collect glyphs to ignore if they already exist in the font
ignoreExisting = [L.split('=')[0].strip()[1:] for L in txt.split('\n') if L.startswith('?')]

# Set to False to open fonts with RoboFont UI (e.g. to visually check changes before saving)
skipInterface = True

for file in files:

    if skipInterface:
        font = OpenFont(file, showInterface=False)
    else:
        font = OpenFont(file, showInterface=True)

    # iterate over all glyph constructions
    for construction in constructions:

        print(construction)
        # build a construction glyph
        constructionGlyph = GlyphConstructionBuilder(construction, font)

        # if the construction for this glyph was preceded by `?`
        # and the glyph already exists in the font, skip it
        if constructionGlyph.name in font and constructionGlyph.name in ignoreExisting:
            continue

        # get the destination glyph in the font
        glyph = font.newGlyph(constructionGlyph.name, clear=True)

        # draw the construction glyph into the destination glyph
        constructionGlyph.draw(glyph.getPen())

        # copy construction glyph attributes to the destination glyph
        glyph.name = constructionGlyph.name
        glyph.unicode = constructionGlyph.unicode
        glyph.width = constructionGlyph.width
        glyph.markColor = 0, 0, 0, 0.5

        # if no unicode was given, try to set it automatically
        if glyph.unicode is None:
            glyph.autoUnicodes()

    if skipInterface:
        font.save()
        font.close()
