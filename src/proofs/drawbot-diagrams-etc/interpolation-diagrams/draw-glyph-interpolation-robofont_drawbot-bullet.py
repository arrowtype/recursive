f = CurrentFont()
rect(0,0,1000,1000)
# glyphName = "bullet"
glyphName = "S"

pointsDict = {}

def normalRGB(r, g, b):
    r1, g1, b1 = r / 255, g / 255, b / 255
    return((r1, g1, b1))

#TODO: animate, with axis values

# TODO: it would be better to grab the glyph box for this
glyph1Pos = (-14, 58) #(200,200) 
glyph2Pos = (566, 416) # (200,200)

glyphNum =0

scale(.85)

## TODO: make into a function(?) to put second cap on top
## currently works okay for cap in two fonts
for f in AllFonts():

    save()
    strokeWidth(2)
    if glyphNum == 0:
        translate(glyph1Pos[0],glyph1Pos[1])
        
        glyphColor = normalRGB(83, 59, 230)
        fill(glyphColor[0],glyphColor[1],glyphColor[2],0.2)
        stroke(glyphColor[0],glyphColor[1],glyphColor[2],0.75)
        
    if glyphNum == 1:
        translate(glyph2Pos[0],glyph2Pos[1])
        
        glyphColor = normalRGB(210, 46, 237)
        fill(glyphColor[0],glyphColor[1],glyphColor[2],0.15)
        stroke(glyphColor[0],glyphColor[1],glyphColor[2],0.6)
    # save()
    # scale(.75)
   
    g = f[glyphName]
    drawGlyph(g)
    

    for c in g:
        for p in c.points:
            # print(p)
            # help(p)
            # for p in s:
            pointsColor = normalRGB(210, 46, 237)
            # fill(pointsColor[0],pointsColor[1],pointsColor[2],.5)
            fill(1,1,1,.5)
            strokeWidth(2)
            # stroke(pointsColor[0],pointsColor[1],pointsColor[2])
            stroke(1,1,1)
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
            #     fill(1,1,1)
            #     oval(p.x-2.5, p.y-2.5, 5, 5)
                #TODO? draw handles
            # print(p.type)
    restore()
    # translate(500,300)
    glyphNum += 1

### figure out how to translate first glyph and its points to some location, and the next glyph and its points to another location.


for point, coordinates in pointsDict.items():
        
    # stroke(0.5,0.5,0.5, 1)
    stroke(1,1,1, .75)
    
    x1, y1 = (coordinates[0][0] + glyph1Pos[0], coordinates[0][1] + glyph1Pos[1])
    
    x2, y2 = (coordinates[1][0] + glyph2Pos[0], coordinates[1][1] + glyph2Pos[1])
    # strokeWidth(2)
    print((coordinates[0][0], coordinates[0][1]),(coordinates[1][0], coordinates[1][1]))

    lineDash(4)
    strokeWidth(2)
    line((x1,y1),(x2,y2))
    
print(pointsDict)

# saveImage("recursive-interpolation-diagram-S.pdf")