import datetime
import sys
import os

# currentDir = sys.argv[0]
currentDir = os.path.dirname(os.path.abspath(__file__))
print(currentDir)

# ---------------------------------------------------------
# CONFIGURATION -------------------------------------------


docTitle = "interp_anime" # update this for your output file name
save = False
outputDir = "exports"
autoOpen = True

fileFormat = "mp4" # pdf, gif, or mp4 # if just 1 frame, can also be jpg or png

frames = 5
pageSize = 4 # inches
DPI = 72 # dots per inch
paddingInPts = 0

colors = {
	"points": (100,100,100),
	"offcurvePoints": (0,0,0),
    "background": (0,0,0)
}

interpolateChar = "n"

# the two master fonts
f1 = AllFonts().getFontsByStyleName('Mono Casual A')[0]
f2 = AllFonts().getFontsByStyleName('Sans Linear C')[0]




# ----------------------------------------------
# Helper functions

def normalRGB(r, g, b):
    """Use like: fill(*normalRGB(255,255,255))"""
    r1, g1, b1 = r / 255, g / 255, b / 255
    return((r1, g1, b1))


pixels = DPI*pageSize # do not edit
W, H = pixels, pixels # do not edit
padding = DPI*paddingInPts/72 # do not edit


f = CurrentFont()
fill(*normalRGB(*colors["background"]))
rect(0,0,W, H)
# glyphName = "bullet"
glyphName = "R"

pointsDict = {}

handlesDict = {}





# TODO: it would be better to grab the glyph box for this
glyph1Pos = (-14, 58) #(200,200) 
glyph2Pos = (566, 416) # (200,200)



scale(.85)
lineCap("round")


glyphNum =0
## TODO: make into a function(?) to put second cap on top
## currently works okay for cap in two fonts
for f in [f1, f2]:

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

    
    
   
    g = f[interpolateChar]
    drawGlyph(g)

    for c in g:
        for p in c.bPoints:
            pointsColor = normalRGB(*colors["points"])
            fill(*pointsColor,.5)
            strokeWidth(2)
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
            
            offcurvePointsColor = normalRGB(*colors["offcurvePoints"])
            fill(*offcurvePointsColor,0.5)
            stroke(*offcurvePointsColor,1)
            strokeWidth(3)
            
            if (p.bcpIn[0], p.bcpIn[1]) != (0,0):
                oval(p.anchor[0]+p.bcpIn[0]-1.5,p.anchor[1]+p.bcpIn[1]-1.5,3,3)
            if (p.bcpOut[0], p.bcpOut[1]) != (0,0):
                oval(p.anchor[0]+p.bcpOut[0]-1.5,p.anchor[1]+p.bcpOut[1]-1.5,3,3)
            
            strokeWidth(2)
            stroke(*offcurvePointsColor,.75)
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

for frame in frames:
    
    factor = frame/frames
    
    interpolated_glyph = RGlyph()
    interpolated_glyph.interpolate(factor, f1[interpolateChar], f2[interpolateChar])

    drawGlyph(interpolated_glyph)


# now = now = datetime.datetime.now().strftime("%Y_%m_%d-%H_%M_%S")

# saveImage(f"Desktop/recursive-interpolation-diagram-{glyphName}-{now}.png")

if save:
    import datetime

    now = datetime.datetime.now().strftime("%Y_%m_%d-%H_%M") # -%H_%M_%S

    if not os.path.exists(f"{currentDir}/{outputDir}"):
        os.makedirs(f"{currentDir}/{outputDir}")

    path = f"{currentDir}/{outputDir}/{docTitle}-{now}.{fileFormat}"

    print("saved to ", path)

    saveImage(path)

    if autoOpen:
        os.system(f"open --background -a Preview {path}")