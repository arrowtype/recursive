from vanilla.dialogs import *
    
inputFonts = getFile("select masters to add feature code to", allowsMultipleSelection=True, fileTypes=["ufo"])

renames = {
    'f_quote.code': 'f_quotesingle.code',
    'asterix_asterix_asterix.code': 'asterisk_asterisk_asterisk.code',
    'asterix_asterix.code': 'asterisk_asterisk.code'
}
    
for fontPath in inputFonts:
    f = OpenFont(fontPath, showInterface=False)

    # oldName, newName = 'ydot.italic', 'ydotbelow.italic'

    for oldName, newName in renames.items():
        for layer in f.layers:
            if oldName in layer.keys():
                layer.renameGlyph(oldName, newName, renameComponents=True, renameGroups=True, renameKerning=True, renameGlyphOrder=True)

                print(f.info.styleName)
                print(f"{oldName} renamed to {newName}\n")
            else:
                print(f.info.styleName)
                print(f"{oldName} not in {f.info.styleName}, {layer.name}\n")

    f.save()
    f.close()


