import datetime

f = CurrentFont()
fill(1)
rect(0,0,1000,1000)
# glyphName = "bullet"
glyphName = "R"

pointsDict = {}

handlesDict = {}

def normalRGB(r, g, b):
    r1, g1, b1 = r / 255, g / 255, b / 255
    return((r1, g1, b1))

#TODO: animate, with axis values

# TODO: it would be better to grab the glyph box for this
glyph1Pos = (-14, 58) #(200,200) 
glyph2Pos = (566, 416) # (200,200)


scale(.85)
lineCap("round")


glyphNum =0
## TODO: make into a function(?) to put second cap on top
## currently works okay for cap in two fonts
for f in AllFonts():

    save()
    strokeWidth(2)
    if glyphNum == 0:
        translate(glyph1Pos[0],glyph1Pos[1])
        
        #glyphColor = normalRGB(84, 59, 230)
        glyphColor = normalRGB(0,0,0) # normalRGB(0, 80, 255)
        fill(glyphColor[0],glyphColor[1],glyphColor[2],0.25)
        stroke(glyphColor[0],glyphColor[1],glyphColor[2],1)
        
    if glyphNum == 1:
        translate(glyph2Pos[0],glyph2Pos[1])
        
        #glyphColor = normalRGB(210, 46, 237)
        #glyphColor = normalRGB(200,200,200) # normalRGB(0, 80, 255)
        glyphColor = normalRGB(0,0,0) # normalRGB(0, 80, 255)
        fill(glyphColor[0],glyphColor[1],glyphColor[2],0.25)
        stroke(glyphColor[0],glyphColor[1],glyphColor[2],1)
    # save()
    # scale(.75)
   
    g = f[glyphName]
    drawGlyph(g)
    

    for c in g:
        for p in c.bPoints:
            print(p)
            # help(p)
            # for p in s:
            pointsColor = normalRGB(100,100,100) #normalRGB(210, 46, 237)
            # fill(pointsColor[0],pointsColor[1],pointsColor[2],.5)
            fill(*pointsColor,.5)
            strokeWidth(2)
            # stroke(pointsColor[0],pointsColor[1],pointsColor[2])
            stroke(*pointsColor)
            if p.type == "curve" or p.type == "corner":
                
                oval(p.anchor[0]-5,p.anchor[1]-5,10,10)

                ## because p.index is unexpected only giving index within loop, not overall glyph
                pointName = str(c.index) + ", " + str(p.index)
                if pointName in pointsDict:
                    pointsDict[pointName].append((p.anchor[0],p.anchor[1]))
                else:
                    # label = str(c.index) + ", " + str(p.index)
                    pointsDict[pointName] = [(p.anchor[0],p.anchor[1])]
                

            ### draw offcurve points and handles
            
            # if in and out are not 0, 0
            
            pointsColor = normalRGB(0,0,0)
            fill(*pointsColor,0.5)
            stroke(*pointsColor,1)
            strokeWidth(3)
            
            if (p.bcpIn[0], p.bcpIn[1]) != (0,0):
                oval(p.anchor[0]+p.bcpIn[0]-1.5,p.anchor[1]+p.bcpIn[1]-1.5,3,3)
            if (p.bcpOut[0], p.bcpOut[1]) != (0,0):
                oval(p.anchor[0]+p.bcpOut[0]-1.5,p.anchor[1]+p.bcpOut[1]-1.5,3,3)
            
            strokeWidth(2)
            stroke(*pointsColor,.75)
            line((p.anchor[0],p.anchor[1]),(p.anchor[0]+p.bcpIn[0],p.anchor[1]+p.bcpIn[1]))
            line((p.anchor[0],p.anchor[1]),(p.anchor[0]+p.bcpOut[0],p.anchor[1]+p.bcpOut[1]))    
            
            inHandleName = str(c.index) + ", " + str(p.index) + ", in"
            inXCoordinate = p.anchor[0]+p.bcpIn[0]
            inYCoordinate = p.anchor[1]+p.bcpIn[1]
            if inHandleName in handlesDict:
                handlesDict[inHandleName].append((inXCoordinate,inYCoordinate))
            else:
                handlesDict[inHandleName] = [(inXCoordinate,inYCoordinate)]
                
            outHandleName = str(c.index) + ", " + str(p.index) + ", out"
            outXCoordinate = p.anchor[0]+p.bcpOut[0]
            outYCoordinate = p.anchor[1]+p.bcpOut[1]
            if outHandleName in handlesDict:
                handlesDict[outHandleName].append((outXCoordinate,outYCoordinate))
            else:
                handlesDict[outHandleName] = [(outXCoordinate,outYCoordinate)]
            
               
    restore()
    # translate(500,300)
    glyphNum += 1

### figure out how to translate first glyph and its points to some location, and the next glyph and its points to another location.


for point, coordinates in pointsDict.items():
    stroke(*pointsColor, 1)
    x1, y1 = (coordinates[0][0] + glyph1Pos[0], coordinates[0][1] + glyph1Pos[1])
    x2, y2 = (coordinates[1][0] + glyph2Pos[0], coordinates[1][1] + glyph2Pos[1])
    # strokeWidth(2)
    lineDash(4)
    strokeWidth(2)
    line((x1,y1),(x2,y2))
    
for point, coordinates in handlesDict.items():
    stroke(0,0,0, .25)
    x1, y1 = (coordinates[0][0] + glyph1Pos[0], coordinates[0][1] + glyph1Pos[1])
    x2, y2 = (coordinates[1][0] + glyph2Pos[0], coordinates[1][1] + glyph2Pos[1])
    # strokeWidth(2)
    lineDash(4)
    strokeWidth(2)
    line((x1,y1),(x2,y2))
    
print(handlesDict)

now = now = datetime.datetime.now().strftime("%Y_%m_%d-%H_%M_%S")

saveImage(f"Desktop/recursive-interpolation-diagram-{glyphName}-{now}.png")