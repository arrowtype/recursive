from vanilla.dialogs import *
from mojo.UI import AskString
from mojo.UI import OutputWindow
import pprint

# TODO: ignore glyphs marked as "experimental" with robofont marx
# TODO: allow user to paste space-separated string of glyphs to limit check to

### SET THIS TO IGNORE GLYPHS YOU WANT TO LEAVE ALONE (e.g. experimental glyphs) ###

glyphsToIgnore = "L.noserif Z.noserif .contrast-circles ampersand.code_experimental ampersand.code_experimental_2 ampersand.code_experimental_3 ampersand.crossbar at.monolinear at.replaced_with_prop at.short braceleft.asymmetrical dagger.daggery dollar.lower g.compact_desc g.extra g.ss01 hyphen.simple one.flatflag r.simple_italic zero.ss01 y.longtail two.replaced_with_rounder sterling.replaced_with_flat onehalf.v1 l.ss01 R.trap a.italic_curl ampersand_ampersand.code at.prop at.simple  braceright.asymmetrical divisionslash.copy_1 exclam.copy_1 g.long_desc g.longtail i.ss01 j.longtail fi fj fl fl.mono" 

# save these soon: fi fj fl fl.mono

####################################################################################

debug = False # will print full dictionaries

widthUnit = AskString('Width unit to check for (e.g. 600, 50, 10)')

files = getFile(f"Select files to check glyph widths for units of {widthUnit}", allowsMultipleSelection=True, fileTypes=["ufo"])

fonts = []
widthsDict = {}
badWidthGlyphs = {}

OutputWindow().show()
OutputWindow().clear()

print("\nCOMPATIBILITY CHECK: GLYPH CONSISTENCY & WIDTHS\n\n")

print("""\
    📊 Emoji are present to help you spot width differences more quickly. 
    Specific emoji have no meaning as to which widths are correct or incorrect.
    You must use your best judgement to decide, or file an issue/ask.
    The first count will be marked with 🍇, the next with 🥑, and so on.\n
""")




for file in files:
    font = OpenFont(file, showInterface=False)

    # fontName = (font.info.styleName).transl ate({ord(c): None for c in 'aeiou'}) # remove vowels to shorten
    fontName = (font.info.styleName)

    fonts.append(fontName)
    badWidthGlyphs[fontName] = {}

    for glyph in font:
        if glyph.width % int(widthUnit) != 0:
            badWidthGlyphs[fontName][glyph.name] = glyph.width
        if glyph.width < 0:
            print("\nNegative-width glyph:")
            print(fontName)
            print(f"{glyph.name} | {glyph.width}")

    for glyph in font:
        if glyph.name not in widthsDict:
            widthsDict[glyph.name] = {}
        
        if fontName not in widthsDict[glyph.name]:
            widthsDict[glyph.name][fontName] = 0

        widthsDict[glyph.name][fontName] = glyph.width

    font.close()

print("Checking fonts:")
for fontName in fonts:
    print("• ", fontName)
print("")

# --------------------------------------------------------------------

# check if there are problem-width glyphs, print to markdown-ready tables
for i in sorted(badWidthGlyphs.keys()):
    if len(badWidthGlyphs[i].keys()) != 0:
        print(f"\n### {i} – glyphs not in units of {widthUnit}\n")
        print(f"| {'**Glyph**'.ljust(20)} | **width** |")
        print(f"| {'-'.ljust(20,'-')} | {'-'.ljust(8,'-')}: |")
        for j in sorted(badWidthGlyphs[i].keys()):
            print(f"| {j.ljust(20)} | {str(badWidthGlyphs[i][j]).rjust(9)} |")

        print()


if debug:
    pp = pprint.PrettyPrinter(indent=2, width=200)
    print("bad width glyphs")
    pp.pprint(badWidthGlyphs)
    print("glyph widths")
    pp.pprint(widthsDict)

# --------------------------------------------------------------------

if debug:
    pp = pprint.PrettyPrinter(indent=2, width=200)
    pp.pprint(widthsDict)

glyphsNotInAllFonts = []

