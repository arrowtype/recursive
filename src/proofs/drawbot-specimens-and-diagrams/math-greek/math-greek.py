"""
  This is a set of Python I use many times I wish to make an animation or multipage doc with Drawbot, 
  but code in my preferred editor (currently, VS Code) rather than in the Drawbot app.
  USAGE:
  First, install DrawBot as a module:
  pip install git+https://github.com/typemytype/drawbot
  
  Adapt script as needed, then run from the command line with:
  
  python3 <path>/math-greek.py
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

fontFam = f"{currentDir}/Recursive_VF_1.084.ttf" # Update as needed. Easiest when font file is in same directory.

loops = 3 #3 # number of times to repeat animation
frames = 32 # 32 # frames per loop
fps = 3
frameRate = 1/fps # only applicable to mp4 and gif; can be buggy
fileFormat = "mp4" # pdf, gif, or mp4

pageSize = 3.5 # inches
DPI = 450 # dots per inch

paddingInPts = 18

# inputText = """\
# Α Β Γ Δ Λ
# Μ Ν Θ Π Φ
# α β γ μ λ
# ν θ π δ φ
# """
inputText = """\
ΑΒΓΔΛ
ΜΝΘΠΦ
αβγμλ
νθπδφ
"""

# ----------------------------------------------
# Helper functions

pixels = DPI*pageSize # do not edit
# W, H = pixels, pixels # do not edit
W, H = 1080,1350 # IG portrait
padding = DPI*paddingInPts/72 # do not edit

# turn font size into usable value for given pageSize
def computeFontSizePoints(pts):
    return W * (pts / (pageSize * 72))

# a frequently-useful function
def interpolate(a, b, t):
    return(a + (b-a) * t)

# ----------------------------------------------
# TEXT FUNCTIONS

def drawCharacters(f, r=1,g=1,b=1, t=1, loop=1):
    # fontSizeLg = H*.13
    fontSizeLg = H*.2 
    offset = H*0.2
    
    blendMode("screen")
    font(fontFam, fontSizeLg)
    wghtVal = interpolate(300, 1000, f)
    caslVal = interpolate(0, 1, f)
    slntVal = interpolate(0, -14, f)
    monoVal = interpolate(1, 0, f)
    fontVariations(wght=wghtVal,CASL=caslVal,slnt=slntVal, MONO=monoVal)

    with savedState():
        for color in [(1,0,0),(0,1,0),(0,0,1)]:

            fill(*color)

            rgbOffset = 0.0025 * f * loop
            translate(0,H*rgbOffset)

            # tracking(20)

            for i, line in enumerate(inputText.split("\n")):
                path = BezierPath()

                txt = FormattedString(
                    line,
                    font=fontFam,
                    fontSize=fontSizeLg,
                    fill=color,
                    tracking=10,
                    align="center",
                    fontVariations={"wght": wghtVal,"CASL": caslVal,"slnt": slntVal, "MONO": monoVal}
                )

                path.text(txt,(W/2, H*0.95-offset*(i+1-.25)))

                drawPath(path)

    # variation label
    with savedState():
        fontSizeSm = H*.02
        blendMode("normal")
        fill(0.875)
        lineHeight(fontSizeSm)
        monoValue = "{:0.2f}".format(monoVal)
        casualValue = "{:0.2f}".format(caslVal)
        weightValue = str(int(wghtVal)).rjust(4,'0')
        slantValue = "-{:05.2f}".format(abs(slntVal))
        font(fontFam, fontSizeSm)
        fontVariations(wght=400,CASL=0.5,slnt=0, MONO=1)
        # rotate(90)
        # text(f"MONO {monoValue}    CASL {casualValue}    WGHT {weightValue}    SLNT {slantValue}", (W*.05, H*-.05), align="left")
        text(f"MONO {monoValue}    CASL {casualValue}    WGHT {weightValue}    SLNT {slantValue}", (W*.5, H*.062), align="center")


# ----------------------------------------------
# ANIMATION

for repeat in range(loops):
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

        drawCharacters(f, 0,1,0, t, repeat+1)

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