from vanilla.dialogs import *
from mojo.UI import OutputWindow
import pprint

debug = False # will print full dictionaries

files = getFile("Select files to check for point count similarity", allowsMultipleSelection=True, fileTypes=["ufo"])

fonts = []
pointsDict = {}

OutputWindow().show()
OutputWindow().clear()


for file in files:
    font = OpenFont(file, showInterface=False)

    fontName = (font.info.styleName) + ' ' + (font.info.styleName)

    print(fontName)

    print(font.kerning)

    font.close()