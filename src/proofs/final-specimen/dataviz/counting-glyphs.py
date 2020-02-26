f = CurrentFont()

total = 0
noComps = 0
handdrawn = 0
composed = 0


monoMan = 0
monoPts = 0
sansMan = 0
sansPts = 0

for g in f:   
    # some contours, 600 width    
    if len(g.contours) > 0 and g.width == 600:    
        monoMan += 1
        for c in g:
            for p in c.points:
                monoPts += 1
    if len(g.contours) > 0 and g.width != 600:
        # handdrawn += 1
        monoMan += 1
        sansMan += 1
        for c in g:
            for p in c.points:
                monoPts += 1
                sansPts += 1
    if len(g.contours) == 0 and len(g.components) > 0:
        composed += 1

print("Total glyphs in final font: ", len(f))
print("Hand drawn per Mono source: ", monoMan)
print("Hand drawn per Sans source: ", sansMan)
print("Composed glyphs per source: ", composed)

print("Drawn glyphs, all sources:  ", (monoMan * 12) + (sansMan *12))
print("Drawn points, all sources:  ", (monoPts * 12) + (sansPts*12))