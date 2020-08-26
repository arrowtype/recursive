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

fontFam = f"{currentDir}/Recursive_VF_1.060.ttf" # Update as needed. Easiest when font file is in same directory.
# fontFam = f"{currentDir}/Recursive_VF_1.039.ttf" # Update as needed. Easiest when font file is in same directory.

frames = 4
fps = 3
frameRate = 1/fps # only applicable to mp4 and gif; can be buggy
fileFormat = "pdf" # pdf, gif, or mp4

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


def words(string):
    fill(1)
    fontSizeLg = H*.325
    fontVariations(wght=800,CASL=0.99, MONO=0)
    openTypeFeatures(frac=True)
    font(fontFam, fontSizeLg)
    fontSize(fontSizeLg)
    # do your usual drawbot stuff here
    # text("1/3", (500,500))
    text(string, (W/2, H/2),align="center")

# words("24/7")



def drawFraction(string, frame, r=1,g=1,b=1, info=False):

    blendMode("screen")
    txt = FormattedString()
    fontSizeLg = H*.5
    offset = H*-0.375
    txt.fill(r,g,b)
    txt.font(fontFam, fontSizeLg)
    wghtVal = interpolate(1000,300, frame)
    caslVal = interpolate(0, 1, frame)
    txt.fontVariations(wght=wghtVal,CASL=caslVal)
    txt.fontSize(fontSizeLg)
    txt.lineHeight(1.5)
    # text("♥♡", (W/2, 0-offset),align="center")

    txt.append(string)
    text(txt, (W/2, 0-offset),align="center")

    # wghtVal = interpolate(300, 1000, f)
    # caslVal = interpolate(0, 1, f)
    # fontVariations(wght=wghtVal,CASL=caslVal)
    # fontSize = fontSizeLg
    # text("♡♥", (W/2, H/2-offset*1.5), align="center")


for frame in range(frames):
    newPage(W,H)

    outOfTen = frame % 10


    fill(0)
    rect(0,0,W,H)
    words(f"{outOfTen}{outOfTen+1}/{outOfTen+2}{outOfTen+3}")
    
    # drawFraction("frac", 1, 1,0,1)


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
        os.system(f"open --background -a Preview {path}")

## not required, but functions as an instant preview
# import os
# os.system(f"open --background -a Preview {path}")