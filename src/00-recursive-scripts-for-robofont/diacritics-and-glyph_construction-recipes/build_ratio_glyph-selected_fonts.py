'''
Build accented glyphs in RoboFont3 using Glyph Construction.

'''
from vanilla.dialogs import *
from glyphConstruction import ParseGlyphConstructionListFromString, GlyphConstructionBuilder

files = getFile("Select files to build glyphs in", allowsMultipleSelection=True, fileTypes=["ufo"])

# Set to False to open fonts with RoboFont UI (e.g. to visually check changes before saving)
skipInterface = True

for file in files:

    if skipInterface:
        font = OpenFont(file, showInterface=False)
    else:
        font = OpenFont(file, showInterface=True)

    # SPECIFIC TO RATIO GLYPH
    leftMargin = font["colon"].leftMargin
    raiseBy = round((font.info.capHeight - font["colon"].bounds[3]) / 2)
    txt = f'ratio = colon'
    constructions = ParseGlyphConstructionListFromString(txt)
    # collect glyphs to ignore if they already exist in the font
    ignoreExisting = [L.split('=')[0].strip()[1:] for L in txt.split('\n') if L.startswith('?')]

    print(constructions)

    # iterate over all glyph constructions
    for construction in constructions:

        print(construction, font)
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
        glyph.markColor = 0, 0, 1, 0.5

        # SPECIFIC TO RATIO GLYPH
        if glyph.name == "ratio":
            for component in glyph.components:
                # center it
                if "Slanted" in font.path:
                    component.moveBy((20, raiseBy)) # 20 is just approximately accurate for all slanted sources
                else:
                    component.moveBy((0, raiseBy))



        # if no unicode was given, try to set it automatically
        if glyph.unicode is None:
            glyph.autoUnicodes()

    if skipInterface:
        font.save()
        font.close()
