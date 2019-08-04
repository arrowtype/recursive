from vanilla.dialogs import *
import os
from mojo.UI import AskString
from mojo.UI import OutputWindow
import pprint


### SET THIS TO IGNORE GLYPHS YOU WANT TO LEAVE ALONE (e.g. experimental glyphs) ###

glyphsToIgnore = "L.noserif N.tighttaper R.trap"

####################################################################################


files = getFile("Select files to check for anchor similarity", allowsMultipleSelection=True, fileTypes=["ufo"])

fonts = []
anchors = {}

OutputWindow().show()
OutputWindow().clear()

for file in files:
    font = OpenFont(file, showInterface=False)

    fontName = font.info.familyName + " " + font.info.styleName

    fonts.append(fontName)

    for glyph in font:
        for anchor in glyph.anchors:

            # if the anchor doesn't yet have an entry, make one
            if anchor.name not in anchors:
                anchors[anchor.name] = {}

            # if the glyph doesn't yet have an entry in this anchor, make one
            if glyph.name not in anchors[anchor.name]:
                anchors[anchor.name][glyph.name] = []

            anchors[anchor.name][glyph.name].append(fontName)

    font.close()

## uncomment below to see full dictionary printed
# pp = pprint.PrettyPrinter(indent=2, width=200)
# pp.pprint(anchors)

problemGlyphs = []

for anchor in anchors:
    for glyphName in anchors[anchor]:
        if len(anchors[anchor][glyphName]) < len(fonts):
            if glyphName not in problemGlyphs and glyphName not in glyphsToIgnore.split(" "):
                problemGlyphs.append(glyphName)



for glyphName in sorted(problemGlyphs):
    print("--------------------------------------------------------------")
    print(f"{glyphName}\n")
    for anchor in sorted(anchors.keys()):
        if glyphName in anchors[anchor]:
            if len(anchors[anchor][glyphName]) < len(fonts):
                print(f"\t /{glyphName} has '{anchor}' in:")
                for fontName in fonts:
                    # if glyphName in anchors[anchor]:
                    if fontName in anchors[anchor][glyphName]:
                        print(f"\t\t • {fontName}")

                print("")
                print(f"\t\t ...but not in:")
                for fontName in fonts:
                    # if glyphName in anchors[anchor]:
                    if fontName not in anchors[anchor][glyphName]:
                        print(f"\t\t\t • {fontName}")
                print("")

print("--------------------------------------------------------------")
print("NOTE: ignored the following glyphs (edit script to adjust this)")
for name in glyphsToIgnore.split(" "):
    print("• ", name)

# # if a font is *missing* from an anchor glyph entry, report it as missing that anchor for that glyph
# for anchor in anchors:
#     print("--------------------------------------------------------------")
#     print("--------------------------------------------------------------")
#     print(f"{anchor}")
#     for glyph in anchors[anchor]:
#         if len(anchors[anchor][glyph]) < len(fonts):
#             # print(f"\t Glyph /{glyph} only has {anchor} in {anchors[anchor][glyph]}")
#             print(f"\t Glyph /{glyph} has anchor '{anchor}' in:")
#             for fontName in fonts:
#                 if fontName in anchors[anchor][glyph]:
#                     print(f"\t • {fontName}")

#             print("")
#             print(f"\t ...but not in:")
#             for fontName in fonts:
#                 if fontName not in anchors[anchor][glyph]:
#                     print(f"\t • {fontName}")
#             print("")


#             print("")

#     print("--------------------------------------------------------------\n")
