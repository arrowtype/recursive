from vanilla.dialogs import *


unicodesToAdd = {
    
}

unicodesToAdd = {
    'eightinferior': (8328,),
    'eightsuperior': (8312,),
    'fiveinferior': (8325,),
    'fivesuperior': (8309,),
    'fourinferior': (8324,),
    'foursuperior': (8308,),
    'nineinferior': (8329,),
    'ninesuperior': (8313,),
    'onehalf': (189,),
    'oneinferior': (8321,),
    'onequarter': (188,),
    'onesuperior': (185,),
    'seveninferior': (8327,),
    'sevensuperior': (8311,),
    'sixinferior': (8326,),
    'sixsuperior': (8310,),
    'threeinferior': (8323,),
    'threequarters': (190,),
    'threesuperior': (179,),
    'twoinferior': (8322,),
    'twosuperior': (178,),
    'onehalf': (189,),
    'onequarter': (188,),
    'threequarters': (190,),
    'onethird': (8531,),
    'twothirds': (8532,),
    'oneeighth': (8539,),
    'threeeighths': (8540,),
    'fiveeighths': (8541,),
    'seveneighths': (8542,),
    'zeroinferior': (8320,),
    'zerosuperior': (8304,)
    }



files =  getFile("Select files to sort", allowsMultipleSelection=True, fileTypes=["ufo"])


for file in files:
    font = OpenFont(file, showInterface=False)

    for figure in unicodesToAdd.keys():
        if figure in font.keys():
            print(f"{figure} had unicodes '{font[figure].unicodes}'")
            font[figure].unicodes = unicodesToAdd[figure]
            print(f"...& is now '{unicodesToAdd[figure]}'\n")

    newGlyphOrder = font.naked().unicodeData.sortGlyphNames(font.templateGlyphOrder, sortDescriptors=[
                    dict(type="cannedDesign", ascending=True, allowPseudoUnicode=True)])

    font.templateGlyphOrder = newGlyphOrder

    font.save()
    font.close()