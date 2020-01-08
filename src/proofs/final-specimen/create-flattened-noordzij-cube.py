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
import fire



# currentDir = sys.argv[0]
currentDir = os.path.dirname(os.path.abspath(__file__))
print(currentDir)

# ---------------------------------------------------------
# CONFIGURATION -------------------------------------------

cubeChar = "a"

docTitle = "drawbot-export" # update this for your output file name
save = True
outputDir = "exports"
autoOpen = True
debug = False

fontFam = f"{currentDir}/Recursive_VF_1.031.ttf" # Update as needed. Easiest when font file is in same directory.

frames = 1
frameRate = 1/60 # only applicable to mp4
fileFormat = "pdf" # pdf, gif, or mp4 # if just 1 frame, can also be jpg or png

pageSize = 3.5 # inches
DPI = 300 # dots per inch

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

def hex2rgb(hex):
    h = hex.lstrip('#')
    RGB = tuple(int(h[i:i+2], 16) for i in (0, 2 ,4))
    r1, g1, b1 = RGB[0] / 255, RGB[1] / 255, RGB[2] / 255
    return(r1, g1, b1)

# Data for font axes

axes = {
	'MONO': (0, 1),
	'CASL': (0, 1),
	'wght': (300, 1000),
	'slnt': (0, -15)
	# 'ital': (0, 1), # intentionally left out
}

def makeDrawing(xVar="wght", yVar="slnt", aXasc=True, bYasc=True, char="a", splits=6):

	"""
		Set x and y to the variation axes you wish to control. 

		Add arguments to control diagram. Defaults are:

			splits=6	| -s | Number of splits in cube
			char="a"	| -c | character to draw
			xVar="wght"	| -x | X axis variation
			yVar="slnt"	| -y | Y axis variation
			aXasc=True	| -a | Ascend on X axis
			bYasc=True	| -b | Ascend on Y axis

		USAGE EXAMPLE:

		python <path>/create-flattened-noordzij-cube.py -s 5 -c r -x CASL -y wght -a False -b False

		(args left out will use defaults)
	"""

	newDrawing() # required by drawbot module

	# ----------------------------------------------
	# THE ACTUAL ANIMATION

	for frame in range(frames):
		newPage(W, H) # required for each new page/frame
		fill(*hex2rgb("0021ff"))
		rect(0,0,W,H) # background

		cubeSize = W - (padding * 2)
		letterAdvance = cubeSize / splits
		textSize = letterAdvance*1.5
		font(fontFam, textSize) # set a font and font size

		print(letterAdvance,textSize)

		# needs instructions on *which* var axis to put on which square axis, e.g.
		# x=wght, y=slnt

		for xStep in range(0, splits):
			x = xStep * letterAdvance + padding
			t = xStep / (splits - 1)
			if aXasc:
				xAxisVal = round(interpolate(axes[xVar][0], axes[xVar][1], t), 2)
			else:
				xAxisVal = round(interpolate(axes[xVar][1], axes[xVar][0], t), 2)

			for yStep in range(0, splits):
				t = yStep / (splits - 1)

				if bYasc:
					yAxisVal = round(interpolate(axes[yVar][0], axes[yVar][1], t), 2)
				else:
					yAxisVal = round(interpolate(axes[yVar][1], axes[yVar][0], t), 2)

				y = yStep * letterAdvance + padding

				print(xVar, xAxisVal, yVar, yAxisVal)

				# allow default vars to be set, as well?
				kwargs = {xVar: xAxisVal, yVar: yAxisVal}
				fontVariations(**kwargs)
				
				if debug:
					fill(0.9)
					stroke(1, 0, 0)
					strokeWidth(0.25)
					rect(x, y, letterAdvance, letterAdvance)

				strokeWidth(0)
				fill(1)
				text(char, (x + letterAdvance/2, y), align="center")

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

if __name__ == '__main__':
	fire.Fire(makeDrawing)