'''
Build accented glyphs in RoboFont3 using Glyph Construction.

'''
from vanilla.dialogs import *
from glyphConstruction import ParseGlyphConstructionListFromString, GlyphConstructionBuilder

# define glyph constructions
# e.g. equal_equal.code = equal & equal
# txt = '''\
# ?slash_slash.code = slash & slash
# ?exclam_exclam.code = exclam & exclam
# ?numbersign_numbersign.code = numbersign & numbersign
# ?equal_equal.code = equal & equal
# ?equal_equal_equal.code = equal & equal & equal
# ?exclam_equal.code = exclam & equal
# ?exclam_equal_equal.code = exclam & equal & equal
# ?less_equal.code = less & equal
# ?greater_equal.code = greater & equal
# ?equal_greater.code = equal & greater
# ?question_question.code = question & question
# ?ampersand_ampersand.code = ampersand & ampersand
# ?percent_percent.code = percent & percent
# ?numbersign_numbersign_numbersign.code = numbersign & numbersign & numbersign
# ?numbersign_numbersign_numbersign_numbersign.code = numbersign & numbersign & numbersign & numbersign
# ?bar_bar.code = bar & bar
# ?dollar_braceleft.code = dollar & braceleft
# ?less_hyphen.code = arrowleft & .arrowhead
# ?hyphen_greater.code = x & arrowright
# f_quote.code = f & quotedbl
# equal_slash_equal.code = equal & slash & equal
# question_period.code = question & period
# question_colon.code = question & colon
# ampersand_ampersand_ampersand.code = ampersand & ampersand & ampersand
# bar_bar_bar.code = bar & bar & bar
# '''

# txt='''\
# equal_equal_equal.code = equal&equal&equal
# exclam_equal.code = exclam&equal
# exclam_equal_equal.code = exclam&equal&equal
# less_equal.code = less&equal
# greater_equal.code = greater&equal
# equal_greater.code = equal&greater
# hyphen_greater.code = hyphen&greater
# less_hyphen.code = less&hyphen
# equal_slash_equal.code = equal&slash&equal
#'''

# txt='''\
# equal.precode=equal
# hyphen.precode=hyphen
# '''

# txt='''\
# equal_equal.code = equal&equal
# '''

# txt='''\
# fi.mono = f.mono & i.mono
# fi.italic = f.italic & i.italic
# fl.mono = f.mono & l.mono
# fl.italic = f.italic & l.italic
# f_f.mono = f.mono & f.mono
# f_f.italic = f.italic & f.italic
# f_f_i.mono = f.mono & f.mono & i.mono
# f_f_i.italic = f.italic & f.italic & i.italic
# f_f_l.mono = f.mono & f.mono & l.mono
# f_f_l.italic = f.italic & f.italic & l.italic
# Lj.italic = L & j.italic
# lj.italic = l.italic & j.italic
# dzcaron.italic = d.italic & zcaron
# Nj.italic = N & j.italic
# nj.italic = n & j.italic
# '''

# txt='''\
# numbersign.code = numbersign
# f_quote.code = f & quotesingle
# underscore_underscore.code = underscore & underscore
# slash_asterisk.code = slash & asterisk
# asterisk_slash.code = asterisk & slash
# slash_slash_slash.code = slash & slash & slash
# quotesingle_quotesingle_quotesingle.code = quotesingle & quotesingle & quotesingle
# quotedbl_quotedbl_quotedbl.code = quotedbl & quotedbl & quotedbl
# grave_grave_grave.code = grave & grave & grave
# less_exclam_hyphen_hyphen.code = less & exclam & hyphen & hyphen
# hyphen_hyphen_greater.code = hyphen & hyphen & greater
# greater_hyphen.code = greater & hyphen
# hyphen_less.code = hyphen & less
# colon_colon.code = colon & colon
# greater_greater.code = greater & greater
# greater_greater_greater.code = greater & greater & greater
# less_less.code = less & less
# less_less_less.code = less & less & less
# less.code = less
# greater.code = greater
# colon_slash_slash.code = colon & slash & slash
# plus.code = plus
# plus_plus.code = plus & plus
# plus_plus_plus.code = plus & plus & plus
# hyphen.code = hyphen
# hyphen_hyphen.code = hyphen & hyphen
# hyphen_hyphen_hyphen.code = hyphen & hyphen & hyphen
# asterisk.code = asterisk
# asterix_asterix.code = asterisk & asterisk
# asterix_asterix_asterix.code = asterisk & asterisk & asterisk
# plus_equal.code = plus & equal
# minus_equal.code = minus & equal
# asterisk_equal.code = asterisk & equal
# slash_equal.code = slash & equal
# percent_c.code = percent & c
# percent_d.code = percent & d
# percent_s.code = percent & s
# percent_g.code = percent & g
# percent_r.code = percent & r
# backslash_n.code = backslash & n
# backslash_b.code = backslash & b
# backslash_r.code = backslash & r
# backslash_t.code = backslash & t
# backslash_v.code = backslash & v
# quotesingle.code = quotesingle
# quotedbl.code = quotedbl
# backslash.code = backslash
# braceleft_bracketleft.code = braceleft & bracketleft
# bracketright_braceright.code = bracketright & braceright
# bracketleft_bracketleft.code = bracketleft & bracketleft
# bracketright_bracketright.code = bracketright & bracketright
# bracketleft_parenleft.code = bracketleft & parenleft
# parenright_bracketright.code = parenright & bracketright
# braceleft_parenleft.code = braceleft & parenleft
# parenright_braceright.code = parenright & braceright
# parenleft_parenleft.code = parenleft & parenleft
# parenright_parenright.code = parenright & parenright
# hyphen_space_bracketleft_space_bracketright.code = hyphen & bracketleft & space & bracketright
# hyphen_space_bracketleft_x_bracketright.code = hyphen & bracketleft & x & bracketright
# '''

txt='''\
hyphen_space_bracketleft_space_bracketright.code = hyphen & bracketleft & space & bracketright
hyphen_space_bracketleft_x_bracketright.code = hyphen & bracketleft & x & bracketright
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
