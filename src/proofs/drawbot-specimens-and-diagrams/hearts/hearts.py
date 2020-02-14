"""
  This is a set of Python I use many times I wish to make an animation or multipage doc with Drawbot, 
  but code in my preferred editor (currently, VS Code) rather than in the Drawbot app.
  USAGE:
  First, install DrawBot as a module:
  pip install git+https://github.com/typemytype/drawbot
  
  Adapt script as needed, then run from the command line with:
  
  python3 <path>/remote-drawbot-script-template.py
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

fontFam = f"{currentDir}/Recursive_VF_1.038.fix.ttf" # Update as needed. Easiest when font file is in same directory.

frames = 2
fps = 3
frameRate = 1/fps # only applicable to mp4 and gif; can be buggy
fileFormat = "pdf" # pdf, gif, or mp4

pageSize = 3.5 # inches
DPI = 72 # dots per inch

paddingInPts = 18

# ----------------------------------------------
# Helper functions

pixels = DPI*pageSize # do not edit
W, H = pixels, pixels # do not edit
padding = DPI*paddingInPts/72 # do not edit

# turn font size into usable value for given pageSize
def computeFontSizePoints(pts):
	return W * (pts / (pageSize * 72))

# a frequently-useful function
def interpolate(a, b, t):
	return(a + (b-a) * t)

# ----------------------------------------------
# THE ACTUAL ANIMATION

def drawHearts(r=1,g=1,b=1):
	fontSize = H*.825
	offset = H*0.0375
	fill(r,g,b)
	font(fontFam, fontSize)
	text("♥♡", (W/2, 0-offset),align="center")
	font(fontFam, fontSize)
	text("♡♥", (W/2, H/2-offset*1.5), align="center")


for frame in range(frames):
	newPage(W, H) # required for each new page/frame
	fill(0)
	rect(0,0,W, H)

	t = frame / frames

	if debug:
		fill(1,0,0)
		rect(0, H/2, W, 1)
		rect(W/2, 0, 1, H)

	blendMode("screen")
	drawHearts(0,1,0)
	translate(0,H*0.01)
	drawHearts(1,0,0)
	translate(0,-H*0.02)
	drawHearts(0,0,1)

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