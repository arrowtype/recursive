f = CurrentFont()

glyphName = "bullet"

pointsDict = {}

# TODO: it would be better to grab the glyph box for this
glyph1Pos = (400,400) #(22, 90)
glyph2Pos = (400,400) #(672, 590)

glyphNum =0

scale(.75)

## TODO: make into a funtion(?) to put second cap on top
## currently works okay for cap in two fonts
for f in AllFonts():

    save()
    if glyphNum == 0:
        translate(glyph1Pos[0],glyph1Pos[1])
    if glyphNum == 1:
        translate(glyph2Pos[0],glyph2Pos[1])
    # save()
    # scale(.75)
    fill(0,0,1,.15)
    stroke(0,0,1)
    g = f[glyphName]
    drawGlyph(g)
    

    for c in g:
        for p in c.points:
            # print(p)
            # help(p)
            # for p in s:
            fill(1,0,0,.25)
            stroke(1,0,0)
            if p.type == "curve" or p.type == "line":
                oval(p.x-5,p.y-5,10,10)

                ## because p.index is unexpected only giving index within loop, not overall glyph
                pointName = str(c.index) + ", " + str(p.index)
                if pointName in pointsDict:
                    # print("exists")
                # #     pointsDict[p.index] = []
                    pointsDict[pointName].append((p.x, p.y))
                else:
                    label = str(c.index) + ", " + str(p.index)
                    pointsDict[pointName] = [(p.x, p.y)]
                
            # if p.type == "offcurve":
            #     fill(1,0,0)
            #     oval(p.x-2.5, p.y-2.5, 5, 5)
                #TODO? draw handles
            # print(p.type)
    restore()
    # translate(500,300)
    glyphNum += 1

### figure out how to translate first glyph and its points to some location, and the next glyph and its points to another location.


for point, coordinates in pointsDict.items():
        
    stroke(0,0,0, .75)
    
    x1, y1 = (coordinates[0][0] + glyph1Pos[0], coordinates[0][1] + glyph1Pos[1])
    
    x2, y2 = (coordinates[1][0] + glyph2Pos[0], coordinates[1][1] + glyph2Pos[1])
    # strokeWidth(2)
    print((coordinates[0][0], coordinates[0][1]),(coordinates[1][0], coordinates[1][1]))

    lineDash(4)
    line((x1,y1),(x2,y2))
    
print(pointsDict)