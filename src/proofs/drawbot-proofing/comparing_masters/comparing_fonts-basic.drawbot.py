from AppKit import NSColor
_color = NSColor.colorWithCalibratedRed_green_blue_alpha_(.75, .75, .75, 1)
Variable([
    dict(name="customString", ui="TextEditor"),
    dict(name="lineHeight", ui="Slider",
            args=dict(
                value=120,
                minValue=80,
                maxValue=160)),
    dict(name="matchXHeights", ui="CheckBox"),
    dict(name="fontSize1", ui="Slider",
            args=dict(
                value=95,
                minValue=75,
                maxValue=125)),
    dict(name="fontSize2", ui="Slider",
            args=dict(
                value=95,
                minValue=75,
                maxValue=125)),
    dict(name="fontSize3", ui="Slider",
            args=dict(
                value=95,
                minValue=75,
                maxValue=125)),
    dict(name="fontColor1", ui="ColorWell"),
    dict(name="fontColor2", ui="ColorWell"),
    dict(name="fontColor3", ui="ColorWell"),
    dict(name="missingGlyphColor", ui="ColorWell", args=dict(color=_color)),
], globals())

# add a maxNumPerLine for better controlling text amount

size('A3')

fontSize(100)
fallbackFont("Arial")

counter = 1


################# 😺 Trying Frederik's suggested method of targeting missing glyphs 😺 #################

import AppKit
import CoreText

from fontTools.ttLib import TTFont
from fontTools.misc.py23 import unichr

def fontPath(fontName):
    font = CoreText.CTFontDescriptorCreateWithNameAndSize(fontName, 10)
    if font:
        url = CoreText.CTFontDescriptorCopyAttribute(font, CoreText.kCTFontURLAttribute)
        if url:
            return url.path()
    else:
        # warn if font doest not exists
        pass
        
    return None

def listFontGlyphNames(fontName):
    path = fontPath(fontName)
    if path is None:
        return []      
    try:
        fontToolsFont = TTFont(path, lazy=True, fontNumber=0)
    except TTLibError:
        # warn if fontTools cannot read the file
        return []        
    characters = []
    glyphNames = fontToolsFont.getGlyphNames()
    fontToolsFont.close()
    if ".notdef" in glyphNames:
        glyphNames.remove(".notdef")
    return glyphNames

# glyphNames = listFontGlyphNames(fontName)

# t = FormattedString(font=fontName)
# t.appendGlyph(*glyphNames)

# textBox(t, (0, 0, width(), height()))

def checkIfGlyphExists(char, fontToCheck, fontColor):
    glyphNamesInFont = listFontGlyphNames(fontToCheck)
    if char in glyphNamesInFont:
        return fill(fontColor) 
    else:
        return fill(missingGlyphColor)

################# 😺 TRIPLES LETTERS IN YOUR STRING, THEN SETS THEM AS TEXT 😺 #################
def testWeights(string, fontName1, fontName2, fontName3):
    counter = 1
    lineCount = 1
    textWidth = 0
    starterPosX = 33
    starterPosY = 125
    lineHeightValue = lineHeight
    positionX = starterPosX
    positionY = height()-starterPosY
    newString = ""
    for char in string:
        newString += char*3
    
    for char in newString:
        if counter % 3 == 0:
            # fill(fontColor3)
            
            fontSize(fontSize3)
            # checkIfGlyphExists(char, "3")
            checkIfGlyphExists(char, fontName3, fontColor3)
            font(fontName3)

            if matchXHeights:
                fontSize(newFontSize3)

        elif (counter + 1) % 3 ==0:
            # fill(fontColor2)
            
            fontSize(fontSize2)
            # checkIfGlyphExists(char, "2")
            checkIfGlyphExists(char, fontName2, fontColor2)
            font(fontName2)

            if matchXHeights:
                fontSize(newFontSize2)

        else:
            # fill(fontColor1)
            
            fontSize(fontSize1)
            checkIfGlyphExists(char, fontName1, fontColor1)
            font(fontName1)
        
        text(char, (positionX, positionY))
        
        ### positions text and controls line wrapping
        letterWidth, letterHeight = textSize(char)
        
        textWidth += letterWidth
        positionX += letterWidth
        
        if counter % 3 == 0:
            letterWidth, letterHeight = textSize(" ")
            positionX += letterWidth + 10
        
        if counter % 9 == 0:
            lineCount += 1
            positionX = starterPosX
            positionY -= lineHeightValue

        counter += 1
        
                
        
def calcNewSize(targetFontName, targetFontSize):
    # source font (font1)
    fontSize(fontSize1)
    font(fontName1)
    xHeight1 = fontXHeight()
    print(fontXHeight())
    
    # target font
    fontSize(targetFontSize)
    font(targetFontName)
    xHeight2 = fontXHeight()

    return targetFontSize * (xHeight1 / xHeight2)

################# ✅ You can add custom fonts here ✅ #################
import string
alpha = string.ascii_uppercase
# alpha = string.lowercase
# customString = "The Royal Academy of Art is an art academy in The Hague. Succeeding the Haagsche Teeken-Academie, the academy was founded on 29 September 1682, making it the oldest in the Netherlands"


fontName1, fontName2, fontName3 = "RecursiveMonoB_020-LnrLt", "RecursiveMonoB_020-LnrXBd", "RecursiveMonoB_020-LnrBk"

print("font size 1 is " + str(fontSize1) + " pt")

if matchXHeights:
    newFontSize2 = calcNewSize(fontName2, fontSize2)
    newFontSize3 = calcNewSize(fontName3, fontSize3)

    print("new font size 2 is %s pt" %newFontSize2)
    print("new font size 3 is %s pt" %newFontSize3)

else:
    print("font size 2 is " + str(fontSize2) + " pt")
    print("font size 3 is " + str(fontSize3) + " pt")

if customString != "":
    customString.replace(" ","")
    testWeights(customString, fontName1, fontName2, fontName3) # use your string as an argument
else:
    testWeights(alpha, fontName1, fontName2, fontName3)


#### to do: add font names and current date to test

import datetime

now = datetime.datetime.now()
metadata = str(now) + " // font 1 is " + fontName1 + " at "  + str(round(fontSize1, 3)) + " pt; font 2 is " + fontName2 + " at "  + str(round(fontSize2, 3)) + " pt; font 3 is " + fontName3 + " at "  + str(round(fontSize3, 3)) + " pt"

font("Verdana")
fontSize(9)
fill(0,0,0)
textBox(metadata, (20, 0, width(), 30))


#### to do: if letter doesn't exist in the supplied font, replace with "n" or some other user-defined string.
#? maybe substitute with rectangle / asterisk / U+25A1 (white square) □


################# 😺 SAVE AS A PDF IF YOU'D LIKE TO PRINT 😺 #################
# saveImage("/Users/stephennixon/Dropbox/KABK_netherlands/type_media/02-tm_contrast/tests/stroop_sharper_uc_in_progress-010718.svg")

# help(saveImage)