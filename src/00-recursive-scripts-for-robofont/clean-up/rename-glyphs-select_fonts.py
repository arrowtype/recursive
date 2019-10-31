from vanilla.dialogs import *
    
inputFonts = getFile("select masters to add feature code to", allowsMultipleSelection=True, fileTypes=["ufo"])
    
for fontPath in inputFonts:
    f = OpenFont(fontPath, showInterface=False)

    oldName, newName = '.arrowhead', '_arrowhead'

    for layer in font.layers:
        layer.renameGlyph(oldName, newName, renameComponents=True, renameGroups=True, renameKerning=True, renameGlyphOrder=True)

    print(f.info.styleName)
    print(f"{oldName} renamed to {newName}\n")

    f.save()
    f.close()


