'''
Build accented glyphs in RoboFont3 using Glyph Construction.

'''
from vanilla.dialogs import *
from glyphConstruction import ParseGlyphConstructionListFromString, GlyphConstructionBuilder

# define glyph constructions
# e.g. equal_equal.code = equal & equal
txt = '''\
?slash_slash.code = slash & slash
?exclam_exclam.code = exclam & exclam
?numbersign_numbersign.code = numbersign & numbersign
?equal_equal.code = equal & equal
?equal_equal_equal.code = equal & equal & equal
?exclam_equal.code = exclam & equal
?exclam_equal_equal.code = exclam & equal & equal
?less_equal.code = less & equal
?greater_equal.code = greater & equal
?equal_greater.code = equal & greater
?question_question.code = question & question
?ampersand_ampersand.code = ampersand & ampersand
?percent_percent.code = percent & percent
?numbersign_numbersign_numbersign.code = numbersign & numbersign & numbersign
?numbersign_numbersign_numbersign_numbersign.code = numbersign & numbersign & numbersign & numbersign
?bar_bar.code = bar & bar
?dollar_braceleft.code = dollar & braceleft
?less_hyphen.code = arrowleft & .arrowhead
?hyphen_greater.code = x & arrowright
f_quote.code = f & quotedbl
equal_slash_equal.code = equal & slash & equal
question_period.code = question & period
question_colon.code = question & colon
ampersand_ampersand_ampersand.code = ampersand & ampersand & ampersand
bar_bar_bar.code = bar & bar & bar
'''
# get the actual glyph constructions from text
constructions = ParseGlyphConstructionListFromString(txt)


files = getFile("Select files to build glyphs in", allowsMultipleSelection=True, fileTypes=["ufo"])

# collect glyphs to ignore if they already exist in the font
ignoreExisting = [L.split('=')[0].strip()[1:] for L in txt.split('\n') if L.startswith('?')]

for file in files:
    font = OpenFont(file, showInterface=False)
    # iterate over all glyph constructions
    for construction in constructions:

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
        glyph.markColor = 0.25, 1, 1, 0.5

        # if no unicode was given, try to set it automatically
        if glyph.unicode is None:
            glyph.autoUnicodes()

    font.save()
    font.close()
