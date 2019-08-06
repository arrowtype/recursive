# copy normal-width glyphs
# a script to copy normal-width glyphs from a monospace UFO to a partly-monospace, partly-proportional UFO

from vanilla.dialogs import *
from mojo.UI import AskYesNoCancel
from mojo.UI import AskString
import random

protectPunctuation = False

protectNonNormalGlyphsTrueFalse = False

monoFormsToCopyAndMark = [
    "f.italic",
    "r.italic",
    "i.italic",
    "l.italic",
    "i.mono",
    "l.sans",
    "f.mono",
    "l.mono"
]

##############################################
######## list of glyphs to *not* copy ########
##############################################

glyphsToNotMove = [] # start empty list

monoSansSwitchingForms = [
    "g.ss01",
    "fi",
    "fl",
    "one.sans",
   
]


narrowPunctuation = [
    "asterisk",  # different size for sans
    "bar",
    "quoteleft",
    "quoteright",
    "comma",
    "colon",
    "semicolon",
    "period",
    "periodcentered",
    "brokenbar",
    "exclam",
    "exclamdown",
    "quotesingle",
    "grave",
    "bracketleft",
    "bracketright",
    "exclamdown",
    "parenleft",
    "parenright",
    "braceleft",
    "braceright",
    "braceleft.cap",
    "dollar.lower"
]

# list narrow glyphs 
narrowGlyphs = [
    "space",
    "i",
    "igrave",
    "iacute",
    "icircumflex",
    "idieresis",
    "j",
    "l",
    "z",
    "r",
    "f",
    "t",
    "I",
    "s",
    "c",
    "J",
    "L",
    "E",
    "F",
    "c",
    "zero",
    "z",
    "i.ss01",
    "l.ss01",
    "ldot", 
    "lslash"
]


# more than 600 units wide
wideGlyphs = [
    "m",
    "O",
    "A",
    "Y",
    "Q",
    "G",
    "V",
    "D",
    "H",
    "N",
    "U",
    "X",
    "Y",
    "w",
    "M",
    "W",
    "ae",
    "fi",
    "fl",
    "ffl",
    "at",
    "AE",
    "OE",
    "ae",
    "oe"
    "Oslash",
    "oslash"
]

newItalicGlyphs = [
    "c.italic",
    "d.italic",
    "g.italic",
    "j.italic",
    "m.italic",
    "s.italic",
    "w.italic",
    "z.italic",
]

glyphsToNotMove = glyphsToNotMove + monoSansSwitchingForms + narrowGlyphs + wideGlyphs + newItalicGlyphs

if protectPunctuation is True:
    glyphsToNotMove = glyphsToNotMove + narrowPunctuation

def protectNonNormalGlyphs(masterToSendTo):
    global glyphsToNotMove
    nonNormalGlyphs = []

    for g in masterToSendTo:
        # if glyph width is not 600 (e.g. lcaron) or 0 (e.g. combinatory diacritics)
        if g.name not in glyphsToNotMove and g.width != 600 and g.width != 0:
            nonNormalGlyphs.append(g.name)
            print(f"{g.name} is {g.width}")
                
    if protectNonNormalGlyphsTrueFalse is True:
         glyphsToNotMove = glyphsToNotMove + nonNormalGlyphs
         print("Protecting non-600 unit glyphs.")
    else:
        print("NOT protecting non-600 unit glyphs.")


def setMarkColor():
    userColor = AskString("Mark copied glyphs as r, b, or gray?", "gray")

    if userColor == "r":
        markColor = (1, .45, .45, .75)
    elif userColor == "gray":
        # markColor = (.45, 1, .55, .75)
        markColor = (0, 0, 0, 0.25)

    elif userColor == "b":
        markColor = (.45, .73, 1, .75)
    else:
        markColor = (1*random.random(), 1*random.random(),
                     1*random.random(), 0.5)
        print("no color set; using rgba" + str(markColor))

    return markColor

def getMasterToCopyFrom():
    # let user select masterToCopyFrom
    masterToCopyFromPath = getFile(
        "COPY FROM")

    if "sans" in masterToCopyFromPath[0].lower():
        print("error: you are trying to copy from a sans font")
        exit()

    masterToCopyFrom = OpenFont(masterToCopyFromPath)[0]

    return masterToCopyFrom


