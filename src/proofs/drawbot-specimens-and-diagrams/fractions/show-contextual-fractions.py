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


def words(string,frac=False):
    fill(1)
    fontSizeLg = H*.2825
    font(fontFam, fontSizeLg)
    fontSize(fontSizeLg)

    openTypeFeatures(frac=False, case=True)

    if frac:
        openTypeFeatures(frac=True, case=True)

    text(string, (W/2, H*0.375),align="center")


def outOfTen(n):
    return n % 10

def animation(frames, frac=False):
    for frame in range(frames):
        newPage(W,H)

        f = frame / frames
        t = frame / frames
        if t <= 0.5:
            f *= 2
        else:
            f = 1 - (f - 0.5) * 2

        if frame % 2 == 0:
            outOfTen = int(frame/2) % 10
            two   = (outOfTen+1) % 10
            three = (outOfTen+2) % 10
            four  = (outOfTen+3) % 10

        wghtVal = interpolate(1000,300, f)
        caslVal = interpolate(0, 1, f)
        monoVal = interpolate(0, 1, f)

        fontVariations(wght=wghtVal,CASL=caslVal, MONO=monoVal)

        fill(0)
        rect(0,0,W,H)
        words(f"{outOfTen}{two}/{three}{four}", frac)


animation(frames)

animation(frames, True)


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