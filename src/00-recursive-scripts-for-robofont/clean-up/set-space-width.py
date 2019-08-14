from mojo.UI import AskString
from vanilla.dialogs import *

spaceWidth = int(AskString('Width to set glyph /space to (e.g. 300)'))

files = getFile("Select files to check for character set similarity", allowsMultipleSelection=True, fileTypes=["ufo"])

for file in files:
    f = OpenFont(file, showInterface=False)

    if f['space'].width != spaceWidth:

        f['space'].width = spaceWidth

        print("/space width set to ", spaceWidth)

    f.save()
    f.close()