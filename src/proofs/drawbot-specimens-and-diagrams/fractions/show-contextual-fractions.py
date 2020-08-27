"""
    Make an animation to show contextual fractions in Recursive.

    Rendered with ColdType. See https://github.com/goodhertz/coldtype/issues/7 for installation instructions.

    Then

    coldtype <path>/show-contextual-fractions.py -db -w
"""

import os 
from drawBot import *             # requires drawbot to be first installed as module
from fontTools.misc.bezierTools import splitCubicAtT
newDrawing()                      # required by drawbot module

docTitle = "contextual-fractions" # update this for your output file name
save = True
outputDir = "exports"
autoOpen = True
debug = False

currentDir = os.path.dirname(os.path.abspath(__file__))
print(currentDir)        

W,H = 1080,1080

fontFam = f"{currentDir}/Recursive_VF_1.062.ttf" # Update as needed. Easiest when font file is in same directory.
# fontFam = f"{currentDir}/Recursive_VF_1.039.ttf" # Update as needed. Easiest when font file is in same directory.

frames = 32
fps = 3
frameRate = 1/fps # only applicable to mp4 and gif; can be buggy
fileFormat = "mp4" # pdf, gif, or mp4

pageSize = 3.5 # inches
DPI = 450 # dots per inch

paddingInPts = 16


# colors

accent = (0.125,0.5,1)

# ----------------------------------------------
# Helper functions

pixels = DPI*pageSize # do not edit
# W, H = pixels, pixels # do not edit
W, H = 1080,1080 # IG square
padding = DPI*paddingInPts/72 # do not edit

# turn font size into usable value for given pageSize
def computeFontSizePoints(pts):
    return W * (pts / (pageSize * 72))

# a frequently-useful function
def interpolate(a, b, t):
    return(a + (b-a) * t)

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

# ----------------------------------------------
# composition

# font(fontFam, 72)



font(fontFam, 72)
#fontSizeLg = H*.2825
fontSizeLg = H*.271

def fraction(string, wghtVal, caslVal, monoVal, frac=False, afrc=False):

    # lines
    stroke(*accent)
    baseline = H*0.404
    line((0, baseline), (W, baseline))

    capHeight = H*0.5927
    line((0, capHeight), (W, capHeight))

    
    stroke(0,0,0,0)

    fraction = FormattedString()
    
    # fraction.fill(1)
    fraction.fontVariations(wght=wghtVal,CASL=caslVal, MONO=monoVal)
    
    fraction.font(fontFam)
    fraction.fontSize(fontSizeLg)

    fraction.openTypeFeatures(frac=False, case=True)
    fraction.align("center")

    if frac:
        fraction.openTypeFeatures(frac=True, case=True)
    
    if afrc:
        # openTypeFeatures(afrc=True, case=True, ss10=True)
        fraction.openTypeFeatures(afrc=True, case=True)

    # TODO: outline text

    fraction.append(string)

    textPath = BezierPath()
    textPath.textBox(fraction, (-W, H*0.322, W*3, fontSizeLg*1.25))
    fill(1)
    drawPath(textPath)

def metadata(wghtVal, caslVal, monoVal):

    monoNum = str('{:4.2f}'.format(monoVal))
    caslNum = str('{:4.2f}'.format(caslVal))
    wghtNum = str('{:3.0f}'.format(wghtVal))

    charWidth = 36

    wghtRate = (wghtVal-300)/(1000-300)

    # fill(1)
    fill(*accent)
    font(fontFam, 32)
    fontVariations(wght=500,CASL=1, MONO=1)
    text(f"MONO {monoNum}", (padding, H*0.175))
    text("*".rjust(int(charWidth*monoVal),"-"), (padding*2.9, H*0.175))

    text(f"CASL {caslNum}", (padding, H*0.1375))
    text("*".rjust(int(charWidth*caslVal),"-"), (padding*2.9, H*0.1375))

    text(f"wght {wghtNum.rjust(4,' ')}", (padding, H*0.1))
    text("*".rjust(int(charWidth*wghtRate),"-"), (padding*2.9, H*0.1))

