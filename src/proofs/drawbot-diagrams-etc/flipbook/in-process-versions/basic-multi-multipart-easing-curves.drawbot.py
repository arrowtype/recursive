from drawBot import * # requires drawbot to be installed as module
import datetime
from fontTools.misc.bezierTools import splitCubicAtT
newDrawing() # for drawbot module

# ---------------------------------------------------------
# CONFIGURATION -------------------------------------------

debug = True # overlays curve visualizations

prop = 0

if prop is 1:
    fontFam = "/Users/stephennixon/type-repos/recursive/src/proofs/drawbot-diagrams-etc/flipbook/fonts/Recursive-sans--w_ital_slnt-2019_08_12.ttf"
else:
    fontFam = "/Users/stephennixon/type-repos/recursive/src/proofs/drawbot-diagrams-etc/flipbook/fonts/Recursive-mono-full--w_ital_slnt-2019_08_12.ttf"

frames = 60 # currently must be in units of 100
frameRate = 1/60 # only applicable to mp4
format = "mp4" # pdf, gif, or mp4

bookSize = 3.5 # inches
DPI = 300 # dots per inch
pixels = DPI*bookSize

W, H = pixels, pixels # do not edit this
textSize = W/30

# W, H = 1080, 1920   # instagram story format
# textSize = W/10     # instagram story format

rwSize = W/1.4

# curviness = 0.7 # amount of easing steepness. 0 to 1.

padding = W*0.085714286 # 0.3 inches

# ---------------------------------------------------------
# ANIMATION -----------------------------------------------

def drawMargins():
    # top, right, bottom, left
    margins = (0.75, 0.3, 0.3, 0.3)
    thickness = 1
    fill(0,1,1)

    # x, y, w, h
    rect(0, H - margins[0]*DPI, W, thickness)  # top
    rect(margins[1]*DPI, 0, thickness, H)      # right
    rect(W - margins[2]*DPI, 0, thickness, H)  # bottom
    rect(0, margins[3]*DPI, W, thickness)      # left


def interpolate(a, b, t):
    distance = b-a
    return(a + distance * t)

# You can even make this getCurve() function do a lot more for you, I'll sketch pseudo code here:


def getCurveValue(t, curviness, axMin, axMax, loop="loop"):
    # curve = ((0,0), (W*curviness, 0), (W-(W*curviness),H), (W,H)) # fast to slow to fast (not sure?)
    curve = ((0,0), (0, H*curviness), (W,H-(H*curviness)), (W,H)) # slow to fast to slow, based on x over time (bell curve)
    # curve = ((0, 20), (-2689.98, 30), (-2000,H), (W,H))
    split = splitCubicAtT(*curve, t)
    x, y = split[0][-1]
    # Scale the y value to the range of 0 and 1, assuming it was in a range of 0 to 1000
    # f = y / H # for some reason, y isn't working as well for me as x to attain different curves...
    f = x / W
    
    # go up with curve for first half, then back down
    if loop is "loop":
        if t <= 0.5:
            f *= 2
        else:
            f = 1 - (f - 0.5) * 2
            
    value = interpolate(axMin, axMax, f)
            
    return value, x, y

def getWeightValue(t, curviness, axMin, axMax):

    curve = ((0,0), (0, H*curviness), (W,H-(H*curviness)), (W,H)) # slow to fast to slow (bell curve)
    split = splitCubicAtT(*curve, t)
    x, y = split[0][-1]
    # if t <= 0.75:
    if t <= 0.5:
        # Scale the y value to the range of 0 and 1, assuming it was in a range of 0 to 1000
        f = x / W * 2
        
        # f *= 2
        value = interpolate(axMin, 800, f)
        
    else:
        # curve = ((W/2,H), (W/2,H-(H*curviness)), (W, H*curviness),(W,0)) # slow to fast to slow (bell curve)
        # curve = ((0,0), (0, H*curviness), (W/2,H-(H*curviness)), (W/2,H)) # slow to fast to slow (bell curve)
        split = splitCubicAtT(*curve, t)
        x, y = split[0][-1]
        # Scale the y value to the range of 0 and 1, assuming it was in a range of 0 to 1000
        f = x / W
        # f = 1 - (f - 0.5) * 2 # reversed
        f = (f - 0.5) * 2 

        value = interpolate(800, axMax, f)

    return value, x, y


def getItalValue(t):
    if t <= 0.5:
        value = 0
    else:
        value = 1
    return value


for frame in range(frames):

    newPage(W, H)
    font(fontFam)
    fontSize(textSize)

    fill(0)
    rect(0,0,W,H)

    frameDuration(frameRate)
    

    t = frame / (frames - 1)

    slntVal = getCurveValue(t, 0, 0.001, -14.999)
    wghtVal = getWeightValue(t, 0.7, 300.001, 899.999)
    xprnVal = getCurveValue(t, 0.5, 0.001, 0.999)
    italVal = getItalValue(t)

    fontVariations(wght=wghtVal[0], XPRN=xprnVal[0], slnt=slntVal[0], ital=italVal)

    

    # print(round(slntVal, 2), round(wghtVal, 2))
    
    size = padding * 0.375

    # fill(1,0,0)

    # rect(0,0,100,100)
    fill(1)
    
    fontSize(rwSize)
    text("rw", (W/15, padding*2))

    # page number
    textBox(str(frame + 1), (padding, padding*0.5, (W- (padding*2)), textSize*1.5), align="right")
    
    
    if debug:
        print("T: " + str(t))
        print("-------------------------------------")
        print("#: " + str(frame))
        print("x: " + str(round(abs(xprnVal[0]), 0)))
        print("w: " + str(round(abs(wghtVal[0]), 0)))
        print("s: " + str(round(abs(slntVal[0]), 2)))
        print('')

        drawMargins()
        
        fill(1,0,1)
        fontSize(textSize/2)
        # text("t" + str(round(abs(t), 2)), (W*t, padding))
        text("@", (W*t, padding))
        text("s" + str(round(abs(slntVal[0]), 2)), (slntVal[1]-W/10, slntVal[2]+textSize))
        text("w" + str(round(wghtVal[0], 0)), (wghtVal[1]-W/10, wghtVal[2]))
        text("x" + str(round(xprnVal[0], 2)), (xprnVal[1]-W/10, xprnVal[2]-textSize))

        
        size = padding * 0.15
        x8 = getCurveValue(t, 0.8, 0, W, loop="nope")[0]
        # oval(x8-size/2, (padding/2)-(size/2), size, size)
        text("0.8", (x8-size/2, (padding/2)-(size/2)))
        
        x3 = getCurveValue(t, 0.3, 0, W, loop="nope")[0]
        text("0.3", (x8-size/2, (padding/2)-(size*1.5)))


    
    # for i in range(frames):
    #     fill(0.6,0.6,0.6,0.375)  
    #     t = i / (frames - 1)
    
    #     slntVal = getSlntValue(t)
    
    
    #     x,y = getCurveXY(t)
    #     oval(x-size/2, (y)-(size/2), size, size)


now = datetime.datetime.now().strftime("%Y_%m_%d-%H") # -%H_%M_%S

saveImage(f"/Users/stephennixon/type-repos/recursive/src/proofs/drawbot-diagrams-etc/flipbook/exports/multi-timing-curves-prop_{prop}-{now}.{format}")

endDrawing()