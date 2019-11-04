from vanilla.dialogs import *
    
inputFonts = getFile("select masters to add feature code to", allowsMultipleSelection=True, fileTypes=["ufo"])
    
for fontPath in inputFonts:
    f = OpenFont(fontPath, showInterface=False)

    oldName, newName = 'at.cap', 'at.alt'

    for layer in f.layers:
        if oldName in f.keys():
            layer.renameGlyph(oldName, newName, renameComponents=True, renameGroups=True, renameKerning=True, renameGlyphOrder=True)

            print(f.info.styleName)
            print(f"{oldName} renamed to {newName}\n")
        else:
            print(f.info.styleName)
            print(f"{oldName} not in {f.info.styleName}\n")

    f.save()
    f.close()


