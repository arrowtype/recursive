"""
    Make an animation to show contextual fractions in Recursive.

    Rendered with ColdType. See https://github.com/goodhertz/coldtype/issues/7 for installation instructions.

    Then

    coldtype <path>/show-contextual-fractions.py -db -w
"""

import os 
from drawBot import *             # requires drawbot to be first installed as module
newDrawing()                      # required by drawbot module

docTitle = "contextual-fractions" # update this for your output file name
save = True
outputDir = "exports"
autoOpen = True
debug = False


currentDir = os.path.dirname(os.path.abspath(__file__))
print(currentDir)        

W,H = 1080,1080

fontFam = f"{currentDir}/Recursive_VF_1.061.ttf" # Update as needed. Easiest when font file is in same directory.
# fontFam = f"{currentDir}/Recursive_VF_1.039.ttf" # Update as needed. Easiest when font file is in same directory.

frames = 32
fps = 3
frameRate = 1/fps # only applicable to mp4 and gif; can be buggy
fileFormat = "gif" # pdf, gif, or mp4

pageSize = 3.5 # inches
DPI = 450 # dots per inch

paddingInPts = 18

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


# ----------------------------------------------
# composition

# font(fontFam, 72)



font(fontFam, 72)
fontSizeLg = H*.2825

def words(string,frac=False, afrc=False):
    fill(1)
    
    font(fontFam, fontSizeLg)
    fontSize(fontSizeLg)

    openTypeFeatures(frac=False, case=True)

    if frac:
        openTypeFeatures(frac=True, case=True)
    
    if afrc:
        openTypeFeatures(afrc=True, case=True, ss10=True)

    text(string, (W/2, H*0.375),align="center")

def metadata(wghtVal, caslVal, monoVal):
    fill(1)
    font(fontFam, 20)
    fontVariations(wght=500,CASL=1, MONO=1)
    text(f"MONO: {str(monoVal)}", (padding, H*0.1))
    text(f"CASL: {str(caslVal)}", (padding+W*.33, H*0.1))
    text(f"wght: {str(wghtVal)}", (padding+W*.66, H*0.1))

def fracState(frac=False, afrc=False):
    font(fontFam, fontSizeLg/3)
    fontVariations(wght=300,CASL=0, MONO=1)
    if frac:
        fill(0,0.1,1)
        text(f"☑ frac", (padding, H*0.75),align="left")
        fill(0.25)
        text(f"☐ afrc", (W/2+padding, H*0.75),align="left")
    if afrc:
        fill(0.25)
        text(f"☐ frac", (padding, H*0.75),align="left")
        fill(0,0.1,1)
        text(f"☑ afrc", (W/2+padding, H*0.75),align="left")
    if frac == False and afrc == False:
        fill(0.25)
        text(f"☐ frac", (padding, H*0.75),align="left")
        text(f"☐ afrc", (W/2+padding, H*0.75),align="left")

one = 0
two = 0
three = 0
four = 0

def animation(frames, one, two, three, four, frac=False, afrc=False):
    for frame in range(frames):
        newPage(W,H)

        fill(0)
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

        wghtVal = interpolate(1000,300, f)
        caslVal = interpolate(0, 1, f)
        monoVal = 1
        if frac or afrc:
            monoVal = interpolate(0, 1, f)

        fontVariations(wght=wghtVal,CASL=caslVal, MONO=monoVal)
        words(f"{one}{two}/{three}{four}", frac, afrc)

        metadata(wghtVal, caslVal, monoVal)

        fracState(frac,afrc)

# TODO: make "slider" visualization of axes
# TODO: add loop with "afrc"
# TODO: offset weight & casl from mono



animation(frames,one, two, three, four)

animation(frames,one, two, three, four, frac=True)

animation(frames,one, two, three, four, afrc=True)


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