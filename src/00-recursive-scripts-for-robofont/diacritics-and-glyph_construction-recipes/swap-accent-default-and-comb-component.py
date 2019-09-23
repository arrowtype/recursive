'''
Decomponentize /horncomb, make /horn a component glyph of it.

'''

print("hey")
# from vanilla.dialogs import *
# from glyphConstruction import ParseGlyphConstructionListFromString, GlyphConstructionBuilder

# files = getFile("Select files to build glyphs in", allowsMultipleSelection=True, fileTypes=["ufo"])

# # # the key will use its value as a component
# # # you probably want the "combining" accent to be the value, so it is the source of truth / thing you draw
# # accentsToSwap = {
# #     "horn": "horncomb"
# # }

# txt = '''\
# horn = horncomb@`center, 400`
# '''
# constructions = ParseGlyphConstructionListFromString(txt)

# # collect glyphs to ignore if they already exist in the font
# ignoreExisting = [L.split('=')[0].strip()[1:] for L in txt.split('\n') if L.startswith('?')]

# for file in files:
#     font = OpenFont(file, showInterface=False)

#     if "horncomb" in font.keys():
#         font["horncomb"].decompose()

#     for construction in constructions:

#         # build a construction glyph
#         constructionGlyph = GlyphConstructionBuilder(construction, font)

#         # if the construction for this glyph was preceded by `?`
#         # and the glyph already exists in the font, skip it
#         if constructionGlyph.name in font and constructionGlyph.name in ignoreExisting:
#             continue

#         # get the destination glyph in the font
#         glyph = font.newGlyph(constructionGlyph.name, clear=True)

#         # draw the construction glyph into the destination glyph
#         constructionGlyph.draw(glyph.getPen())

#         # copy construction glyph attributes to the destination glyph
#         glyph.name = constructionGlyph.name
#         glyph.unicode = constructionGlyph.unicode
#         glyph.width = constructionGlyph.width
#         glyph.markColor = 0, 0, 0, 0.5

#         # if no unicode was given, try to set it automatically
#         if glyph.unicode is None:
#             glyph.autoUnicodes()