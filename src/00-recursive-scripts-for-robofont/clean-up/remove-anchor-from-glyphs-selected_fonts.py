from vanilla.dialogs import *



inputFonts = getFile("select masters to add feature code to", allowsMultipleSelection=True, fileTypes=["ufo"])

accentsToClean = "acutecomb acutecomb.case gravecomb gravecomb.case hookcomb".split(" ")

anchorToRemove = "_side"


    
for fontPath in inputFonts:
    f = OpenFont(fontPath, showInterface=False)
    
    fontName = f.info.familyName + " " + f.info.styleName
    
    print(fontName)
    
    for g in accentsToClean:
        for a in f[g].anchors:
            if a.name == anchorToRemove:
                f[g].removeAnchor(a)
                
                print(f"{a.name} removed from {g}")
    
    
    
    f.save()
    f.close()