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

parser = argparse.ArgumentParser(description='Add version numbering to font name IDs')

parser.add_argument('fonts', nargs="+")

parser.add_argument(
        "-i",
        "--inplace",
        action='store_true',
        help="Edit fonts and save under the same filepath, without an added suffix.",
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

def abbreviateName(name, styleNames):
    # style names
    for word in styleNames:
        if word in NAME_ABBR.keys():
            name = name.replace(word, NAME_ABBR[word])
    # version name
    name=name.replace('Beta ', 'b')
    name=name.replace('1.','')

    return name

def main():
    args = parser.parse_args()
    projectVersion = getVersion()

    for font_path in args.fonts:

        # open font path as a font object, for manipulation
        ttfont = TTFont(font_path)

        # check for gvar table to see whether it's a variable font
        if 'gvar' not in ttfont.keys():
            fontIsStatic = True
            print("\n-------------------------------------------\nFont is static.")
        else:
            fontIsStatic = False
            print("\n-------------------------------------------\nFont is variable.")


        # GET NAME ID 17, typographic style name, to use in name ID 6
        styleName = getFontNameID(ttfont, 17)
        print(styleName)
        styleNames = str(styleName).split(' ')

        # UPDATE NAME ID 16, typographic family name
        famName = getFontNameID(ttfont, 16)

       
        newFamName = f"{famName} {projectVersion}st"
        newFamName = abbreviateName(newFamName, styleNames)
        setFontNameID(ttfont, 16, newFamName)

        

        

        # UPDATE NAME ID 6
        # replace last part of postScript font name, e.g. "LinearA" from "RecursiveMono-LinearA"

        if fontIsStatic:
            psName = str(getFontNameID(ttfont, 6))
            # psStyle = psName.split("-")[-1]
            psFam = psName.split("-")[0]
            newPsName = psName.replace(psFam, f"{psFam}{projectVersion.replace(' ','').replace('1.','')}st")

            if 'Beta' in newPsName:
                newPsName = newPsName.replace('Beta', NAME_ABBR['Beta'])

            newPsName = abbreviateName(newPsName, styleNames)
        else:
            print("Variable font")
            psName = str(getFontNameID(ttfont, 6))
            psFam = psName.split("-")[0]
            newPsName = psName.replace(psFam, psFam + projectVersion.replace(' ','').replace('1.',''))

        # set new ps name
        setFontNameID(ttfont, 6, newPsName)


        # VERSION, ID 5 (e.g. "Version 1.005")

        if "Beta" in projectVersion:
            newVersion = f"Version {projectVersion.replace('Beta ','')}"
        else:
            newVersion = f"Version {projectVersion}"

        setFontNameID(ttfont, 5, newVersion)

        # FULL FONT NAME, ID 4

        if fontIsStatic:

            newFamName = f"{famName} {projectVersion}st"

            newFamName = newFamName + ' ' + styleName
            styleName = styleName.replace('Linear ','').replace('Casual ','')

            # if 'Linear' in styleName:
            #     newFamName = newFamName + ' ' + styleName
            #     styleName = styleName.replace('Linear ','')

            # if 'Casual' in styleName:
            #     newFamName = newFamName + ' ' + styleName
            #     styleName = styleName.replace('Casual ','')

            newFamName = newFamName.replace(' Italic','').replace('Italic','')
        else:
            newFamName = f"{famName} {projectVersion}"

        newFamName = abbreviateName(newFamName, styleNames)

        if fontIsStatic:
            completeName = newFamName
            if 'Italic' in styleName:
                completeName = abbreviateName(newFamName + 'Italic', styleNames)
            setFontNameID(ttfont, 4, completeName)
        else:
            newFamName = abbreviateName(newFamName, styleNames)
            setFontNameID(ttfont, 4, newFamName)


        # UNIQUE FONT NAME, ID 3 (e.g. 1.005;ARRW;RecursiveSans-LinearA)

        oldUniqueID = str(getFontNameID(ttfont, 3))
        oldUniqueIDParts = oldUniqueID.split(";")
        newUniqueID = f"{projectVersion.replace('Beta ','')};{oldUniqueIDParts[1]};{newPsName}"
        setFontNameID(ttfont, 3, newUniqueID)

        # UPDATE BASIC FONT NAME, id 1

        legalStyleNames = ['Regular', 'Italic', 'Bold', 'Bold Italic']
        # TODO: 
        if styleName not in legalStyleNames and 'Italic' in styleName:
            styleName = 'Italic'
        if styleName not in legalStyleNames and 'Italic' not in styleName:
            styleName = 'Regular'

        setFontNameID(ttfont, 2, styleName)
        setFontNameID(ttfont, 1, newFamName)

        # SAVE FONT
        if args.inplace:
            ttfont.save(font_path)
        else:
            ttfont.save(font_path + '.fix')


if __name__ == '__main__':
    main()
