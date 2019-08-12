from drawBot import * # requires drawbot to be installed as module
import datetime
from fontTools.misc.bezierTools import splitCubicAtT
newDrawing() # for drawbot module

# ---------------------------------------------------------
# CONFIGURATION -------------------------------------------

debug = True # overlays curve visualizations

prop = 1

if prop is 1:
    fontFam = "/Users/stephennixon/type-repos/recursive/src/proofs/drawbot-diagrams-etc/flipbook/fonts/Recursive-sans--w_ital_slnt-2019_08_12.ttf"
else:
    fontFam = "/Users/stephennixon/type-repos/recursive/src/proofs/drawbot-diagrams-etc/flipbook/fonts/Recursive-mono-full--w_ital_slnt-2019_07_25.ttf"

frames = 100 # currently must be in units of 100
format = "gif" # pdf, gif, or mp4

bookSize = 3.5 # inches
DPI = 144 # dots per inch
pixels = DPI*bookSize

W, H = pixels, pixels # do not edit this

textSize = W/30
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
    f = y / pixels
    # Use this value to interpolate between the start and end values on your axis
    value = interpolate(axMin, axMax, f)
    return value, x, y

# def getSlntValue(t):

#     curviness = 2
#     # curve = getCurve(curviness) # your curve for "slnt" goes here

#     curve = ((0,0), (pixels*curviness, 0), (pixels-(pixels*curviness),pixels), (pixels,pixels))
#     split = splitCubicAtT(*curve, t)
#     x, y = split[0][-1]
#     # Scale the y value to the range of 0 and 1, assuming it was in a range of 0 to 1000
#     f = y / H
#     # Use this value to interpolate between the start and end values on your axis
#     value = interpolate(0, -15, f)
#     return value

# def getWghtValue(t):

#     curviness = 0.5
#     # curve = getCurve(curviness) # your curve for "slnt" goes here

#     curve = ((0,0), (pixels*curviness, 0), (pixels-(pixels*curviness),pixels), (pixels,pixels))
#     split = splitCubicAtT(*curve, t)
#     x, y = split[0][-1]

#     print("x,y is ", split[0][-1])
#     # Scale the y value to the range of 0 and 1, assuming it was in a range of 0 to 1000
#     f = y / H
#     # Use this value to interpolate between the start and end values on your axis
#     value = interpolate(300, 900, f)
#     return value

# (you would of course need an interpolate() function for this, let me know if you need one for a linear interpolation)

# With three of these, that have their own curves and their own ranges in the interpolate() line, it's easy to just do something like this:
newPage(W, H)

fill(0)
rect(0,0,W,H)

for frame in range(frames):

    # newPage(W, H)
    

    t = frame / (frames - 1)
    # xprnValue = getXprnValue(t)
    # wghtValue = getWghtValue(t)
    # slntValue = getSlntValue(t)
    ## and then go right ahead and draw this frame
    ## just use these three values to format the text and draw the sliders

    # slntVal = getSlntValue(t)
    # wghtVal = getWghtValue(t)
    slntVal = getAxisValue(t, 0.25, 0, -15)
    wghtVal = getAxisValue(t, 3, 300, 900)
    xprnVal = getAxisValue(t, 1.4, 0, 1)

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

    text("yo", (slntVal[1], slntVal[2]))
    
    # y = H * (((wghtVal - 300) / 600))
    # oval(x-size/2, (y)-(size/2), size, size)
    text("wtf", (wghtVal[1], wghtVal[2]))
    # text("wtf", (x + 30, y))

    text("nice", (xprnVal[1], xprnVal[2]))


    
    # for i in range(frames):
    #     fill(0.6,0.6,0.6,0.375)  
    #     t = i / (frames - 1)
    
    #     slntVal = getSlntValue(t)
    
    
    #     x,y = getCurveXY(t)
    #     oval(x-size/2, (y)-(size/2), size, size)


now = datetime.datetime.now().strftime("%Y_%m_%d-%H_%M") # -%H_%M_%S

saveImage("/Users/stephennixon/type-repos/recursive/src/proofs/drawbot-diagrams-etc/flipbook/exports/multi-timing-curves-" + now + "." + format)

endDrawing()