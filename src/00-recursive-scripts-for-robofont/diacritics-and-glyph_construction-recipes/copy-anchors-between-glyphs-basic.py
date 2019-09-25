for f in AllFonts():
    
    # find location of bottom anchor in T
    # add bottom anchor to Y

    for a in f["T"].anchors:
        if a.name == "bottom":
            dotLoc = a.position
            print(dotLoc)
    
    Yanchors = []
    print(f["Y"].anchors)
    
    for a in f["Y"].anchors:
        Yanchors.append(a.name)
  
    print(Yanchors)  
    if "bottom" not in Yanchors:
       f["Y"].appendAnchor("bottom", dotLoc)
    
    # find location of hook anchor in O
    # add hook anchor to Y
    
    for a in f["O"].anchors:
        if a.name == "hook":
            hookLoc = a.position
            print(hookLoc)
    
    Yanchors = []
    print(f["Y"].anchors)
    
    for a in f["Y"].anchors:
        Yanchors.append(a.name)
  
    print(Yanchors)  
    if "hook" not in Yanchors:
       f["Y"].appendAnchor("hook", hookLoc)