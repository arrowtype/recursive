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

    print(font.groups)

    print(font.kerning.items())

    if len(font.kerning.keys()) == 0:
        print("no kerns")
        print(font.kerning)

        help(font.kerning)
        # font.kerning = {}

        # groups = RKerning()

        groups = RKerning()

        blankKerning = {
            ('public.kern1.A', 'public.kern2.Z'): 0
            }
        font.kerning.update(blankKerning)
        print(font.kerning)


    font.save()
    font.close()