from vanilla import FloatingWindow, Button, EditText, TextBox, CheckBox, ColorWell
from AppKit import NSColor
from mojo.UI import Message
from mojo.roboFont import OpenWindow
from vanilla.dialogs import *

class GlyphFax(object):

    def __init__(self):
        '''Initialize the dialog.'''
        x = y = padding = 10
        buttonHeight = 20
        windowWidth = 400
        
        rows = 5.5
        
        self.w = FloatingWindow((windowWidth, buttonHeight*rows + padding*(rows)), "Glyph Fax Machine")

        self.fonts = {}
        
        # self.w.textBox = TextBox((x, y, -padding, buttonHeight), "Glyphs to Copy")
        

        # y += buttonHeight 
        
        self.w.editText = EditText((x, y, -padding, buttonHeight*2+padding), placeholder="Space-separated list of glyphs to copy")


        y += buttonHeight*2 + padding*2
        
        self.w.overwriteGlyphsCheckBox = CheckBox((x, y, -padding, buttonHeight), "Overwrite Glyphs", value=False, callback=self.overwriteGlyphsOptions)
        self.w.colorWell = ColorWell((windowWidth*0.8, y, -padding, buttonHeight),color=NSColor.orangeColor())

        y += buttonHeight + padding

        self.w.overwriteNormalWidthGlyphsCheckBox = CheckBox((x,y, -padding, 10), "Overwrite 600-unit Glyphs", value=True, sizeStyle="small")
        self.w.overwriteNormalWidthGlyphsCheckBox.show(False)

        self.w.overwriteAdjustedWidthGlyphsCheckBox = CheckBox((windowWidth*0.45, y, -padding, 10), "Overwrite non-600-unit Glyphs", value=False, sizeStyle="small")
        self.w.overwriteAdjustedWidthGlyphsCheckBox.show(False)

        y += buttonHeight + padding

        self.w.sans2mono = Button(
                (x, y, windowWidth/3 - padding/2, buttonHeight),
                "Sans → Mono",
                callback=self.sans2monoCallback)

        self.w.mono2sans = Button(
                (windowWidth/3 + padding, y, -padding, buttonHeight),
                "Mono → Sans",
                callback=self.mono2SansCallback)

        self.w.open()

    def copyGlyph(self,glyphName, fontToCopyFrom, fontToSendTo):

        print(f"copying glyph /{glyphName} from \n\t{fontToCopyFrom} \n\tto \n\t{fontToSendTo}")

        glyphCopyName = glyphName

        if glyphName not in fontToSendTo:
            fontToSendTo.newGlyph(glyphName)
        else:
            overwrite = self.w.overwriteGlyphsCheckBox.get()
            overwrite600 = self.w.overwriteNormalWidthGlyphsCheckBox.get()
            overwriteNon600 = self.w.overwriteAdjustedWidthGlyphsCheckBox.get()

            # default case: overwrite is false (overwrite 600 is true, overwrite non600 is false)
            if overwrite == False:
                glyphCopyName = glyphName + '.copy'
                fontToSendTo.newGlyph(glyphCopyName)

            elif overwrite == True and overwrite600 == True and overwriteNon600 == True:
                fontToSendTo[glyphCopyName].clear()

            elif overwrite == True and overwrite600 == False and overwriteNon600 == True:
                if round(fontToSendTo[glyphCopyName].width, -1) == 600:
                    glyphCopyName = glyphName + '.copy'
                    fontToSendTo.newGlyph(glyphCopyName)
                else:
                    fontToSendTo[glyphCopyName].clear()

            elif overwrite == True and overwrite600 == True and overwriteNon600 == False:
                if round(fontToSendTo[glyphCopyName].width, -1) == 600:
                    fontToSendTo[glyphCopyName].clear()
                else:
                    glyphCopyName = glyphName + '.copy'
                    fontToSendTo.newGlyph(glyphCopyName)

        glyphToCopy = fontToCopyFrom[glyphName]
        layerGlyph = fontToSendTo[glyphCopyName].getLayer("foreground")

        # get the point pen of the layer glyph
        pen = layerGlyph.getPointPen()
        # draw the points of the imported glyph into the layered glyph
        glyphToCopy.drawPoints(pen)

        layerGlyph.width = glyphToCopy.width

        layerGlyph.markColor = (self.w.colorWell.get().redComponent(), self.w.colorWell.get().greenComponent(),self.w.colorWell.get().blueComponent(),self.w.colorWell.get().alphaComponent())

        for anchor in glyphToCopy.anchors:
            layerGlyph.appendAnchor(anchor.name, (anchor.x, anchor.y))

    def glyphsToCopy(self,sender):
        if self.w.editText.get() == "":
            Message('no glyphs listed', title='Glyph Fax Machine', informativeText='Please list glyphs to send copies of!')
            return
        
        return self.w.editText.get().split(" ")

    def getFontsCueCopying(self, proportionToCopyFrom, glyphsToCopy):
        files = getFile("Select UFOs to copy glyphs between",
                allowsMultipleSelection=True, fileTypes=["ufo"])

        for path in files:
            f = OpenFont(path, showInterface=False)
            # style = f.info.styleName
            variation = f.info.styleName.replace('Mono ','').replace('Sans ','')
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
            print('\n',variation,'\n')

            for glyphName in glyphsToCopy:
                self.copyGlyph(glyphName, self.fonts[variation][0], self.fonts[variation][1])

            for f in self.fonts[variation]:
                # print('\t', f)
                f.save()
                f.close()

        self.w.close()

    def overwriteGlyphsOptions(self, sender):
        '''Show/hide overwriting options'''

        if self.w.overwriteNormalWidthGlyphsCheckBox.isVisible() == False:
            self.w.overwriteNormalWidthGlyphsCheckBox.show(True)
        else:
            self.w.overwriteNormalWidthGlyphsCheckBox.show(False)

        if self.w.overwriteAdjustedWidthGlyphsCheckBox.isVisible() == False:
            self.w.overwriteAdjustedWidthGlyphsCheckBox.show(True)
        else:
            self.w.overwriteAdjustedWidthGlyphsCheckBox.show(False)



    def mono2SansCallback(self, sender):
        '''Copy glyphs from Mono to Sans masters.'''

        glyphsToCopy = self.glyphsToCopy(sender)

        if glyphsToCopy is not None:
            self.getFontsCueCopying('Mono',glyphsToCopy)

    def sans2monoCallback(self, sender):
        '''Copy glyphs from Sans to Mono masters.'''

        glyphsToCopy = self.glyphsToCopy(sender)

        if glyphsToCopy is not None:
            self.getFontsCueCopying('Sans',glyphsToCopy)



if __name__ == '__main__':

    OpenWindow(GlyphFax)