def getMasterToSendTo():
    # let user select masterToSendTo
    masterToSendToPath = getFile(
        "MOVE INTO")

    if "mono" in masterToSendToPath[0].lower():
        print("error: you are trying to copy into a mono font")
        exit()
    
    masterToSendTo = OpenFont(masterToSendToPath)[0]

    masterToSendToName = masterToSendTo.info.familyName + \
        " " + masterToSendTo.info.styleName

    return masterToSendTo, masterToSendToName


def makeListOfGlyphsToOverwrite(masterToCopyFrom, masterToSendTo):
    glyphsToOverwrite = []
    for g in masterToCopyFrom:
        # if g.name not in typicallyNarrowGlyphs and g.name not in typicallyWideGlyphs:
        if g.name not in glyphsToNotMove and len(g.contours) > 0:
            glyphsToOverwrite.append(g.name)

    print("Glyphs to overwrite:\n", sorted(glyphsToOverwrite))
    return glyphsToOverwrite


def checkIfOkay(glyphsToOverwrite, masterToSendToName):
    proceedWithCopy = AskYesNoCancel("This will overwrite glyphs " + str(
        glyphsToOverwrite) + " in " + masterToSendToName+"." + " Proceed?")

    return proceedWithCopy


def clearThenCopyGlyphs(masterToCopyFrom, masterToSendTo, userConfirmation):

    # set a color for overwritten glyphs
    color = setMarkColor()

    if userConfirmation == 1:
        for g in masterToSendTo:
            # if g.name not in typicallyNarrowGlyphs and g.name not in typicallyWideGlyphs and g.name not in somewhatNarrowGlyphs and g.name not in somewhatWideGlyphs:
            # if glyphIsNormalWidth(g.name):
            if g.name not in glyphsToNotMove:
                g.clear()

                # # # check that glyph has no suffix (so as not to clear alternate glyphs) (but is this necessary?)
                # glyphNameSplit = g.name.split(".")
                # if len(glyphNameSplit) == 1:
                #     g.clear()

        for g in masterToCopyFrom:
            # if the glyph doesn't exist in the current font, create a new glyph
            if g.name not in masterToSendTo:
                masterToSendTo.newGlyph(g.name)

            # if glyphIsNormalWidth(g.name):
            if g.name not in glyphsToNotMove:
                # get the layered glyph
                layerGlyph = masterToSendTo[g.name].getLayer("foreground")

                # get the point pen of the layer glyph
                pen = layerGlyph.getPointPen()
                # draw the points of the imported glyph into the layered glyph
                g.drawPoints(pen)

                layerGlyph.width = g.width

                # mark overwritten glyphs
                layerGlyph.markColor = color

                # Marking glyphs to fix while copying from mono to sans

                if layerGlyph.name in narrowPunctuation and protectPunctuation is False:
                    layerGlyph.markColor = (1,0,0,1)
                
                if layerGlyph.name in monoFormsToCopyAndMark and protectNonNormalGlyphsTrueFalse is False:
                    layerGlyph.markColor = (1,0,0,1)

                # also copy anchors

                # layerGlyph.anchors.append(something?)
                for anchor in g.anchors:
                    # print((anchor[0].name, (anchor[1][0], anchor[1][1])))
                    layerGlyph.appendAnchor(anchor.name, (anchor.x, anchor.y))

# print(getMasterToCopyFrom()[1])


getFrom = getMasterToCopyFrom()

if getFrom == "":
    print("nevermind")
else:
    sendTo, sendToName = getMasterToSendTo()

    protectNonNormalGlyphs(sendTo)

    glyphsToOverwrite = makeListOfGlyphsToOverwrite(getFrom, sendTo)
    userConfirmation = checkIfOkay(glyphsToOverwrite, sendToName)

    clearThenCopyGlyphs(getFrom, sendTo, userConfirmation)

# we are done :)
print("done")

# ? only copy glyphs that have changed / are different?
# how can you tell? maybe:
# if dateOfOriginGlif is newer that dateOfDestGlif, overwrite, else skip
