from fontTools.ufoLib import UFOReader


ufoPath="src/masters/mono/Recursive Mono-Linear A Slanted.ufo"


from fontTools.ufoLib.glifLib import GlifLibError
from defcon import Font

# iteratee through glyphs to see whether you can spot problem
ufo = Font(ufoPath)
for layer in ufo.layers: 
    for glyphName in layer.keys(): 
        try: 
            layer[glyphName] 
        except GlifLibError: 
            print(layer.name, glyphName)