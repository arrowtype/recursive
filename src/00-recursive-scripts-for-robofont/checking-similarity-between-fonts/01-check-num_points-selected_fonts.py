from vanilla.dialogs import *
from mojo.UI import AskString
from mojo.UI import OutputWindow
import pprint

# TODO: ignore glyphs marked as "experimental" with robofont marx
# TODO: allow user to paste space-separated string of glyphs to limit check to

### SET THIS TO IGNORE GLYPHS YOU WANT TO LEAVE ALONE (e.g. experimental glyphs) ###

glyphsToIgnore = "R.trap Z.noserif ampersand.code_experimental_2 ampersand.code_experimental_3 ampersand.crossbar at.simple at.short at.replaced_with_prop dagger.daggery g.extra g.long_desc g.longtail g.ss01 onehalf.v1 perthousand r.simple_italic sterling.replaced_with_flat two.replaced_with_rounder zero.ss01 one.flatflag"

####################################################################################


files = getFile("Select files to check for anchor similarity", allowsMultipleSelection=True, fileTypes=["ufo"])

fonts = []
pointsDict = {}

OutputWindow().show()
OutputWindow().clear()

print("\nCOMPATIBILITY CHECK: GLYPH CONSISTENCY & POINT COUNTS\n\n")

print("""\
    📊 Emoji are present to help you spot point number differences more quickly. 
    Specific emoji have no meaning as to which numbers are correct or incorrect.
    The first count will be marked with 🍇, the next with 🍋, and so on.\n
""")

for file in files:
    font = OpenFont(file, showInterface=False)

    # fontName = (font.info.styleName).transl ate({ord(c): None for c in 'aeiou'}) # remove vowels to shorten
    fontName = (font.info.styleName)

    fonts.append(fontName)

    for glyph in font:
        if glyph.name not in pointsDict:
            pointsDict[glyph.name] = {}
        
        if fontName not in pointsDict[glyph.name]:
            pointsDict[glyph.name][fontName] = 0


        for c in glyph:
            for seg in c:
                for pt in seg:
                    # if the anchor doesn't yet have an entry, make one
                    pointsDict[glyph.name][fontName] += 1

    font.close()

print("Checking fonts:")
for fontName in fonts:
    print("• ", fontName)
print("")

# uncomment below to see full dictionary printed
# pp = pprint.PrettyPrinter(indent=2, width=200)
# pp.pprint(pointsDict)

glyphsNotInAllFonts = []

for glyphName in pointsDict.keys():
    if len(pointsDict[glyphName]) < len(fonts):
        if glyphName not in glyphsNotInAllFonts and glyphName not in glyphsToIgnore.split(" "):
            glyphsNotInAllFonts.append(glyphName)

glyphsWithUnevenPoints = []

for glyphName in pointsDict.keys():
    if len(set(pointsDict[glyphName].values())) > 1:
        if glyphName not in glyphsWithUnevenPoints and glyphName not in glyphsToIgnore.split(" "):
            glyphsWithUnevenPoints.append(glyphName)
            
maxFontNameLength = len(max(fonts, key=len))


alertEmoji = "🍇 🍋 🍉 🍊 🥑 🍑 🍌 🍒 🌽 🍈 🐶 🐱 🐭 🐰 🦊 🐻 🐯 🦁 🐮 🐷 🐸 🐵 🐔 🐣".split(" ")
iconDict = {}

for glyphName in sorted(glyphsWithUnevenPoints):
    iconDict[glyphName] = {}
    # for font with this glyph
    for fontName in pointsDict[glyphName].keys():
        # if glyph point count not already in icon dict under glyph
        if pointsDict[glyphName][fontName] not in iconDict[glyphName].keys():
            count  = str(pointsDict[glyphName][fontName])
            iconDict[glyphName][count] = ""

    # go through each glyph:font combo in iconDict and assing emoji to diff counts
    for index,pointCount in enumerate(iconDict[glyphName].keys()):
        iconDict[glyphName][pointCount] = alertEmoji[index]

# pp = pprint.PrettyPrinter(indent=2, width=200)
# pp.pprint(iconDict)

problemGlyphs = glyphsNotInAllFonts + glyphsWithUnevenPoints

for glyphName in sorted(problemGlyphs):
    print("\n--------------------------------------------------------------\n")
    print(f"{glyphName}\n")

    # If glyph has different point counts in different fonts, report
    # if len(set(pointsDict[glyphName].keys())) != 1:
    if glyphName in glyphsWithUnevenPoints:

        print(f"\t{'Font'.ljust(maxFontNameLength + 1)} |  Pts | 📊") # add contour count? segment count?
        print(f"\t{''.ljust(maxFontNameLength + 1, '-')} | ---- | --")

        for fontName in pointsDict[glyphName].keys():
            
            pointCount = str(pointsDict[glyphName][fontName])
            print(f"\t{fontName.ljust(maxFontNameLength + 1)} | {str(pointsDict[glyphName][fontName]).rjust(4)} | {iconDict[glyphName][pointCount]}")
            
        print("")

    # If glyph is not in all fonts, report
    # if len(pointsDict[glyphName]) != len(fonts):
    if glyphName in glyphsNotInAllFonts:
        # print("\tGlyph is not in all fonts.\n")
        print("\tIs in:\n\t------------------")
        for fontName in sorted(fonts):
            if fontName in pointsDict[glyphName]:
                print("\t",fontName)
        
        print("\n")

        print("\tNot in:\n\t------------------")
        for fontName in sorted(fonts):
            if fontName not in pointsDict[glyphName]:
                print("\t",fontName)

if len(glyphsWithUnevenPoints) >= 1:
    print("️\n\nGlyphs with unequal points between fonts:")
    print("\t", end=" ")
    for glyphName in sorted(glyphsWithUnevenPoints):
        # print(" - [ ] ", glyphName)
        print(glyphName, end=" ")
    print("")


if len(glyphsNotInAllFonts) >= 1:
    print("\n\nGlyphs that aren't in all fonts:")
    print("\t", end=" ")
    for glyphName in sorted(glyphsNotInAllFonts):
        # print(" - [ ] ", glyphName)
        print(glyphName, end=" ")
    print("")

if len(problemGlyphs) is 0:
    print("🤖🤖🤖\n")
    print("Looks like all glyphs have the same anchors – nice work! \n")
    print("🎉🎉🎉\n")


if glyphsToIgnore is not "" and len(glyphsToIgnore.split(" ")) > 0:
    print("\n--------------------------------------------------------------\n")
    print("NOTE: ignored the following glyphs (they are experiments or currently low-priority)")
    print("(edit script to adjust these)")
    for name in glyphsToIgnore.split(" "):
        print(name, end=" ")

print("\n")