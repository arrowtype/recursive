# make flipbook pages for an animated specimen
# https://codepen.io/thundernixon/pen/wVypxe?editors=1100

import datetime
from fontTools.misc.bezierTools import splitCubicAtT

debug = True

bookSize = 3.5
DPI = 150
pixels = DPI*bookSize



W, H = pixels, pixels # size is 72 dpi * bookSize




frames = 200

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
    
    completionOnCurve = y / pixels
    
    # completionOnCurve = ease(t)
    
    # if in first half of frames
    if frame <= frames*0.5:
        
        minXprn = 0.01
        maxXprn = 1
        
        minWeight = 300.01
        maxWeight = 800.01
        
        minSlnt = 0.01
        maxSlnt = -15
        
        currentItal = 0
                
        # completionOnCurve = y / H * 0.5
        completionOnCurve = y / pixels * 2
        
        
        
    if frame > frames*0.5:
        minXprn = 1
        maxXprn = 0
        
        minWeight = 800.01
        maxWeight = 900 - 0.01
        
        minSlnt = -15
        maxSlnt = 0
        
        currentItal = 0
        
        completionOnCurve = (y - 0.5) / pixels * 2 -1
        
    if frame > frames * 0.75:
        
        currentItal = 0.5
    
    
    currentXprn = interp(minXprn, maxXprn, completionOnCurve)
    currentWeight = interp(minWeight, maxWeight, completionOnCurve)
    currentSlnt = interp(minSlnt, maxSlnt, completionOnCurve)
    
    fontVariations(
        wght=currentWeight,
        XPRN=currentXprn,
        slnt=currentSlnt,
        ital=currentItal
        )
    
    print(str(frame).ljust(3), " | factor: ", str(round(completionOnCurve, 3)).ljust(5)," | t: ", str(round(t, 3)).ljust(5), " | wght: ", currentWeight)
    
    fontSize(W/1.4)
    text("rw", (W/16, H/12))
    
    fontSize(W/30)
    
    padding = 0.1
    # text(str(round(currentWeight)), (((W*0.1)+(W*completionOnCurve * 0.7)), H *0.7))
    
    x = str('{:4.2f}'.format(currentXprn))
    w = str('{:3.0f}'.format(currentWeight))
    s = str('{:4.2f}'.format(currentSlnt))
    i = str('{:4.2f}'.format(currentItal))
    text(f"p {str(0)}   x {x}   w {w}   s {s}   i {i}", (((W*0.025)), H *0.025))  

    if debug:
        fill(1,0,1,1)
        size = pixels/pixels * 2
        rect(0,H*.66, W*y/W, size)      # y - curved

        for frame in range(frames):
            t = frame / frames
            size = pixels/pixels * 4
            oval(loc[0]-size/2, y-size/2, size, size)


now = datetime.datetime.now().strftime("%Y_%m_%d") # -%H_%M_%S

saveImage("./exports/recursive-flipbook-" + now + ".gif")