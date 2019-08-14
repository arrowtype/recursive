from vanilla.dialogs import *
from mojo.UI import AskString

files =  getFile("Select files to sort", allowsMultipleSelection=True, fileTypes=["ufo"])


for file in files:
    font = OpenFont(file, showInterface=False)

    newGlyphOrder = font.naked().unicodeData.sortGlyphNames(font.templateGlyphOrder, sortDescriptors=[
                    dict(type="cannedDesign", ascending=True, allowPseudoUnicode=True)])

    font.templateGlyphOrder = newGlyphOrder

    font.save()
    font.close()