# menuTitle : Slant Selected Glyphs
# shortCut  : command+control+shift+A

f = CurrentFont()

italicAngle = f.info.italicAngle

italicOffset = f.lib["com.typemytype.robofont.italicSlantOffset"]

for g in f.selection:
    # g.decompose()
    f[g].prepareUndo()
    
    for c in f[g]:     
        c.skewBy(-italicAngle) 
        c.moveBy((italicOffset, 0))

    
    f[g].performUndo()