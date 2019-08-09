# make flipbook pages for an animated specimen
# https://codepen.io/thundernixon/pen/wVypxe?editors=1100

import datetime
from fontTools.misc.bezierTools import splitCubicAtT


# fontFam = "Rec Mono Beta013 Var"

fontFam = "./fonts/Recursive-mono-full--w_ital_slnt-2019_07_25.ttf"
frames = 100
format = "gif"

frontmatter = False
debug = True

bookSize = 3.5
DPI = 150
pixels = DPI*bookSize



W, H = pixels, pixels # size is 72 dpi * bookSize



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
    
# # ---------------------------------------------------------
# # FRONTMATTER ---------------------------------------------

if frontmatter:

    textSize = H/40
    lineSize = textSize * 1.5

    newPage(W, H)
    fill(0)
    rect(0,0,W,H)

    font(fontFam)
    fontSize(textSize)
    lineHeight(lineSize)
    fontVariations(wght=500)

    fill(1)
    textBox("\
Recursive is a versatile new variable font from Arrow Type & Google Fonts, inspired by single-stroke casual signpainting but designed for screens. Five variation axes (Proportion, Expression, Weight, Slant, & Italic) allow extreme customizability, while named instances offer predetermined styles for ease of use. \n\n\
The Proportion axis allows selection between two subfamilies: Mono & Sans (or anything in between). All other axes allow control over font styles without changing the width of glyphs. This allows smooth typographic transitions without affecting line length, enabling new levels of typographic flexibility & interaction.\n\n\
Recursive is licensed under the SIL Open Font License, making it free & easy to use in any project.\
    ", (W*0.1, H*0.1, W*0.8, H*0.75))

    # PAGE TWO

    newPage(W, H)
    fill(0)
    rect(0,0,W,H)

    font(fontFam)
    fontSize(textSize)
    lineHeight(lineSize)
    fontVariations(wght=500)

    fill(1)
    textBox("\
Type design by Stephen Nixon, with contributions from Katja Schimmel, Lisa Huang, and Rafał Buchner, plus early guidance from faculty and visiting instructors at KABK TypeMedia. Type mastering by Ben Kiel.\n\n\
Started at TypeMedia, 2018. Sponsored by Google Fonts, 2019.\n\n\
Book design by Math Practice.\n\
Typeset with Drawbot by Stephen Nixon.\n\n\
https://recursive.design\n\n\
Made by friends of Google Fonts (logo)\n\n\
Recursive Sans \t Arrow Type\
    ", (W*0.1, H*0.1, W*0.8, H*0.75))

# ---------------------------------------------------------
# ANIMATION -----------------------------------------------

for frame in range(frames):
    
    newPage(W, H)
    font(fontFam)
    # font("fonts/Recursive-mono-full--w_ital_slnt-2019_07_24.ttf")
    
    frameDuration(1/60)
    fill(0)
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
    
    # TODO: split into quarters for smoother weight progression
    
    # if in first half of frames
    if frame <= frames*0.5:
        
        minXprn = 0.01
        maxXprn = 1
        
        minWeight = 300.01
        maxWeight = 900 - 0.01
        
        minSlnt = 0.01
        maxSlnt = -15
        
        currentItal = 0
                
        # completionOnCurve = y / H * 0.5
        completionOnCurve = y / pixels * 2
        
        
        
    if frame > frames*0.5:
        minXprn = 1
        maxXprn = 0
        
        minWeight = 900 - .01
        maxWeight = 300 + 0.01
        
        minSlnt = -15
        maxSlnt = 0
        
        currentItal = 1
        
        completionOnCurve = (y - 0.5) / pixels * 2 -1
        
    # if frame > frames * 0.6:
        
    #     currentItal = 1
    
    
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
    text("rw", (W/15, H/12))
    
    fontSize(W/30)
    
    padding = 0.1
    # text(str(round(currentWeight)), (((W*0.1)+(W*completionOnCurve * 0.7)), H *0.7))
    
    x = str('{:4.2f}'.format(currentXprn))
    w = str('{:3.0f}'.format(currentWeight))
    s = str('{:5.2f}'.format(currentSlnt))
    i = str('{:4.2f}'.format(currentItal))
    text(f"p {str(0)}   x {x}   w {w}   s {s}   i {i}", (((W*0.025)), H *0.025))  

    if debug:
        fill(1,0,1,1)
        size = pixels/pixels * 2
        rect(0,H*.66, W*y/W, size)      # y - curved

        for frame in range(frames):
            t = frame / frames
            size = pixels/pixels * 4
            oval(loc[0]-size/2, (y/2)+(H/12)-(size/2), size, size)


now = datetime.datetime.now().strftime("%Y_%m_%d-%H_%M") # -%H_%M_%S

saveImage("./exports/recursive-flipbook-" + now + "." + format)