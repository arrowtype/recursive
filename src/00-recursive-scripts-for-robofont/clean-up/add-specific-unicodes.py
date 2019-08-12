from vanilla.dialogs import *
files = getFile("Select files to check for character set similarity", allowsMultipleSelection=True, fileTypes=["ufo"])

for file in files:
    f = OpenFont(file, showInterface=False)
    
    print("\n",f.info.styleName)
    
    ## commaaccentcomb
    if "commaaccentcomb" in f.keys():
        print(f["commaaccentcomb"].unicodes)       

    if f["commaaccentcomb"].unicodes is not (806,):
        f["commaaccentcomb"].unicodes = (806,) 
        print("unicode added to /commaaccentcomb")
         
    
    # ## dotbelowcomb
    # if "dotbelowcomb" in f.keys():
    #     print(f["dotbelowcomb"].unicodes)       
    
    # if f["dotbelowcomb"].unicodes is not (803,):
    #     f["dotbelowcomb"].unicodes = (803,) 
    #     print("unicode added to /dotbelowcomb")
        
    # for g in f:
    #     for comp in g.components:
    #         # print(comp)
    #         if comp.baseGlyph == "dotaccentcmb":
    #             print(comp.baseGlyph)
    #             comp.baseGlyph = "dotaccentcomb"
    #             print(comp.baseGlyph)

    # ## DOTACCENTCOMB
    # if "dotaccentcomb" in f.keys():
    #     print(f["dotaccentcomb"].unicodes)       
    # if "dotaccentcmb" in f.keys():
    #     print(f["dotaccentcmb"].unicodes)
    #     f["dotaccentcmb"].name = "dotaccentcomb"
    
    # if f["dotaccentcomb"].unicodes is not (775,):
    #     f["dotaccentcomb"].unicodes = (775,) 
        
    # for g in f:
    #     for comp in g.components:
    #         # print(comp)
    #         if comp.baseGlyph == "dotaccentcmb":
    #             print(comp.baseGlyph)
    #             comp.baseGlyph = "dotaccentcomb"
    #             print(comp.baseGlyph)
                
    # ## CEDILLACOMB

    # if "cedillacomb" in f.keys():
    #     print(f["cedillacomb"].unicodes)       
    #     print(f["cedillacomb"].name)
    
    # if f["cedillacomb"].unicodes is not (807,):
    #     f["cedillacomb"].unicodes = (807,)
        
    f.save()
    f.close()
