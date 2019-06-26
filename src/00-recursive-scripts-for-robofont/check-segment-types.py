g = CurrentGlyph()

print("FONT".ljust(18), end=" ")
print("|", end=" ")

print("CONTOURS & SEGMENTS")

for f in AllFonts():
    
    print(f.info.styleName.ljust(18), end=" ")
    print("|", end=" ")
    counter = 0
    for c in f[g.name]:
        print(f"C{counter}", end =" ") 
        for s in c:
            
            # possible segment types: move, line, curve, qcurve
            
            ## if you want to be boring:
            # print(s.type[0].upper(), end =" ")
            
            ## if you want to spot the differences more easily:
            if s.type == "line":
                print("📏", end =" ")
            elif s.type == "curve":
                print("🥐", end =" ")
            elif s.type == "move":
                print("🚚", end =" ")
            elif s.type == "qcurve":
                print("🥨", end =" ")
        print("|", end =" ")  
        counter += 1 
            
    print("")
