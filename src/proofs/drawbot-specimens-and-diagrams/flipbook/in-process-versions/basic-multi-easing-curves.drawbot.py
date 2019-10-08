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

frames = 500 # currently must be in units of 100
format = "mp4" # pdf, gif, or mp4

bookSize = 3.5 # inches
DPI = 144 # dots per inch
pixels = DPI*bookSize

# W, H = pixels, pixels # do not edit this
# textSize = W/30

W, H = 1080, 1920
textSize = W/10

rwSize = W/1.4

# curviness = 0.7 # amount of easing steepness. 0 to 1.

padding = W*0.025

# ---------------------------------------------------------
# ANIMATION -----------------------------------------------


def interpolate(a, b, t):
    distance = b-a
    return(a + distance * t)


# You can even make this getCurve() function do a lot more for you, I'll sketch pseudo code here:

def getAxisValue(t, curviness, axMin, axMax):
    curve = ((0,0), (W*curviness, 0), (W-(W*curviness),H), (W,H))
    # curve = ((0, 20), (-2689.98, 30), (-2000,H), (W,H))
    split = splitCubicAtT(*curve, t)
    x, y = split[0][-1]
    # Scale the y value to the range of 0 and 1, assuming it was in a range of 0 to 1000
    f = y / H
    # Use this value to interpolate between the start and end values on your axis
    value = interpolate(axMin, axMax, f)
    return value, x, y


for frame in range(frames):

    newPage(W, H)
    font(fontFam)
    fontSize(textSize)

    fill(0)
    rect(0,0,W,H)

    frameDuration(1/60)
    

    t = frame / (frames - 1)
    # xprnValue = getXprnValue(t)
    # wghtValue = getWghtValue(t)
    # slntValue = getSlntValue(t)
    ## and then go right ahead and draw this frame
    ## just use these three values to format the text and draw the sliders

    print(t)

    # slntVal = getSlntValue(t)
    # wghtVal = getWghtValue(t)
    slntVal = getAxisValue(t, 0.25, 0, -15)
    wghtVal = getAxisValue(t, 3, 300, 900)
    xprnVal = getAxisValue(t, 1.4, 0, 1)

    fontVariations(wght=wghtVal[0], XPRN=xprnVal[0], slnt=slntVal[0], ital=0.5)

    

    # print(round(slntVal, 2), round(wghtVal, 2))
    
    size = padding * 0.375

    # fill(1,0,0)

    # rect(0,0,100,100)

    fill(1)

    # (y - startPos ) / stepRange
    # x = W * t
    # y = -H * ((slntVal - 0) /15)
    # oval(x-size/2, (y)-(size/2), size, size)
    # text("yo", (x, y))

    text("yo", (slntVal[1]-W/10, slntVal[2]))
    # text("slnt\n" + str(round(slntVal[0], 2)), (slntVal[1]-W/10, slntVal[2]))
    
    # y = H * (((wghtVal - 300) / 600))
    # oval(x-size/2, (y)-(size/2), size, size)
    text("nice", (wghtVal[1]-W/10, wghtVal[2]))
    # text("wght\n" + str(round(wghtVal[0], 0)), (wghtVal[1]-W/10, wghtVal[2]))

    text("wtf", (xprnVal[1]-W/10, xprnVal[2]))
    # text("xprn\n" + str(round(xprnVal[0], 2)), (xprnVal[1]-W/10, xprnVal[2]))


    
    # for i in range(frames):
    #     fill(0.6,0.6,0.6,0.375)  
    #     t = i / (frames - 1)
    
    #     slntVal = getSlntValue(t)
    
    
    #     x,y = getCurveXY(t)
    #     oval(x-size/2, (y)-(size/2), size, size)


now = datetime.datetime.now().strftime("%Y_%m_%d-%H_%M") # -%H_%M_%S

saveImage(f"/Users/stephennixon/type-repos/recursive/src/proofs/drawbot-diagrams-etc/flipbook/exports/multi-timing-curves-prop_{prop}-{now}.{format}")

endDrawing()