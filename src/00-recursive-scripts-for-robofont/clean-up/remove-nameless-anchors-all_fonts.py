af = AllFonts()

for f in af:
    for g in f:
        for a in g.anchors:
            if a.name == None:
                g.removeAnchor(a)