def fracState(frac=False, afrc=False):
    #font(fontFam, fontSizeLg/3)
    font(fontFam, fontSizeLg/2.60)
    fontVariations(wght=300,CASL=0, MONO=1)
    fracStateHeight= H*0.82
    if frac:
        fill(*accent)
        text(f"☑ frac", (padding, fracStateHeight),align="left")
        fill(0.25)
        text(f"☐ afrc", (W-padding, fracStateHeight),align="right")
    if afrc:
        fill(0.25)
        text(f"☐ frac", (padding, fracStateHeight),align="left")
        fill(*accent)
        text(f"☑ afrc", (W-padding, fracStateHeight),align="right")
    if frac == False and afrc == False:
        fill(0.25)
        text(f"☐ frac", (padding, fracStateHeight),align="left")
        text(f"☐ afrc", (W-padding, fracStateHeight),align="right")

one = 0
two = 0
three = 0
four = 0

def animation(frames, one, two, three, four, frac=False, afrc=False):
    for frame in range(frames):
        newPage(W,H)

        fill(0.05)
        rect(0,0,W,H)

        f = frame / frames
        t = frame / frames
        if t <= 0.5:
            f *= 2
        else:
            f = 1 - (f - 0.5) * 2

        # # first col moves fastest, fourth slowest
        # if frame % 1 == 0:
        #     one = int(frame/2) % 10
        # if frame % 2 == 0:
        #     two   = (one+1) % 10
        # if frame % 3 == 0:
        #     three = (one+2) % 10
        # if frame % 4 == 0:
        #     four  = (one+3) % 10

        # update each col every fourth frame
        if frame % 4 == 0:
            one = int(frame/2) % 10
        if (frame+1) % 4 == 0:
            two   = (one+1) % 10
        if (frame+2) % 4 == 0:
            three = (one+2) % 10
        if (frame+3) % 4 == 0:
            four  = (one+3) % 10

        wghtVal = getCurveValue(t, 0.5, 1000, 300)
        caslVal = getCurveValue(t, 0.5, 0, 1)
        monoVal = (1,0,0)
        if frac or afrc:
            monoVal = getCurveValue(t, 0.5, 1, 0)

        fraction(f"{one}{two}{three}{four}{one}{two}/{three}{four}{one}{two}{three}{four}",wghtVal[0], caslVal[0], monoVal[0], frac, afrc)

        metadata(wghtVal[0], caslVal[0], monoVal[0])

        fracState(frac,afrc)

        if debug:
            stroke(1,0,1)
            fill(1,1,1,0)
            line((0,H/2),(W,H/2))
            rect(padding, padding, W-padding*2, H-padding*2)
            for count in range(4):
                rect(padding+((W-padding*2)/5)*count, padding, (W-padding*2)/5, H-padding*2)

# TODO: make numbers count 0–9 without being even/odd
# TODO: make "slider" visualization of axes
# TODO: add loop with "afrc"
# TODO: offset weight & casl from mono
# TODO: rebuild fonts & make new release


animation(frames,one, two, three, four, frac=True)

animation(frames,one, two, three, four, afrc=True)

animation(frames,one, two, three, four)



endDrawing()                      # advised by drawbot docs

if save:
    import datetime

    now = datetime.datetime.now().strftime("%Y_%m_%d-%H_%M") # -%H_%M_%S

    if not os.path.exists(f"{currentDir}/{outputDir}"):
        os.makedirs(f"{currentDir}/{outputDir}")

    path = f"{currentDir}/{outputDir}/{docTitle}-{now}.{fileFormat}"

    print("saved to ", path)

    saveImage(path)

    if autoOpen:
        os.system(f"open --background -a Safari {path}")

## not required, but functions as an instant preview
# import os
# os.system(f"open --background -a Preview {path}")