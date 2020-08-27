"""
  This is a set of Python I use many times I wish to make an animation or multipage doc with Drawbot, 
  but code in my preferred editor (currently, VS Code) rather than in the Drawbot app.
  USAGE:
  First, install DrawBot as a module:
  pip install git+https://github.com/typemytype/drawbot
  
  Adapt script as needed, then run from the command line with:
  
  python3 <path>/hearts.py
"""

from drawBot import * # requires drawbot to be installed as module
import sys
import os

newDrawing() # required by drawbot module

# currentDir = sys.argv[0]
currentDir = os.path.dirname(os.path.abspath(__file__))
print(currentDir)          

# ---------------------------------------------------------
# CONFIGURATION -------------------------------------------

docTitle = "drawbot-export" # update this for your output file name
save = True
outputDir = "exports"
autoOpen = True
debug = False

fontFam = f"{currentDir}/Recursive_VF_1.060.ttf" # Update as needed. Easiest when font file is in same directory.

frames = 1
fps = 3
frameRate = 1/fps # only applicable to mp4 and gif; can be buggy
fileFormat = "mp4" # pdf, gif, or mp4

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
# TEXT FUNCTIONS

def writeInfoTop(f, r,g,b):    
    with savedState():
        fontSizeSm = H*.025
        fontVariations(wght=500,CASL=1,MONO=1)
        font(fontFam, fontSizeSm)
        wghtVal = interpolate(600,400, f)
        caslVal = interpolate(1, 0, f)
        fontVariations(wght=wghtVal,CASL=caslVal)
        blendMode("normal")
        fill(0)
        lineHeight(fontSizeSm*1.25)

        wghtVal = interpolate(300,1000, f)
        caslVal = interpolate(0, 1, f)
        casualValue = "{:0.2f}".format(caslVal)
        text(f"CASL = {casualValue}\nwght = {str(int(wghtVal)).rjust(4,'0')}", (W*.75, H*.76), align="center")

        wghtVal = interpolate(1000,300, f)
        caslVal = interpolate(0, 1, f)
        casualValue = "{:0.2f}".format(caslVal)
        text(f"CASL = {casualValue}\nwght = {str(int(wghtVal)).rjust(4,'0')}", (W*.25, H*.275), align="center")

def drawHearts(f, r=1,g=1,b=1, info=False):
    fontSizeLg = H*.825
    offset = H*0.0375
    fill(r,g,b)
    blendMode("screen")
    font(fontFam, fontSizeLg)
    wghtVal = interpolate(1000,300, f)
    caslVal = interpolate(0, 1, f)
    fontVariations(wght=wghtVal,CASL=caslVal)
    fontSize = fontSizeLg
    text("♥♡", (W/2, 0-offset),align="center")

    wghtVal = interpolate(300, 1000, f)
    caslVal = interpolate(0, 1, f)
    fontVariations(wght=wghtVal,CASL=caslVal)
    fontSize = fontSizeLg
    text("♡♥", (W/2, H/2-offset*1.5), align="center")


# ----------------------------------------------
# ANIMATION

for repeat in range(5):
    for frame in range(frames):
        newPage(W, H) # required for each new page/frame
        fill(0)
        rect(0,0,W, H)

        f = frame / frames
        t = frame / frames
        if t <= 0.5:
            f *= 2
        else:
            f = 1 - (f - 0.5) * 2

        t = frame / frames

        if debug:
            fill(1,0,0)
            rect(0, H/2, W, 1)
            rect(W/2, 0, 1, H)

        
        rgbOffset = 0.0075
        
        drawHearts(f, 0,1,0)
        translate(0,H*rgbOffset)
        drawHearts(f, 1,0,0)
        translate(0,-H*rgbOffset*2)
        drawHearts(f, 0,0,1, info=True)

        writeInfoTop(f, 0,0,0)

endDrawing() # advised by drawbot docs

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