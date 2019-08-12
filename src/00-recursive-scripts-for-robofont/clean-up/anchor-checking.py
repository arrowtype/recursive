import pprint
from vanilla.dialogs import *
files = getFile("Select files to check for character set similarity", allowsMultipleSelection=True, fileTypes=["ufo"])

anchorNames = {}

for file in files:
    f = OpenFont(file, showInterface=False)
    
    fontName = f.info.styleName
    
    print("---------------------------------------------------------------------------")
    print("\n",fontName)
    # print(f["dotbelowcomb"].components)
    
    
    for g in f:

        for a in g.anchors:
            if fontName not in anchorNames.keys():
                anchorNames[fontName] = {}
                
            if g.name not in anchorNames[fontName].keys():
                anchorNames[fontName][g.name] = []
                
            anchorNames[fontName][g.name].append(a.name)
    print("\n")
    
    f.close()

pp = pprint.PrettyPrinter(indent=2, width=200)
pp.pprint(anchorNames)

