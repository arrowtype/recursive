# make flipbook pages for an animated specimen
# https://codepen.io/thundernixon/pen/wVypxe?editors=1100

import datetime
from fontTools.misc.bezierTools import splitCubicAtT

debug = True

bookSize = 3.5
DPI = 72
pixels = DPI*bookSize

easingCurve = ((0,0), (pixels*0.5,0), (pixels*0.5,pixels), (pixels,pixels))

W, H = pixels, pixels # size is 72 dpi * bookSize

frames = 200

# newPage(W, H)

for frame in range(frames):
    newPage(W, H)
    frameDuration(1/60)
    rect(0,0,W,H)
    t = frame / frames
    split = splitCubicAtT(*easingCurve, t)
    
    loc = split[0][-1]
    
    print("frame: ".ljust(10), frame)
    print("t: ".ljust(10), t)
    print("y: ".ljust(10), loc[1], "\n")
    
    fill(1)
    
    
    
    rect(0,H*.66, W*loc[1]/W, 10) # y - curved
    rect(0,H*.33, W*t, 10) # t – linear
    
    if debug:
        for frame in range(frames):
            t = frame / frames
            split = splitCubicAtT(*easingCurve, t)    
            loc = split[0][-1]
            size = pixels/pixels *2
            oval(loc[0]-size/2, loc[1]-size/2, size, size)

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


now = datetime.datetime.now()


saveImage("./exports/recursive-flipbook-" + now.strftime("%Y_%m_%d-%H_%M_%S") + ".mp4")