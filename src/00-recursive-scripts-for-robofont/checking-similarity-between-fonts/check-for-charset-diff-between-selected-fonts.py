from vanilla.dialogs import *
from mojo.UI import AskString
from mojo.UI import OutputWindow
import pprint


### SET THIS TO IGNORE GLYPHS YOU WANT TO LEAVE ALONE (e.g. experimental glyphs) ###

glyphsToIgnore = ""

####################################################################################


files = getFile("Select files to check for character set similarity", allowsMultipleSelection=True, fileTypes=["ufo"])

fonts = []
glyphs = {}

OutputWindow().show()
OutputWindow().clear()

for file in files:
    font = OpenFont(file, showInterface=False)

    fontName = font.info.familyName + " " + font.info.styleName

    fonts.append(fontName)

    for glyph in font:

        # if the glpyh doesn't yet have an entry, make one
        if glyph.name not in glyphs:
            glyphs[glyph.name] = []

        # if the glyph doesn't yet have an entry in this anchor, make one
        if fontName not in glyphs[glyph.name]:
            glyphs[glyph.name].append(fontName)

    font.close()

print("Checking fonts:")
for fontName in fonts:
    print("• ", fontName)
print("")

# uncomment below to see full dictionary printed
# pp = pprint.PrettyPrinter(indent=2, width=200)
# pp.pprint(glyphs)

# problemGlyphs = []

# for glyphName in glyphs.keys():
#     if len(glyphs[glyph.name]) < len(fonts):
#         if glyphName not in problemGlyphs and glyphName not in glyphsToIgnore.split(" "):
#             problemGlyphs.append(glyphName)

# print(sorted(problemGlyphs))

## if you want to check specific glyphs, add them here as a space-separated list
problemGlyphs = "i.mono l.mono f.mono r.mono l.sans f.italic r.italic i.italic l.italic fl.mono fl.sans".split(" ")



for glyphName in sorted(problemGlyphs):
    print("--------------------------------------------------------------\n")

    print(f"## {glyphName}")
    if len(glyphs[glyphName]) < len(fonts):
        print(f"- [ ] /{glyphName} is in:")
        for fontName in sorted(fonts):
            if fontName in glyphs[glyphName]:
                print(f"- {fontName}")

        print("")
        print(f"...but not in:")
        for fontName in sorted(fonts):
            if fontName not in glyphs[glyphName]:
                print(f"  - [ ] {fontName}")
        print("")

if len(problemGlyphs) is 0:
    print("🤖🤖🤖\n")
    print("Looks like all fonts have similar character sets – nice work! \n")
    print("🎉🎉🎉\n")

if len(glyphsToIgnore) > 0:
    print("--------------------------------------------------------------")
    print("NOTE: ignored the following glyphs (edit script to adjust this)")
    for name in glyphsToIgnore.split(" "):
        print("• ", name)
