'''
Build accented glyphs in RoboFont3 using Glyph Construction.

'''
from vanilla.dialogs import *
from glyphConstruction import ParseGlyphConstructionListFromString, GlyphConstructionBuilder

# define glyph constructions
txt = '''\
?Gamma = T | 0393
?Delta = A | 0394
?Theta = O + hyphen@center | 0398
?Lambda = A | 039b
?Pi = H | 03a0
?Phi = O + bar@center | 03a6
?gamma = v + bar@center | 03b3
?delta = o + s@top | 03b4
?theta = zero + hyphen@center | 03b8
?lambda = l + v | 03bb
?phi = o + bar@center | 03c6
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
        glyph.markColor = 1, 0.75, 0, 0.5

        # if no unicode was given, try to set it automatically
        if glyph.unicode is None:
            glyph.autoUnicodes()

        # # if you have to apply a transformation to a specific glyph
        # if glyph.name == "minus.superior":
        #     for component in glyph.components:
        #         component.transformation = (0.5833373454702526, 0, 0, 0.5833373454702521, 25, 394)

    if skipInterface:
        font.save()
        font.close()