for glyphName in widthsDict.keys():
    if len(widthsDict[glyphName]) < len(fonts):
        if glyphName not in glyphsNotInAllFonts and glyphName not in glyphsToIgnore.split(" "):
            glyphsNotInAllFonts.append(glyphName)

glyphsWithUnevenWidths = []

for glyphName in widthsDict.keys():
    if len(set(widthsDict[glyphName].values())) > 1:
        if glyphName not in glyphsWithUnevenWidths and glyphName not in glyphsToIgnore.split(" "):
            glyphsWithUnevenWidths.append(glyphName)
            
maxFontNameLength = len(max(fonts, key=len))


alertEmoji = "🍇 🥑 🍉 🍊 🍒 🍑 🌽 🍈 🍌 🐶 🐱 🐭 🦊".split(" ")
iconDict = {}

for glyphName in sorted(glyphsWithUnevenWidths):
    iconDict[glyphName] = {}
    # for font with this glyph
    for fontName in widthsDict[glyphName].keys():
        # if glyph width count not already in icon dict under glyph
        if widthsDict[glyphName][fontName] not in iconDict[glyphName].keys():
            count  = str(widthsDict[glyphName][fontName])
            iconDict[glyphName][count] = ""

    # go through each glyph:font combo in iconDict and assing emoji to diff counts
    for index,width in enumerate(iconDict[glyphName].keys()):
        iconDict[glyphName][width] = alertEmoji[index]


if debug:
    pp = pprint.PrettyPrinter(indent=2, width=200)
    pp.pprint(iconDict)

problemGlyphs = glyphsNotInAllFonts + glyphsWithUnevenWidths

for glyphName in sorted(problemGlyphs):
    print("\n--------------------------------------------------------------\n")
    print(f"{glyphName}\n")

    # If glyph has different width counts in different fonts, report
    if glyphName in glyphsWithUnevenWidths:

        print(f"\t{'Font'.ljust(maxFontNameLength + 1)} | Wdth | 📊") # add contour count? segment count?
        print(f"\t{''.ljust(maxFontNameLength + 1, '-')} | ---- | --")

        for fontName in widthsDict[glyphName].keys():
            
            width = str(widthsDict[glyphName][fontName])
            print(f"\t{fontName.ljust(maxFontNameLength + 1)} | {str(widthsDict[glyphName][fontName]).rjust(4)} | {iconDict[glyphName][width]}")
            
        print("")

    # If glyph is not in all fonts, report
    if glyphName in glyphsNotInAllFonts:
        # print("\tGlyph is not in all fonts.\n")
        print("\tIs in:\n\t------------------")
        for fontName in sorted(fonts):
            if fontName in widthsDict[glyphName]:
                print("\t",fontName)
        
        print("\n")

        print("\tNot in:\n\t------------------")
        for fontName in sorted(fonts):
            if fontName not in widthsDict[glyphName]:
                print("\t",fontName)

if len(glyphsWithUnevenWidths) >= 1:
    print("️\n\nGlyphs with unequal widths between fonts:\n")
    print("\t", end=" ")
    for glyphName in sorted(glyphsWithUnevenWidths):
        # print(" - [ ] ", glyphName)
        print(glyphName, end=" ")
    print("")


if len(glyphsNotInAllFonts) >= 1:
    print("\n\nGlyphs that aren't in all fonts:\n")
    print("\t", end=" ")
    for glyphName in sorted(glyphsNotInAllFonts):
        # print(" - [ ] ", glyphName)
        print(glyphName, end=" ")
    print("")

if len(problemGlyphs) is 0:
    print("🤖🤖🤖\n")
    print("Looks like all glyphs have the same width counts – nice work! \n")
    print("🎉🎉🎉\n")


if glyphsToIgnore is not "" and len(glyphsToIgnore.split(" ")) > 0:
    print("\n--------------------------------------------------------------\n")
    print("NOTE: ignored the following glyphs (they are experiments or currently low-priority)")
    print("(edit script to adjust these)")
    for name in glyphsToIgnore.split(" "):
        print(name, end=" ")

print("\n")