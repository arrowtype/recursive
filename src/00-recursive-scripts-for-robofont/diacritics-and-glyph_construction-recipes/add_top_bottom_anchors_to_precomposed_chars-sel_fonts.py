"""
    Script to add anchors to top/bottom to anchors to specific precomposed characters, 
    to support 'mark' attached for needed combinations not precomposed.

    Initial scope: "Ṝ ṝ Ḹ ḹ" for https://github.com/arrowtype/recursive/issues/367

    Assumptions:
    - You are only adding "top" anchors
    - You are only adding top anchors to precomposed glyphs with bottom accents (glyphsToAddAnchorsTo)
    - Glyphs aren’t nested more than two levels deep
"""

from vanilla.dialogs import *
from mojo.UI import AskYesNoCancel

files = getFile("Select files to add anchors in", allowsMultipleSelection=True, fileTypes=["ufo"])

saveAndClose = AskYesNoCancel("Save & close fonts after adding anchors?")


glyphsToAddAnchorsTo = "Ldotbelow Rdotbelow ldotbelow rdotbelow ldotbelow.italic rdotbelow.italic ldotbelow.mono rdotbelow.mono ldotbelow.simple rdotbelow.simple Ldotbelow.sans ldotbelow.sans".split(" ")


for file in files:
    if saveAndClose == 1:
        font = OpenFont(file, showInterface=False)
    elif saveAndClose == 0:
        font = OpenFont(file, showInterface=True)

    print()
    print(font.info.familyName, font.info.styleName)

    # the main thing
    for glyphName in glyphsToAddAnchorsTo:

        # find main base of precomposed glyph
        mainBase = [c.baseGlyph for c in font[glyphName].components if font[c.baseGlyph].width > 0][0]

        try:
            # get "top" anchor position of main base
            topAnchorPosition = [(a.x, a.y) for a in font[mainBase].anchors if a.name == "top"][0]

            # print()
            # print(mainBase, font[mainBase].anchors)
            # print(topAnchorPosition)

        # if glyphs are nested components, do it again
        except IndexError:
            realMainBase = [c.baseGlyph for c in font[mainBase].components if font[c.baseGlyph].width > 0][0]
            topAnchorPosition = [(a.x, a.y) for a in font[realMainBase].anchors if a.name == "top"][0]

            # print()
            # print("-> Going DEEPER")
            # print(mainBase, font[mainBase].anchors)
            # print(topAnchorPosition)


        if "top" not in [a.name for a in font[glyphName].anchors]:

            # add "top" anchor at that position in dotbelow glyph
            font[glyphName].appendAnchor("top",topAnchorPosition)
            print(f"anchor appended to {glyphName} at {topAnchorPosition}")


    if saveAndClose == 1:
        font.save()
        font.close()
