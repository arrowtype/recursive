from fontTools.ufoLib import UFOReader

# iteratee through glyphs to see whether you can spot problem

ufoPath="src/masters/mono/Recursive Mono-Linear A Slanted.ufo"

# print(UFOReader(ufoPath).getGlyphSet(validateRead=None))
# UFO = UFOReader(ufoPath)

# import pprint

# pp = pprint.PrettyPrinter(indent=2, width=200)
# pp.pprint(UFO.getCharacterMapping())


# for unicodes, name in UFO.getCharacterMapping():
#     print(unicodes, name)


from fontTools.ufoLib.glifLib import GlifLibError
from defcon import Font

ufo = Font(ufoPath)
for layer in ufo.layers: 
    for glyphName in layer.keys(): 
        try: 
            layer[glyphName] 
        except GlifLibError: 
            print(layer.name, glyphName)