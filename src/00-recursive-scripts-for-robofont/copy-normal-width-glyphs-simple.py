# copy normal-width glyphs
# a script to copy normal-width glyphs from a monospace UFO to a partly-monospace, partly-proportional UFO

from vanilla.dialogs import *
from mojo.UI import AskYesNoCancel
from mojo.UI import AskString
import random

##############################################
######## list of glyphs to *not* copy ########
##############################################

sansSpecificForm = [
    "g",
    "g.ss01",
    "fi",
    "fl",
    "cent"  # not a component
]

# list narrow glyphs (.5 width)
typicallyNarrowGlyphs = [
    "space",
    "i",
    "igrave",
    "iacute",
    "icircumflex",
    "idieresis",
    "j",
    "l",
    "z",
    "i.ss01",
    "l.ss01",
    "f.italic",
    "r.italic",
    "i.italic",
    "l.italic",
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

# .75 width
somewhatNarrowGlyphs = [
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
    "z"
]


# more than 600 units wide
somewhatWideGlyphs = [
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
    "Y"
]

# extra wide glyphs (not sure if these need to be separate?)
typicallyWideGlyphs = [
    "w",
    "M",
    "W",
    "ae",
    "fi",
    "fl",
    "ffl",
    "at"
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

# ? list glyphs that shouldn't be copied due to visual adjustments, e.g. serif "f" to sans-serif "f"
# f, r
# should these have versions like "ss01" that are copied, instead of normal versions?

glyphsToNotMove = typicallyNarrowGlyphs + narrowPunctuation + sansSpecificForm +
somewhatNarrowGlyphs + somewhatWideGlyphs + \
    typicallyWideGlyphs + newItalicGlyphs


def protectNonNormalGlyphs(masterToSendTo):
    for g in masterToSendTo:
        # if glyph width is not 600 (e.g. lcaron) or 0 (e.g. combinatory diacritics)
        if g.width != 600 and g.width != 0:
            glyphsToNotMove.append(g.name)
            print(g.name)


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


def glyphIsNormalWidth(glyphName):
    # make a variable
    glyphIsNormalWidth = False

    # if glyph name is not in the lists of not-normal width glyphs, set glyphIsNormalWidth to True
    if glyphName not in glyphsToNotMove:
        glyphIsNormalWidth = True

    return glyphIsNormalWidth


def getMasterToCopyFrom():
    # let user select masterToCopyFrom
    masterToCopyFromPath = getFile(
        "Please pick a master to copy normal-width characters from")
    # print(masterToCopyFromPath)

    masterToCopyFrom = OpenFont(masterToCopyFromPath)[0]

    return masterToCopyFrom


def getMasterToSendTo():
    # let user select masterToSendTo
    masterToSendToPath = getFile(
        "Please pick a master to overwrite copied normal-width characters into")
    # print(masterToSendToPath)
    masterToSendTo = OpenFont(masterToSendToPath)[0]

    masterToSendToName = masterToSendTo.info.familyName + \
        " " + masterToSendTo.info.styleName

    return masterToSendTo, masterToSendToName


def makeListOfGlyphsToOverwrite(masterToCopyFrom, masterToSendTo):
    glyphsToOverwrite = []
    for g in masterToCopyFrom:
        # if g.name not in typicallyNarrowGlyphs and g.name not in typicallyWideGlyphs:
        if glyphIsNormalWidth(g.name) and len(g.contours) > 0:
            glyphsToOverwrite.append(g.name)

    print(glyphsToOverwrite)
    return glyphsToOverwrite


def checkIfOkay(glyphsToOverwrite, masterToSendToName):
    proceedWithCopy = AskYesNoCancel("This will overwrite glyphs " + str(
        glyphsToOverwrite) + " in " + masterToSendToName+"." + " Proceed?")

    print(proceedWithCopy)
    return proceedWithCopy


def clearThenCopyGlyphs(masterToCopyFrom, masterToSendTo, userConfirmation):

    # set a color for overwritten glyphs
    color = setMarkColor()

    if userConfirmation == 1:
        for g in masterToSendTo:
            # if g.name not in typicallyNarrowGlyphs and g.name not in typicallyWideGlyphs and g.name not in somewhatNarrowGlyphs and g.name not in somewhatWideGlyphs:
            if glyphIsNormalWidth(g.name):
                g.clear()

                # # # check that glyph has no suffix (so as not to clear alternate glyphs) (but is this necessary?)
                # glyphNameSplit = g.name.split(".")
                # if len(glyphNameSplit) == 1:
                #     g.clear()

        for g in masterToCopyFrom:
            # if the glyph doesn't exist in the current font, create a new glyph
            if g.name not in masterToSendTo:
                masterToSendTo.newGlyph(g.name)

            if glyphIsNormalWidth(g.name):
                # get the layered glyph
                layerGlyph = masterToSendTo[g.name].getLayer("foreground")

                # get the point pen of the layer glyph
                pen = layerGlyph.getPointPen()
                # draw the points of the imported glyph into the layered glyph
                g.drawPoints(pen)

                layerGlyph.width = g.width

                # mark overwritten glyphs
                layerGlyph.markColor = color

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
