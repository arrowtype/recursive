for f in AllFonts():
    print(f)
    
    
    fromGlyph = "I"
    toGlyph = "Y"
    anchorToCopy = "bottom"
    
    for a in f[fromGlyph].anchors:
        if a.name == anchorToCopy:
            anchorLoc = a.position
            print(anchorLoc)
    
    toGlyphAnchors = []
    print(f[toGlyph].anchors)
    
    for i, a in enumerate(f[toGlyph].anchors):
        toGlyphAnchors.append(a.name)
        
        if a.name == anchorToCopy:
            anchorToCopyIndex = i
        
    # replaces anchor if it already exists (but may be at incorrect location)
    if anchorToCopy in toGlyphAnchors:
        f[toGlyph].removeAnchor(f[toGlyph].anchors[anchorToCopyIndex])
        f[toGlyph].appendAnchor(anchorToCopy, anchorLoc)
  
    # adds anchor if it doesn't exist
    else:
        f[toGlyph].appendAnchor(anchorToCopy, anchorLoc)

    