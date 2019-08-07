# make flipbook pages for an animated specimen
# https://codepen.io/thundernixon/pen/wVypxe?editors=1100

import datetime
from fontTools.misc.bezierTools import splitCubicAtT

debug = True

bookSize = 3.5
DPI = 150
pixels = DPI*bookSize




W, H = pixels, pixels # size is 72 dpi * bookSize

frames = 80

minWeight = 300.01
maxWeight = 899.99

minExpression = 0.01
maxExpression = 1

maxSlant = 0
minSlant = -15

# def ease(t):
#     # easingCurve = ((a,a), (b*0.5,a), (b*0.5,b), (b,b))
#     easingCurve = ((0,0), (pixels/2,0), (pixels/2,pixels), (pixels,pixels))
#     split = splitCubicAtT(*easingCurve, t)
#     loc = split[0][-1]
#     y = loc[1]
#     return(y)
    

def interp(a, b, t):
    distance = b-a
    return(a + distance * t)

for frame in range(frames):
    
    newPage(W, H)
    
    # font("fonts/Recursive-mono-full--w_ital_slnt-2019_07_24.ttf")
    font("Rec Mono Beta013 Var")
    frameDuration(1/60)
    rect(0,0,W,H)
    t = frame / frames
    # split = splitCubicAtT(*easingCurve, t)
    
    easingCurve = ((0,0), (pixels/2,0), (pixels/2,pixels), (pixels,pixels))
    split = splitCubicAtT(*easingCurve, t)
    loc = split[0][-1]
    y = loc[1]
    
    # loc = split[0][-1]
    
    fill(1)
    
    # completionOnCurve = ease(t)
    
    # if in first half of frames
    # if frame < frames*0.5:
    #     minWeight = 300.01
    #     maxWeight = 800
        
    #     completionOnCurve = completionOnCurve / W /2
        
    # else:
    #     minWeight = 800
    #     maxWeight = 900
        
    #     completionOnCurve = completionOnCurve
    
    completionOnCurve = y / pixels
    
    currentWeight = interp(minWeight, maxWeight, completionOnCurve)
    
    fontVariations(
        wght=currentWeight
        )
        
    fontSize(W/1.4)
    text("rw", (W/16, H/12))
    
    fontSize(W/20)
    text(str(round(currentWeight)), ((W*0.1)+(W*completionOnCurve*0.7), H*.7))
    
    
    if debug:
        size = pixels/pixels * 2
        rect(0,H*.66, W*y/W, size)      # y - curved
        # rect(0,H*.33, W*t, 10)             # t – linear
        print("frame: ".ljust(10), frame)
        print("t: ".ljust(10), t)
        print("y: ".ljust(10), y, "\n")
        for frame in range(frames):
            t = frame / frames
            # split = splitCubicAtT(*easingCurve, t)    
            # loc = split[0][-1]
            
            oval(loc[0]-size/2, y-size/2, size, size)

# interpolate axis function

# for page in range(0,pages):
#     newPage(W, H)
    
#     t = page/pages
    
    
#     # currentWeight = weights[page]
#     # currentExpression = expressions[page]*0.001 + 0.001

#     currentRate = 360 * t
    
#     angle = 360 * t

#     angle += t * 360

#     y = 250 + amplitude * sin(radians(angle))

#     print("page: ".ljust(10), page)
#     print("t: ".ljust(10), t)
#     print("angle: ".ljust(10), angle)
#     print("y: ".ljust(10), y, "\n")
#     rect(100, y/2, 10, 10)
    
#     fontVariations(
#         wght=currentWeight, 
#         XPRN=currentExpression,
#         slnt=-15*currentExpression
#         )
#     text("rw", (W/16, H/12))


now = datetime.datetime.now().strftime("%Y_%m_%d-%H_%M")

saveImage("./exports/recursive-flipbook-" + now + ".gif")