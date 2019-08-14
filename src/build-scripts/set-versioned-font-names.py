# intended specificall for variable font files

import os
import argparse
from fontTools.ttLib import TTFont

def getVersion():
    with open("version.txt") as f:
        currentVersion = f.read()
        return currentVersion

def getFontNameID(font, ID, platformID=3, platEncID=1):
    name = font['name'].getName(ID, platformID, platEncID)
    return name

# setName(self, string, nameID, platformID, platEncID, langID)

def setFontNameID(font, ID, newName, platformID=3, platEncID=1, langID=0x409):

    oldName = font['name'].getName(ID, platformID, platEncID)
    font['name'].setName(newName, ID, platformID, platEncID, langID)


    print(f"\n\t• name {ID}: '{oldName}' → '{newName}'")



parser = argparse.ArgumentParser(description='Print out nameID strings of the fonts')

parser.add_argument('fonts', nargs="+")

# parser.add_argument('--id', '-i', default='all')

namesToVersion = {
    1
}

NAME_IDS = {
    1: 'familyName',    # Recursive Sans Linear A
    3: 'uniqueID',      # 1.005;ARRW;RecursiveSans-LinearA
    4: 'fullName',      # Recursive Sans Linear A
    5: 'version',       # Version 1.005
    6: 'psName',        # RecursiveSans-LinearA
    16: 'typeFamily'    # Recursive Sans
}

def main():
    args = parser.parse_args()
    projectVersion = getVersion()

    for font_path in args.fonts:
        ttfont = TTFont(font_path)

        for nameID in NAME_IDS:
            print(f"{NAME_IDS[nameID].ljust(10)}: {getFontNameID(ttfont, nameID)}")

        # Update typographic family name
        famName = getFontNameID(ttfont, 16)
        newFamName = f"{famName} Beta {projectVersion}"

        setFontNameID(ttfont, 16, newFamName)

        # UPDATE NAME ID 6
        # replace last part of postScript font name, e.g. "LinearA" from "RecursiveMono-LinearA"
        psName = str(getFontNameID(ttfont, 6))
        psStyle = psName.split("-")[-1]
        newPsName = psName.replace(psStyle, f"Beta_{projectVersion.replace('.','_')}")
        # set new ps name
        setFontNameID(ttfont, 6, newPsName)

        # VERSION, ID 5 (e.g. "Version 1.005")

        newVersion = f"Version {projectVersion}"

        setFontNameID(ttfont, 5, newVersion)

        # FULL FONT NAME, ID 4

        setFontNameID(ttfont, 4, newFamName)

        # UNIQUE FONT NAME, ID 3 (e.g. 1.005;ARRW;RecursiveSans-LinearA)

        oldUniqueID = str(getFontNameID(ttfont, 3))
        oldUniqueIDParts = oldUniqueID.split(";")
        newUniqueID = f"{projectVersion};{oldUniqueIDParts[1]};{newPsName}"
        setFontNameID(ttfont, 3, newUniqueID)

        # UPDATE BASIC FONT NAME, id 1
        setFontNameID(ttfont, 1, newFamName)

        # SAVE FONT
        ttfont.save(font_path + '.fix')


if __name__ == '__main__':
    main()