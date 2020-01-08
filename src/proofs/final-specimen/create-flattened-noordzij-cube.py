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
	'MONO': (0, 1),
	'CASL': (0, 1),
	'wght': (300, 1000),
	'slnt': (0, -15)
	# 'ital': (0, 1), # intentionally left out
}

def makeDrawing(xVar="wght", yVar="slnt", xAsc=True, yAsc=True, char="a", splits=6):

	"""
		Set x and y to the variation axes you wish to control. 

		Add arguments to control diagram. Defaults are xVar="wght", yVar="slnt", xAsc=True, yAsc=True, splits=6 and char="a"

		python <path>/create-flattened-noordzij-cube.py -x CASL -y wght -c r
		
		TODO: support xAsc and yAsc (make axes descend if False)
	"""

	newDrawing() # required by drawbot module

	# ----------------------------------------------
	# THE ACTUAL ANIMATION

	for frame in range(frames):
		newPage(W, H) # required for each new page/frame


		cubeSize = W - (padding * 2)
		letterAdvance = cubeSize / splits
		textSize = letterAdvance*1.5
		font(fontFam, textSize) # set a font and font size

		print(letterAdvance,textSize)

		# needs instructions on *which* var axis to put on which square axis, e.g.
		# x=wght, y=slnt

		for xStep in range(0, splits):
			x = xStep * letterAdvance + padding
			t = xStep / splits
			xAxisVal = round(interpolate(axes[xVar][0], axes[xVar][1], t), 2)
			for yStep in range(0, splits):
				t = yStep / splits
				yAxisVal = round(interpolate(axes[yVar][0], axes[yVar][1], t), 2)
				y = yStep * letterAdvance + padding




				# MONO = round(interpolate(axes['MONO'][0], axes['MONO'][1], t), 2)
				# CASL = round(interpolate(axes['CASL'][0], axes['CASL'][1], t), 2)
				# wght = round(interpolate(axes['wght'][0], axes['wght'][1], t), 2)
				# slnt = round(interpolate(axes['slnt'][0], axes['slnt'][1], t), 2)
				# ital = 0.5 # auto
				print(xVar, xAxisVal, yVar, yAxisVal)

				kwargs = {xVar: xAxisVal, yVar: yAxisVal}
				fontVariations(**kwargs)
				
				if debug:
					fill(0.9)
					stroke(1, 0, 0)
					strokeWidth(0.25)
					rect(x, y, letterAdvance, letterAdvance)

				strokeWidth(0)
				fill(0)
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