glyphs = {}

for font in AllFonts():
    fontName = font.info.familyName + " " + font.info.styleName
    
    glyphs[fontName] = []
    for glyph in font:
        glyphs[fontName].append(glyph.name)
    
    
print(glyphs[list(glyphs.keys())[0]])
print("")
print(glyphs[list(glyphs.keys())[1]])

list1 = glyphs[list(glyphs.keys())[0]]
list2 = glyphs[list(glyphs.keys())[1]]
print("\nMissing values in second list:", (set(list1).difference(list2))) 