# ## set major version
# for font in AllFonts():
#     font.info.versionMajor = 1

for font in AllFonts():
    # help(font)
    font.prepareUndo()
    font.newGlyph("r")
    font["r"].width = 600
    font.performUndo()