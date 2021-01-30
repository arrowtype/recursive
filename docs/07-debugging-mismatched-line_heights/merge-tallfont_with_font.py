"""
    Script to include a "tall font" with other fonts, to then test the effect of max glyph dimension on line height.

    For more details, see https://github.com/arrowtype/recursive/issues/308

    USAGE:

    python merge-font-and-tallfont.py <tall_font_path> <normal_font_path>
"""

import argparse
from fontTools.merge import Merger
from fontTools.ttLib import TTFont


def getFontNameID(font, ID, platformID=3, platEncID=1):
    name = str(font['name'].getName(ID, platformID, platEncID))
    return name


def setFontNameID(font, ID, newName, platformID=3, platEncID=1, langID=0x409):
    print(f"\n\t• name {ID}:")
    oldName = font['name'].getName(ID, platformID, platEncID)
    print(f"\n\t\t was '{oldName}'")
    font['name'].setName(newName, ID, platformID, platEncID, langID)
    print(f"\n\t\t now '{newName}'")


def mergeTwoFonts(fontpath, tallfont, saveTo):
    merged = Merger().merge([fontpath, tallfont])
    merged.save(saveTo)


parser = argparse.ArgumentParser(description='Merge font A with font B')

parser.add_argument('-t', '--tallfont')
parser.add_argument('fonts', nargs="+")


def main():
    args = parser.parse_args()

    for font_path in args.fonts:
        print(font_path)
        print(args.tallfont)

        saveTo = font_path.replace("Recursive","RecTest")
        mergeTwoFonts(font_path, args.tallfont, saveTo)

        font = TTFont(saveTo)
        name1 = getFontNameID(font, 1).replace("Recursive","RecTest")
        name3 = getFontNameID(font, 3).replace("Recursive","RecTest")
        name4 = getFontNameID(font, 4).replace("Recursive","RecTest")
        name6 = getFontNameID(font, 6).replace("Recursive","RecTest")
        name16 = getFontNameID(font, 16).replace("Recursive","RecTest")

        setFontNameID(font, 1, name1)
        setFontNameID(font, 3, name3)
        setFontNameID(font, 4, name4)
        setFontNameID(font, 6, name6)
        setFontNameID(font, 16, name16)

        if font["OS/2"].usWeightClass == 400:
            setFontNameID(font, 2, "Regular")
            setFontNameID(font, 17, "Regular")
        if font["OS/2"].usWeightClass == 700:
            setFontNameID(font, 2, "Bold")
            setFontNameID(font, 17, "Bold")

        font["OS/2"].yMin = -500
        font["OS/2"].yMax = 1300

        font.save(saveTo)


if __name__ == '__main__':
    main()
