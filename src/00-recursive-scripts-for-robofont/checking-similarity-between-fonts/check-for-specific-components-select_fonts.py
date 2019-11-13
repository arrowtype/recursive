from vanilla.dialogs import *
from mojo.UI import OutputWindow

## use if you want to select different files
files = getFile("Select file to copy from", allowsMultipleSelection=True, fileTypes=["ufo"])

## uncomment if you wish to see output window
OutputWindow().show()
OutputWindow().clear()


components = {}

for fontPath in files:

    f = OpenFont(fontPath, showInterface=False)

    fontName = f.info.styleName

    if fontName not in components.keys():
            components[fontName] = {}

    for g in f:
        for comp in g.components:
            if comp.baseGlyph == 'dotaccentcomb.case' or comp.baseGlyph == 'cedillacomb.case':
                if g.name not in components[fontName].keys():
                    components[fontName][g.name] = []

                components[fontName][g.name].append(comp.baseGlyph)
            

    f.close()

import pprint
pp = pprint.PrettyPrinter(indent=2, width=200)
pp.pprint(components)



# common_keys_vals = [(key, [dict[key] for dict in components.keys()])]
