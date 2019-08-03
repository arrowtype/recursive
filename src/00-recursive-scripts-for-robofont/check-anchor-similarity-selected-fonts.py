from vanilla.dialogs import *
import os
from mojo.UI import AskString
from mojo.UI import OutputWindow
import pprint

files = getFile("Select files to update", allowsMultipleSelection=True, fileTypes=["ufo"])

fonts = []
anchors = {}

OutputWindow().show()

for file in files:
    font = OpenFont(file, showInterface=False)

    fontName = font.info.familyName + " " + font.info.styleName

    fonts.append(fontName)
    print(fontName)

    for glyph in font:
        print(glyph.name)
        for anchor in glyph.anchors:

            # if the anchor doesn't yet have an entry, make one
            if anchor.name not in anchors:
                anchors[anchor.name] = {}

            # if the glyph doesn't yet have an entry in this anchor, make one
            if glyph.name not in anchors[anchor.name]:
                anchors[anchor.name][glyph.name] = []

            anchors[anchor.name][glyph.name].append(fontName)

    font.close()

# uncomment to see full dictionary printed
# pp = pprint.PrettyPrinter(indent=2, width=200)
# pp.pprint(anchors)

# if a font is *missing* from an anchor glyph entry, report it as missing that anchor for that glyph
for anchor in anchors:
    for glyph in anchors[anchor]:
        if len(anchors[anchor][glyph]) < len(fonts):
            print(f"{anchor}")
            print(f"\t Glyph /{glyph} only has {anchor} in {anchors[anchor][glyph]}")
            print("")
