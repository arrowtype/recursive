from vanilla import FloatingWindow, Button, EditText, TextBox, CheckBox, ColorWell
from AppKit import NSColor
from mojo.UI import Message
from mojo.roboFont import OpenWindow
from vanilla.dialogs import getFile, OpenFont


class GlyphFax(object):

    def __init__(self):
        '''Initialize the dialog.'''
        x = y = padding = 10
        buttonHeight = 20
        windowWidth = 400

        rows = 4.5

        self.w = FloatingWindow((windowWidth, buttonHeight * rows + padding * (rows)), "Glyph Fax Machine")

        self.fonts = {}

        self.w.editText = EditText((x, y, -padding, buttonHeight * 2 + padding), placeholder="Space-separated list of glyphs to copy")

        y += buttonHeight * 2 + padding * 2

        # self.w.overwriteGlyphsCheckBox = CheckBox((x, y, -padding, buttonHeight), "Overwrite Glyphs", value=False, callback=self.overwriteGlyphsOptions)

        # y += buttonHeight + padding

        self.w.overwriteNormalWidthGlyphsCheckBox = CheckBox((x, y, -padding, buttonHeight), "Overwrite 600w Glyphs", value=False, sizeStyle="small")
        # self.w.overwriteNormalWidthGlyphsCheckBox.show(False)

        self.w.overwriteAdjustedWidthGlyphsCheckBox = CheckBox((windowWidth * 0.4, y, -padding, buttonHeight), "Overwrite non-600w Glyphs", value=False, sizeStyle="small")
        # self.w.overwriteAdjustedWidthGlyphsCheckBox.show(False)
        self.w.colorWell = ColorWell((windowWidth * 0.85, y, -padding, buttonHeight), color=NSColor.orangeColor())

        y += buttonHeight + padding

        self.w.sans2mono = Button(
            (x, y, windowWidth / 3 - padding / 2, buttonHeight),
            "Sans → Mono",
            callback=self.sans2monoCallback)

        self.w.mono2sans = Button(
            (windowWidth / 3 + padding, y, -padding, buttonHeight),
            "Mono → Sans",
            callback=self.mono2SansCallback)

        self.w.open()

    def copyGlyph(self, glyphName, fontToCopyFrom, fontToSendTo):

        print(f"copying glyph /{glyphName} from \n\t{fontToCopyFrom} \n\tto \n\t{fontToSendTo}")

        glyphCopyName = glyphName
        copyGlyph = True

        if glyphName not in fontToSendTo:
            fontToSendTo.newGlyph(glyphName)
        else:
            overwrite600 = self.w.overwriteNormalWidthGlyphsCheckBox.get()
            overwriteNon600 = self.w.overwriteAdjustedWidthGlyphsCheckBox.get()

            # default case: overwrite is false (overwrite 600 is true, overwrite non600 is false)
            if overwrite600 is False and overwriteNon600 is False:
                # glyphCopyName = glyphName + '.copy'
                # fontToSendTo.newGlyph(glyphCopyName)

                copyGlyph = False

            elif overwrite600 is True and overwriteNon600 is True:
                fontToSendTo[glyphCopyName].clear()

            elif overwrite600 is False and overwriteNon600 is True:
                if round(fontToSendTo[glyphCopyName].width, -1) == 600:
                    # glyphCopyName = glyphName + '.copy'
                    # fontToSendTo.newGlyph(glyphCopyName)

                    copyGlyph = False
                else:
                    fontToSendTo[glyphCopyName].clear()

            elif overwrite600 is True and overwriteNon600 is False:
                if round(fontToSendTo[glyphCopyName].width, -1) == 600:
                    fontToSendTo[glyphCopyName].clear()
                else:
                    # glyphCopyName = glyphName + '.copy'
                    # fontToSendTo.newGlyph(glyphCopyName)

                    copyGlyph = False

        if copyGlyph:
            glyphToCopy = fontToCopyFrom[glyphName]
            layerGlyph = fontToSendTo[glyphCopyName].getLayer("foreground")

            # get the point pen of the layer glyph
            pen = layerGlyph.getPointPen()
            # draw the points of the imported glyph into the layered glyph
            glyphToCopy.drawPoints(pen)

            if len(layerGlyph.components) == 1:
                parentGlyphWidth = fontToSendTo[layerGlyph.components[0].baseGlyph].width
                print(type(parentGlyphWidth))
                layerGlyph.width = parentGlyphWidth

                print("copied glyph now has width of its component parent:", str(parentGlyphWidth))
            else:
                layerGlyph.width = glyphToCopy.width

            layerGlyph.markColor = (self.w.colorWell.get().redComponent(), self.w.colorWell.get().greenComponent(), self.w.colorWell.get().blueComponent(), self.w.colorWell.get().alphaComponent())

            for anchor in glyphToCopy.anchors:
                layerGlyph.appendAnchor(anchor.name, (anchor.x, anchor.y))

    def glyphsToCopy(self, sender):
        if self.w.editText.get() == "":
            Message('no glyphs listed', title='Glyph Fax Machine', informativeText='Please list glyphs to send copies of!')
            return

        return self.w.editText.get().split(" ")

    # default: dlig & ss01–ss12 off

    def getFontsCueCopying(self, proportionToCopyFrom, glyphsToCopy):
        files = getFile("Select UFOs to copy glyphs between", allowsMultipleSelection=True, fileTypes=["ufo"])

        for path in files:
            f = OpenFont(path, showInterface=True)
            variation = f.info.styleName.replace('Mono ', '').replace('Sans ', '')
            if variation not in self.fonts.keys():
                self.fonts[variation] = []

            if self.fonts[variation] == []:
                self.fonts[variation].append(f)
            elif self.fonts[variation] != []:
                # if 'Mono' already in list, put 'Sans' second
                if proportionToCopyFrom in self.fonts[variation][0].info.styleName:
                    self.fonts[variation].append(f)
                # else put 'Mono' first
                else:
                    self.fonts[variation] = [f] + self.fonts[variation]

        for variation in self.fonts.keys():
            print('\n', variation, '\n')
            for glyphName in glyphsToCopy:
                self.copyGlyph(glyphName, self.fonts[variation][0], self.fonts[variation][1])

        self.w.close()

    # ss01–ss12 on

    def mono2SansCallback(self, sender):
        '''Copy glyphs from Mono to Sans masters.'''

        glyphsToCopy = self.glyphsToCopy(sender)

        if glyphsToCopy is not None:
            self.getFontsCueCopying('Mono', glyphsToCopy)

    def sans2monoCallback(self, sender):
        '''Copy glyphs from Sans to Mono masters.'''

        glyphsToCopy = self.glyphsToCopy(sender)

        if glyphsToCopy is not None:
            self.getFontsCueCopying('Sans', glyphsToCopy)


if __name__ == '__main__':

    OpenWindow(GlyphFax)
