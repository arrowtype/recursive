'''
Build accented glyphs in RoboFont3 using Glyph Construction.

'''
from vanilla.dialogs import *
from glyphConstruction import ParseGlyphConstructionListFromString, GlyphConstructionBuilder

# define glyph constructions
# e.g. equal_equal.code = equal & equal
txt = '''\
parenleft.case = parenleft
parenright.case = parenright
bracketleft.case = bracketleft
bracketright.case = bracketright
braceleft.case = braceleft
braceright.case = braceright
at.case = at
guilsinglleft.case = guilsinglleft
guilsinglright.case = guilsinglright
guillemotleft.case = guillemotleft
guillemotright.case = guillemotright
slash.case = slash
backslash.case = backslash
periodcentered.case = periodcentered
bullet.case = bullet
questiondown.case = questiondown
exclamdown.case = exclamdown
hyphen.case = hyphen
endash.case = endash
emdash.case = emdash
arrowleft.case = arrowleft
arrowright.case = arrowright
arrowup.case = arrowup
arrowdown.case = arrowdown
?arrowleftright.case = arrowleftright
?arrowupdown.case = arrowupdown
arrowNW.case = arrowNW
arrowNE.case = arrowNE
arrowSE.case = arrowSE
arrowSW.case = arrowSW
plus.case = plus
minus.case = minus
divide.case = divide
plusminus.case = plusminus
multiply.case = multiply
equal.case = equal
notequal.case = notequal
approxequal.case = approxequal
less.case = less
greater.case = greater
lessequal.case = lessequal
greaterequal.case = greaterequal
logicalnot.case = logicalnot
colon.case = colon
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
        glyph.markColor = 0, 0, 0, 0.5

        # if no unicode was given, try to set it automatically
        if glyph.unicode is None:
            glyph.autoUnicodes()

    font.save()
    font.close()
