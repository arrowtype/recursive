"""
    Add `caret` anchors to ligature glyphs with approximate placement.

    USAGE:

    Run in RoboFont, then select UFOs to automatically add ligature carets to. 

    Positioning should be manually checked/fixed afterwards (if the ligatures aren’t just composed from the base glyphs).
"""

from vanilla.dialogs import *

# name ligatures to look for
ligatures = [
    "f_f",
    "fi",
    "fl",
    "f_f_i",
    "f_f_l",
    "f_f.italic",
    "f_f_i.italic",
    "f_f_l.italic",
    "fi.italic",
    "fl.italic",
    "f_f.mono",
    "f_f_i.mono",
    "f_f_l.mono",
    "fi.mono",
    "fl.mono",
]

# get files
files = getFile("Select files to modify", allowsMultipleSelection=True, fileTypes=["ufo"])

for file in files:
    font = OpenFont(file, showInterface=False)

    print("\n\n--------------------------------------------------\n")
    print(font.info.styleName)

    for glyphName in font.keys():
        if glyphName in ligatures:

            print()
            print(glyphName)

            g = font[glyphName]

            simpleName = glyphName.replace("_","").replace(".italic","").replace(".mono","")

            widthCounter = 0
            for index, charName in enumerate(simpleName):
                # do this one less time than the full length
                if index != len(simpleName) - 1 and f"caret_{index+1}" not in [a.name for a in g.anchors]:
                    widthCounter += font[charName].width
                    g.appendAnchor(f"caret_{index+1}", (widthCounter,0))
                    print(f"added anchor 'caret_{index+1}' at x={widthCounter}" )

        if ".code" in glyphName:
            print()
            print(glyphName)

            g = font[glyphName]
            simpleName = glyphName.split(".")[0]

            # split these by underscores
            partNames = simpleName.split("_")

            widthCounter = 0
            for index, charName in enumerate(partNames):
                # do this one less time than the full length
                if index != len(partNames) - 1 and f"caret_{index+1}" not in [a.name for a in g.anchors]:
                    # these are monospaced, so it works best to just set carets at the spacing unit
                    widthCounter += 600
                    g.appendAnchor(f"caret_{index+1}", (widthCounter,0))
                    print(f"added anchor 'caret_{index+1}' at x={widthCounter}" )

    font.save()
    font.close()
