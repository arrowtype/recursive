g = CurrentGlyph()

for a in g.anchors:
    if a.name == None:
        g.removeAnchor(a)