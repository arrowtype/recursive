import datetime
import os
import sys

currentDir = os.path.dirname(os.path.abspath(__file__))


saveOutput = True
outputDir = "exports"
docTitle = "recursive-interpolation"
fileFormat = "png"

scaling = 1.5

W, H = 1000 * scaling,1000 * scaling

newPage(W, H)

scale(scaling)

f = CurrentFont()
fill(1)
rect(0,0,W, H)
# glyphName = "bullet"
glyphName = "R"
startFont = "/Users/stephennixon/type-repos/recursive/src/masters/mono/Recursive Mono-Casual A Slanted.ufo"
endFont = "/Users/stephennixon/type-repos/recursive/src/masters/mono/Recursive Mono-Linear C.ufo"

f1 = OpenFont(startFont, showInterface=False)
f2 = OpenFont(endFont, showInterface=False)

pointsDict = {}
handlesDict = {}

#TODO: animate, with axis values

# TODO: it would be better to grab the glyph box for this

glyph1 = f1[glyphName]
glyph2 = f2[glyphName]



glyph1Pos = (-14, 58) #(200,200) 
glyph2Pos = (600, 478) # (200,200)


scale(.82)
lineCap("round")




def hex2rgb(hex):
    h = hex.lstrip('#')
    RGB = tuple(int(h[i:i+2], 16) for i in (0, 2 ,4))
    r1, g1, b1 = RGB[0] / 255, RGB[1] / 255, RGB[2] / 255
    return(r1, g1, b1)

colors = {
    "points": hex2rgb("#0020aa"), # primary blue
    "offcurvePoints":  hex2rgb("#0050FF"),
    "pointFill": hex2rgb("#ffffff"),      
    "handles": hex2rgb("#0050FF"),   
    "background": hex2rgb("#080822"),        # dark blue
    "glyphBox": hex2rgb("#080811"), #(0,0,0),
    "glyphFill": (*hex2rgb("#000000"),0.05),
    "glyphStroke": (*hex2rgb("#000000"),0.5), #hex2rgb("#B3CAFF"),
    "guides": hex2rgb("#080822"), #hex2rgb("#003099"),
    "labels": (0,0,0),
    "connections": hex2rgb("#0050FF")
}



fonts = [f1, f2]

glyphNum =0
## TODO: make into a function(?) to put second cap on top
## currently works okay for cap in two fonts
for f in fonts:

    save()
    strokeWidth(2)
    if glyphNum == 0:
        translate(glyph1Pos[0],glyph1Pos[1])
        fill(*colors["glyphFill"])
        stroke(*colors["glyphStroke"])
        
    if glyphNum == 1:
        translate(glyph2Pos[0],glyph2Pos[1])
        fill(*colors["glyphFill"])
        stroke(*colors["glyphStroke"])

    g = f[glyphName]
    drawGlyph(g)
    

    for c in g:
        for p in c.bPoints:
            if p.type == "curve" or p.type == "corner":

                ## because p.index is unexpected only giving index within loop, not overall glyph
                pointName = str(c.index) + ", " + str(p.index)
                if pointName in pointsDict:
                    pointsDict[pointName].append((p.anchor[0],p.anchor[1]))
                else:
                    pointsDict[pointName] = [(p.anchor[0],p.anchor[1])]
                

            ### draw offcurve points and handles
            
            # if in and out are not 0, 0
            
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


# oncurve connections
for point, coordinates in pointsDict.items():
    stroke(*colors["connections"], 1)
    x1, y1 = (coordinates[0][0] + glyph1Pos[0], coordinates[0][1] + glyph1Pos[1])
    x2, y2 = (coordinates[1][0] + glyph2Pos[0], coordinates[1][1] + glyph2Pos[1])
    lineDash(4)
    strokeWidth(2)
    line((x1,y1),(x2,y2))
    
# offcurve connections
for point, coordinates in handlesDict.items():
    stroke(*colors["connections"], .25)
    x1, y1 = (coordinates[0][0] + glyph1Pos[0], coordinates[0][1] + glyph1Pos[1])
    x2, y2 = (coordinates[1][0] + glyph2Pos[0], coordinates[1][1] + glyph2Pos[1])
    lineDash(4)
    strokeWidth(2)
    line((x1,y1),(x2,y2))
    
glyphNum = 0
lineDash(0)

for f in fonts:
    save()    
    g = f[glyphName]
    
    if glyphNum == 0:
        translate(glyph1Pos[0],glyph1Pos[1])
        
    if glyphNum == 1:
        translate(glyph2Pos[0],glyph2Pos[1])

    for c in g:
        for p in c.bPoints:
            
            ### draw offcurve points and handles
            
            # handles
            strokeWidth(2)
            stroke(*colors["handles"])
            line((p.anchor[0],p.anchor[1]),(p.anchor[0]+p.bcpIn[0],p.anchor[1]+p.bcpIn[1]))
            line((p.anchor[0],p.anchor[1]),(p.anchor[0]+p.bcpOut[0],p.anchor[1]+p.bcpOut[1]))    
            
            # offcurve points
            stroke(*colors["offcurvePoints"])
            strokeWidth(3)
            if (p.bcpIn[0], p.bcpIn[1]) != (0,0):
                oval(p.anchor[0]+p.bcpIn[0]-1.5,p.anchor[1]+p.bcpIn[1]-1.5,3,3)
            if (p.bcpOut[0], p.bcpOut[1]) != (0,0):
                oval(p.anchor[0]+p.bcpOut[0]-1.5,p.anchor[1]+p.bcpOut[1]-1.5,3,3)
            
            ### draw points
            
            fill(*colors["pointFill"])
            strokeWidth(2)
            stroke(*colors["points"])
            if p.type == "curve" or p.type == "corner":            
                oval(p.anchor[0]-5,p.anchor[1]-5,10,10)
                
    restore()
    # translate(500,300)
    glyphNum += 1

    
#print(handlesDict)

now = now = datetime.datetime.now().strftime("%Y_%m_%d-%H_%M_%S")

# if saveOutput:
#     saveImage(f"Desktop/recursive-interpolation-diagram-{glyphName}-{now}.png")
    
# ------------
# save image
# ------------

if saveOutput:
    import datetime

    now = datetime.datetime.now().strftime("%Y_%m_%d-%H_%M") # -%H_%M_%S

    if not os.path.exists(f"{currentDir}/{outputDir}"):
        os.makedirs(f"{currentDir}/{outputDir}")

    path = f"{currentDir}/{outputDir}/{docTitle}-{now}.{fileFormat}"

    print("saved to ", path)

    saveImage(path)
