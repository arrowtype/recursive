from vanilla.dialogs import *
from fontTools import agl

# add glyph names to this dictionary if they aren't getting automatically picked up
unicodeNameMatches = {
    "nobreakspace":     "00A0",
    "kcommaaccent":     "0137",
    "Kcommaaccent":     "0136",
    "gcommaaccent":     "0123",
    "Gcommaaccent":     "0122",
    "ncommaaccent":     "0146",
    "Ncommaaccent":     "0145",
    "lcommaaccent":     "013C",
    "Lcommaaccent":     "013B",
    "rcommaaccent":     "0157",
    "Rcommaaccent":     "0156",
    "scommaaccent":     "0219",
    "Scommaaccent":     "0218",
    "ijacute":          "E132",
    "IJacute":          "E133",
    "adotbelow":        "1EA1",
    "Adotbelow":        "1EA0",
    "edotbelow":        "1EB9",
    "Edotbelow":        "1EB8",
    "idotbelow":        "1ECB",
    "Idotbelow":        "1ECA",
    "odotbelow":        "1ECD",
    "Odotbelow":        "1ECC",
    "udotbelow":        "1EE5",
    "Udotbelow":        "1EE4",
    "etilde":           "1EBD",
    "Etilde":           "1EBC",
    "ytilde":           "1EF9",
    "Ytilde":           "1EF8",
    "ymacron":          "0233",
    "Ymacron":          "0232",
    "oogonek":          "01EB",
    "Oogonek":          "01EA",
    "schwa":            "0259",
    "Schwa":            "018F",
    
    # combining accents
    "gravecomb":                "0300",
    "acutecomb":                "0301",
    "circumflexcomb":           "0302",
    "tildecomb":                "0303",
    "macroncomb":               "0304",
    "brevecomb":                "0306",
    "dotaccentcomb":            "0307",
    "dieresiscomb":             "0308",
    "ringcomb":                 "030A",
    "hungarumlautcomb":         "030B",
    "caroncomb":                "030C",
    "commaturnedabovecomb":     "0312",
    "commaaboverightcomb":      "0315",
    "dotbelowcomb":             "0323",
    "commaaccentcomb":          "0326",
    "cedillacomb":              "0327",
    "ogonekcomb":               "0328",
}

def addUnicodeForGlyph(g):
    if g.unicode == None or g.unicodes == []:
            if g.name in agl.AGL2UV:
                uni = agl.AGL2UV[g.name]
    
                g.unicode = hex(uni)
    
                print(g.unicodes)
            elif g.name[:3] == "uni":
                uni = g.name[-4:]
            
                if uni != "case":
            
                    g.unicode = uni
                    print(g.name, g.unicodes, uni)
                    
def addUnicodeForTrickyGlyphs(g):
    if g.unicodes == ():
        uni = unicodeNameMatches.get(g.name, "noUnicode")
        
        if uni != "noUnicode":
            print(g.name, uni)
            g.unicode = uni


### use the below to use the current font (and comment out lines below)

def sortFont(font):
    # the new default is at the end, so this will re-apply a "smart sort" to the font
    newGlyphOrder = font.naked().unicodeData.sortGlyphNames(font.glyphOrder, sortDescriptors=[dict(type="cannedDesign", ascending=True, allowPseudoUnicode=True)])
    font.glyphOrder = newGlyphOrder


files = getFile("Select files to add unicodes to", allowsMultipleSelection=True, fileTypes=["ufo"])

for file in files:
    font = OpenFont(file, showInterface=False)
    for g in font:
        addUnicodeForGlyph(g)
        addUnicodeForTrickyGlyphs(g)
    sortFont(font)

    font.save()

    font.close()