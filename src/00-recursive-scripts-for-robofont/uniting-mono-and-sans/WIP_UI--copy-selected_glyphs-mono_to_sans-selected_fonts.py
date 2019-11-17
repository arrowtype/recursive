from vanilla import FloatingWindow, Button, EditText, TextBox
from mojo.UI import Message
from mojo.roboFont import OpenWindow

class ToolDemo(object):

    def __init__(self):
        '''Initialize the dialog.'''
        x = y = padding = 10
        buttonHeight = 20
        windowWidth = 320
        
        rows = 5
        
        self.w = FloatingWindow((windowWidth, buttonHeight*rows + padding*(rows)), "Recursive Glyph Fax Machine")

        glyphsToCopy = []
        
        self.w.textBox = TextBox((x, y, -padding, buttonHeight), "Glyphs to copy (space-separated list)")
        
        y += buttonHeight 
        
        self.w.editText = EditText((x, y, -padding, buttonHeight*2+padding))

        y += buttonHeight*2 + padding*2

        self.w.sans2mono = Button(
                (x, y, windowWidth/3 - padding/2, buttonHeight),
                "Sans → Mono",
                callback=self.sans2monoCallback)

        self.w.mono2sans = Button(
                (windowWidth/3 + padding, y, -padding, buttonHeight),
                "Mono → Sans",
                callback=self.mono2SansCallback)

        self.w.open()

    def mono2SansCallback(self, sender):
        '''Copy glyphs from Mono to Sans masters.'''
        
        #print(self.glyphsToCopy)
        print(self.w.editText.get().split(" "))

        # if font is None:
        #     Message('no font open', title='myTool', informativeText='Please open a font first!')
        #     return

    def sans2monoCallback(self, sender):
        '''Copy glyphs from Sans to Mono masters.'''

        print(self.w.editText.get().split(" "))

        # if font is None:
        #     Message('no font open', title='myTool', informativeText='Please open a font first!')
        #     return




if __name__ == '__main__':

    OpenWindow(ToolDemo)