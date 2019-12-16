'''
Build accented glyphs in RoboFont3 using Glyph Construction.

'''
from vanilla.dialogs import *
from glyphConstruction import ParseGlyphConstructionListFromString, GlyphConstructionBuilder

# define glyph constructions

txt = '''\

# a.simple = a.italic 
# aacute.simple = aacute.italic 
# abreve.simple = abreve.italic 
# abreveacute.simple = abreveacute.italic 
# abrevedot.simple = abrevedot.italic 
# abrevegrave.simple = abrevegrave.italic 
# abrevehook.simple = abrevehook.italic 
# abrevetilde.simple = abrevetilde.italic 
# acircumflex.simple = acircumflex.italic 
# acircumflexacute.simple = acircumflexacute.italic 
# acircumflexdot.simple = acircumflexdot.italic 
# acircumflexgrave.simple = acircumflexgrave.italic 
# acircumflexhook.simple = acircumflexhook.italic 
# acircumflextilde.simple = acircumflextilde.italic 
# adieresis.simple = adieresis.italic 
# adotbelow.simple = adotbelow.italic 
# agrave.simple = agrave.italic 
# ahook.simple = ahook.italic 
# amacron.simple = amacron.italic 
# aogonek.simple = aogonek.italic 
# aring.simple = aring.italic 
# aringacute.simple = aringacute.italic 
atilde.simple = atilde.italic
# g.simple = g.italic 
# gbreve.simple = gbreve.italic 
# gcaron.simple = gcaron.italic 
# gcircumflex.simple = gcircumflex.italic 
# gcommaaccent.simple = gcommaaccent.italic 
# gdotaccent.simple = gdotaccent.italic
# f.simple = f
# l.simple = l.italic
# lacute.simple = lacute.italic
# lcommaaccent.simple = lcommaaccent.italic
# ldotbelow.simple = ldotbelow.italic
# llinebelow.simple = llinebelow.italic
# lslash.simple = lslash.italic
# r.simple = r.italic
# racute.simple = racute.italic
# rcaron.simple = rcaron.italic
# rcommaaccent.simple = rcommaaccent.italic
# one.simple = one.sans
'''



constructions = ParseGlyphConstructionListFromString(txt)



files = getFile("Select files to build glyphs in", allowsMultipleSelection=True, fileTypes=["ufo"])

# collect glyphs to ignore if they already exist in the font
ignoreExisting = [L.split('=')[0].strip()[1:] for L in txt.split('\n') if L.startswith('?')]

for file in files:
    font = OpenFont(file, showInterface=False)
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

    font.save()
    font.close()
