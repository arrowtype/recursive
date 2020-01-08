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

cubeSplits = 9 # number of glyphs on each edge
cubeChar = "a"

docTitle = "drawbot-export" # update this for your output file name
save = True
outputDir = "exports"
autoOpen = True
debug = False

fontFam = f"{currentDir}/Recursive_VF_1.031.ttf" # Update as needed. Easiest when font file is in same directory.

frames = 1
frameRate = 1/60 # only applicable to mp4
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

axes = {
	'mono': (0, 1),
	'casl': (0, 1),
	'wght': (300, 1000),
	'slnt': (0, -15)
	# 'ital': (0, 1), # intentionally left out
}

# ----------------------------------------------
# THE ACTUAL ANIMATION

for frame in range(frames):
	newPage(W, H) # required for each new page/frame


	cubeSize = W - (padding * 2)
	letterAdvance = cubeSize / cubeSplits
	textSize = letterAdvance*1.5
	font(fontFam, textSize) # set a font and font size

	print(letterAdvance,textSize)

	for xStep in range(0, cubeSplits):
		x = xStep * letterAdvance + padding
		for yStep in range(0, cubeSplits):
			y = yStep * letterAdvance + padding

			t = xStep / cubeSplits

			mono = round(interpolate(axes['mono'][0], axes['mono'][1], t), 2)
			casl = round(interpolate(axes['casl'][0], axes['casl'][1], t), 2)
			wght = round(interpolate(axes['wght'][0], axes['wght'][1], t), 2)
			slnt = round(interpolate(axes['slnt'][0], axes['slnt'][1], t), 2)
			ital = 0.5 # auto

			fontVariations(MONO=mono, CASL=casl, wght=wght, slnt=slnt)
			
			if debug:
				fill(0.9)
				stroke(1, 0, 0)
				strokeWidth(0.25)
				rect(x, y, letterAdvance, letterAdvance)

			strokeWidth(0)
			fill(0)
			text(cubeChar, (x + letterAdvance/2, y), align="center")

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
