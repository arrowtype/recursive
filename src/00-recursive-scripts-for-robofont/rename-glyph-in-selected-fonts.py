# a script to find glyphs with unicode names and give them human-readable names
# started from https://forum.robofont.com/topic/624/renaming-the-glyph-problem/6

import pprint

from glyphNameFormatter.reader import u2n, n2u, u2U
from vanilla.dialogs import *


def updateGlyphName(f):
    f.features.text = feaText


def getNameFromUnicode(g):
    name = u2n(g.unicode)
    return name


def getReadableNames(font):
    renamingDict = {}
    for glyph in font:
        old_name = glyph.name

        if "uni" in old_name:  # and "." not in old_name:
            new_name = getNameFromUnicode(glyph)

            print(old_name, "\t\t\t", new_name)
            print("---------------------------------")

            if new_name is None:
                continue
            else:
                if new_name not in renamingDict.keys():
                    if new_name != old_name:
                        renamingDict[old_name] = new_name
                    for glyph2 in font:
                        if glyph2.name.split(".")[0] == old_name:
                            old_name2 = glyph2.name
                            new_name2 = glyph2.name.replace(old_name, new_name)
                            if new_name2 not in renamingDict.keys():
                                if new_name2 != old_name2:
                                    renamingDict[old_name2] = new_name2
    pprint.pprint(renamingDict)
    renamingDictKeys = list(renamingDict.keys())

    for old in reversed(renamingDictKeys):
        print(old)
        if old in font.keys():
            glyph = font[old]
            if len(glyph.contours) != 0:
                font.renameGlyph(old, renamingDict[old])
                print("\t", old, "→", renamingDict[old])
                for glyph2 in font:
                    for comp in glyph2.components:
                        if comp.baseGlyph == old:
                            comp.baseGlyph = renamingDict[old]

    #             # del renamingDict[old]
                print(old)
                renamingDictKeys.remove(old)

    print(renamingDictKeys)

    for old in reversed(renamingDictKeys):
        glyph = font[old]
        if len(glyph.contours) == 0:

            font.renameGlyph(old, renamingDict[old])
            print(old, "\t\t\t→", renamingDict[old])
            for glyph2 in font:
                for comp in glyph2.components:
                    if comp.baseGlyph == old:
                        comp.baseGlyph = renamingDict[old]


# getReadableNames(CurrentFont())

inputFonts = getFile(
    "select UFOs", allowsMultipleSelection=True, fileTypes=["ufo"])

for fontPath in inputFonts:
    f = OpenFont(fontPath, showInterface=True)

    getReadableNames(f)

#     # f.save()
#     # f.close()
