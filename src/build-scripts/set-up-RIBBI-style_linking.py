

'''

    :/ DOES NOT YET WORK

    Attempt to make Reg-Ital-Bold-BoldItal styles link properly in apps like Word and VS Code

        # if " Bold Itacic" in name 1
        # nameID 1.replace(" Bold Italic","")
        # change nameID 2 to "Bold Italic"

        # if " Bold" in name 1
        # nameID 1.replace(" Bold","")
        # change nameID 2 to "Bold"

        # if "Italic" in nameID 1
        # nameID 1.replace(" Italic","")
        # change nameID 2 to "Italic"

    To use:

    0. You must have FontTools installed
    1. Include a file at the root of your type project, called "version.txt"
    2. In "version.txt," have only a version number, like "1.014" or "Beta 1.014" (just the version string, without quotes)
    3. In your terminal, go to the base of the font project. Run this script, and add a path or paths to fonts as an argument, e.g.:

        python <path>/set-up-RIBBI-style_linking.py <path>/<font>.ttf

'''

import os
import argparse
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


# PARSE ARGUMENTS

parser = argparse.ArgumentParser(description='Set name ID 2 to allow RIBBI style linking')

parser.add_argument('fonts', nargs="+")

parser.add_argument(
        "-i",
        "--inplace",
        action='store_true',
        help="Edit fonts and save under the same filepath, without an added suffix.",
    )


def main():
    args = parser.parse_args()

    for font_path in args.fonts:
        print("\n-----------------------------------------\n")
        print(font_path)
        ttfont = TTFont(font_path)

        # UPDATE NAME ID 16, typographic family name
        famName = getFontNameID(ttfont, 1)

        newFamName = famName

        # To Try: remove "Linear" and version number, for just "Recursive Mono" and "Recursive Sans"?

        if " Bold Italic" in famName:
            newFamName = famName.replace(" Bold Italic","")
            setFontNameID(ttfont, 2, "Bold Italic")
            setFontNameID(ttfont, 1, newFamName)
            setFontNameID(ttfont, 4, newFamName)

        if " Bold" in famName and " Bold Italic" not in famName:
            newFamName = famName.replace(" Bold","")
            setFontNameID(ttfont, 2, "Bold")
            setFontNameID(ttfont, 1, newFamName)
            setFontNameID(ttfont, 4, newFamName)

        if " Regular" in famName and " Italic" not in famName:
            newFamName = famName.replace(" Regular","")
            setFontNameID(ttfont, 2, "Regular")
            setFontNameID(ttfont, 1, newFamName)
            setFontNameID(ttfont, 4, newFamName)

        if " Italic" in famName and " Bold" not in famName and " Regular" not in famName:
            newFamName = famName.replace(" Italic","")
            setFontNameID(ttfont, 2, "Italic")
            setFontNameID(ttfont, 1, newFamName)
            setFontNameID(ttfont, 4, newFamName)

        # UPDATE BASIC FONT NAME, id 1
        

        # SAVE FONT
        if args.inplace:
            ttfont.save(font_path)
        else:
            if '.ttf' in font_path:
                ttfont.save(font_path.replace(r'.ttf','.fix.ttf'))
            elif '.otf' in font_path:
                ttfont.save(font_path.replace(r'.otf','.fix.otf'))


if __name__ == '__main__':
    main()
