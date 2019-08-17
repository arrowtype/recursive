'''

    Font versions often clash in software. The simplest way to avoid that is to add a version number to new fonts, e.g.

        "Recursive Mono Beta v1.014"

    ...but this can be annoying to add to new files. This script makes it simple. To use:

    0. You must have FontTools installed
    1. Include a file at the root of your type project, called "version.txt"
    2. In "version.txt," have only a version number, like "1.014" or "Beta 1.014" (just the version string, without quotes)
    3. In your terminal, go to the base of the font project. Run this script, and add a path or paths to fonts as an argument, e.g.:

        python <path>/set-versioned-font-names.py <path>/<font>.ttf

'''

import os
import argparse
from fontTools.ttLib import TTFont

def getVersion():
    with open("version.txt") as f:
        currentVersion = f.read()
        return currentVersion

def getFontNameID(font, ID, platformID=3, platEncID=1):
    name = str(font['name'].getName(ID, platformID, platEncID))
    return name

# setName(self, string, nameID, platformID, platEncID, langID)

def setFontNameID(font, ID, newName, platformID=3, platEncID=1, langID=0x409):
    print(f"\n\t• name {ID}:")
    oldName = font['name'].getName(ID, platformID, platEncID)
    print(f"\n\t\t was '{oldName}'")
    font['name'].setName(newName, ID, platformID, platEncID, langID)
    print(f"\n\t\t now '{newName}'")


# PARSE ARGUMENTS

parser = argparse.ArgumentParser(description='Print out nameID strings of the fonts')

parser.add_argument('fonts', nargs="+")

parser.add_argument(
        "-s",
        "--static",
        action='store_false',
        help="Is font static? If so, this will update its versions differently.",
    )  # xprn

NAME_IDS = {
    1: 'familyName',    # Recursive Sans Linear A
    3: 'uniqueID',      # 1.005;ARRW;RecursiveSans-LinearA
    4: 'fullName',      # Recursive Sans Linear A
    5: 'version',       # Version 1.005
    6: 'psName',        # RecursiveSans-LinearA
    16: 'typeFamily'    # Recursive Sans
}

# important for Name ID 6, which must be less than about 30 characters
NAME_ABBR = {
    'Beta': 'B',
    'Casual': 'Csl',
    'Linear': 'Lnr',
    'Italic': 'It',
    'Light': 'Lt',
    'Regular': 'Rg',
    'Medium': 'Md',
    'SemiBold': 'SBd',
    'Bold': 'Bd',
    'ExtraBold': 'XBd',
    'Black': 'Bk',
    'Heavy': 'Hv'
}

def main():
    args = parser.parse_args()
    projectVersion = getVersion()

    for font_path in args.fonts:
        ttfont = TTFont(font_path)

        if args.static is not None:
            print("NOTE: treating as a static font due to --static option")

        for nameID in NAME_IDS:
            print(f"{NAME_IDS[nameID].ljust(10)}: {getFontNameID(ttfont, nameID)}")

        # GET NAME ID 17, typographic style name, to use in name ID 6

        styleName = getFontNameID(ttfont, 17)
        styleNames = str(styleName).split(' ')

        # UPDATE NAME ID 16, typographic family name
        famName = getFontNameID(ttfont, 16)
        newFamName = f"{famName} {projectVersion}"

        setFontNameID(ttfont, 16, newFamName)

        # UPDATE NAME ID 6
        # replace last part of postScript font name, e.g. "LinearA" from "RecursiveMono-LinearA"

        if args.static is not None:
            psName = str(getFontNameID(ttfont, 6))
            # psStyle = psName.split("-")[-1]
            psFam = psName.split("-")[0]
            newPsName = psName.replace(psFam, f"{psFam}{projectVersion.replace(' ','').replace('1.','_')}")

            for word in styleNames:
                if word in NAME_ABBR.keys():
                    newPsName = newPsName.replace(word, NAME_ABBR[word])

            if 'Beta' in newPsName:
                newPsName = newPsName.replace('Beta', NAME_ABBR['Beta'])
        else:
            print("Variable font")
            psName = str(getFontNameID(ttfont, 6))
            psFam = psName.split("-")[0]
            newPsName = psName.replace(psFam, psFam + projectVersion.replace(' ','_').replace('.','_'))

        # set new ps name
        setFontNameID(ttfont, 6, newPsName)


        # VERSION, ID 5 (e.g. "Version 1.005")

        if "Beta" in projectVersion:
            newVersion = f"Version {projectVersion.replace('Beta ','')}"
        else:
            newVersion = f"Version {projectVersion}"

        setFontNameID(ttfont, 5, newVersion)

        # FULL FONT NAME, ID 4

        if args.static is not None:
            newFamName = newFamName + " " + styleName
            setFontNameID(ttfont, 4, newFamName)
        else:
            setFontNameID(ttfont, 4, newFamName)


        # UNIQUE FONT NAME, ID 3 (e.g. 1.005;ARRW;RecursiveSans-LinearA)

        oldUniqueID = str(getFontNameID(ttfont, 3))
        oldUniqueIDParts = oldUniqueID.split(";")
        newUniqueID = f"{projectVersion.replace('Beta ','')};{oldUniqueIDParts[1]};{newPsName}"
        setFontNameID(ttfont, 3, newUniqueID)

        # UPDATE BASIC FONT NAME, id 1
        setFontNameID(ttfont, 1, newFamName)

        # SAVE FONT
        ttfont.save(font_path + '.fix')


if __name__ == '__main__':
    main()