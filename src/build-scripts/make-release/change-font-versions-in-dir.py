"""
    A script to change the version of a font binary.

    For use on pre-prepped directory, e.g. `fonts_1.050`.

    → Changes font versions in `head` and `name` tables
    → Updates version numbers in paths

    Would have to handle OTC/TTC collections to work in entire release dir.

    USAGE:

    python3 src/build-scripts/make-release/change-font-versions-in-dir.py <font_dir_path> <version>

    ...where <version> is a number in the format of "1.054"

    WARNING:
    - Doesn’t currently work if the manually-set oldVersion ends in a "0" :|
    - Assumes version numbers will match in head table, plus names 3 & 5
    - has option arg from --oldVersion, but it is a bit inconsistent. Check outputs carefully!
"""

from fontTools.ttLib import TTFont
import math
import fire
import os

# GET / SET NAME HELPER FUNCTIONS

def getFontNameID(font, ID, platformID=3, platEncID=1):
    name = str(font['name'].getName(ID, platformID, platEncID))
    return name

def setFontNameID(font, ID, newName):
    
    print(f"\n\t• name {ID}:")
    macIDs = {"platformID": 3, "platEncID": 1, "langID": 0x409}
    winIDs = {"platformID": 1, "platEncID": 0, "langID": 0x0}

    oldMacName = font['name'].getName(ID, *macIDs.values())
    oldWinName = font['name'].getName(ID, *winIDs.values())

    if oldMacName != newName:
        print(f"\n\t\t Mac name was '{oldMacName}'")
        font['name'].setName(newName, ID, *macIDs.values())
        print(f"\n\t\t Mac name now '{newName}'")

    if oldWinName != newName:
        print(f"\n\t\t Win name was '{oldWinName}'")
        font['name'].setName(newName, ID, *winIDs.values())
        print(f"\n\t\t Win name now '{newName}'")

# MAIN FUNCTION

def changeVersion(fontPath, newVersion, oldVersion=""):
# def changeVersion(fontPath):
    font = TTFont(fontPath)

    if oldVersion == "":
        oldVersion = str(font['head'].fontRevision)[0:5]
    else:
        oldVersion = str(oldVersion)

    oldVersion = oldVersion.ljust(5, "0")

    print()
    print('oldVersion:', oldVersion)

    font['head'].fontRevision = newVersion

    print('head version now ', font['head'].fontRevision)

    # update name 3 – 1.050;ARRW;Recursive-SansLinearLight
    oldName3 = getFontNameID(font, 3)
    setFontNameID(font, 3, oldName3.replace(oldVersion, str(newVersion)))

    # update name 5 – Version 1.050
    print()
    print('Name 5:', getFontNameID(font, 5))
    print(newVersion)
    oldName5 = getFontNameID(font, 5)
    setFontNameID(font, 5, oldName5.replace(f"Version {oldVersion}", f"Version {str(newVersion)}"))

    if oldVersion != newVersion:
        # this logic is messed up ... 
        try:
            savePath = fontPath.replace(str(oldVersion), str(newVersion))
            font.save(savePath)
        except:
            savePath = fontPath.replace(str(oldVersion), str(newVersion))
            font.save(fontPath)
            print(f"Font version: {oldVersion} → {newVersion}")

def changeVersionsInDir(directory, newVersion, oldVersion=""):
    for root, dirs, files in os.walk(directory):
        for file in files:
            extension = file.split(".")[-1]
            if extension in ["ttf","otf","woff2"]:
                fontPath = os.path.join(root, file)

                changeVersion(fontPath, newVersion, oldVersion)


if __name__ == '__main__':
    # fire.Fire(changeVersion)
    fire.Fire(changeVersionsInDir)