'''
    options:
        override? if not, append '.copy' suffix
        monoToSans? if not, will go sans to mono
    
    get list of fonts
    pair fonts by stylename (mono & sans linear slanted A, mono & sans casual B, etc)

    check: copy glyphs 'a, b, c.italic' from selected mono to sans fonts?
    
    for glyph in selection of current font
        go through fontPairs
            copy glyph from mono to sans
            mark glyph with color (orange?)
'''

from vanilla.dialogs import *
import os
from mojo.UI import AskString

from vanilla import *

class WindowDemo(object):

    def __init__(self):
        self.w = Window((200, 70), "Window Demo")
        self.w.myButton = Button((10, 10, -10, 20), "My Button")
        self.w.myTextBox = TextBox((10, 40, -10, 17), "My Text Box")
        self.w.open()

    def reportClick(self):
        

WindowDemo()

# # glyphsToCopy = CurrentFont().selection

# glyphsToMakeDefault = AskString(
#     'Space-separated list of glyphs to copy Mono to Sans').split(" ")

# # if the user cancels or inputs an empty string, cancel the script
# if glyphsToMakeDefault == "":
#     print("canceled")

# files = getFile("Select UFOs to copy glyphs between",
#                 allowsMultipleSelection=True, fileTypes=["ufo"])

# # fonts = {
# #         "Casual A" = (monoFontCasualA, sansFontCasualA)
# # }

# fonts = {}

# for path in files:
#     f = OpenFont(path, showInterface=False)
#     # style = f.info.styleName
#     variation = f.info.styleName.replace('Mono ','').replace('Sans ','')
#     if variation not in fonts.keys():
#         fonts[variation] = []

#     if fonts[variation] == []:
#         fonts[variation].append(f)
#     elif fonts[variation] != []:
#         # if 'Mono' already in list, put 'Sans' second
#         if 'Mono' in fonts[variation][0].info.styleName:
#             fonts[variation].append(f)
#         # else put 'Mono' first
#         else:
#             fonts[variation] = [f] + fonts[variation]

# for variation in fonts.keys():
#     print(variation)
#     for f in fonts[variation]:
#         print('\t', f)
#         f.close()