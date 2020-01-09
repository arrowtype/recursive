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

docTitle = "drawbot-export" # update this for your output file name
save = True
outputDir = "exports"
autoOpen = True
debug = False

fontFam = f"{currentDir}/Recursive_VF_1.031.ttf" # Update as needed. Easiest when font file is in same directory.

frames = 1
fileFormat = "pdf" # pdf # if just 1 frame, can also be jpg or png (otherwise, only the final frame is saved)

pageSize = 3.5 # inches
DPI = 72 # dots per inch

paddingInPts = 8

# ----------------------------------------------
# Helper functions

pixels = DPI*pageSize # do not edit
W, H = pixels, pixels # do not edit

def getPadding(pts):
	return DPI*paddingInPts/72 # do not edit

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

def makeDrawing(xVar="wght", yVar="slnt", Xasc=True, Yasc=True, letter="a", rows=6, cols=6, MONOVal=0, CASLVal=0, wghtVal=300, slntVal=0, italVal=0.5, fileTag=""):

	"""
		Set x and y to the variation axes you wish to control. 

		Add arguments to control diagram. Defaults are:

		argument    | abbr | value | description
		----------- | ---- | ----- | ----------------------------------------------
		--letter    | -l   | a     | letter to draw
		--rows      | -r   | 6     | Number of rows in cube
		--cols      | -c   | 6     | Number of cols in cube
		--xVar      | -x   | wght  | X axis variation
		--yVar      | -y   | slnt  | Y axis variation
		--Xasc     | -a   | True  | Ascend on X axis
		--Yasc     | -b   | True  | Ascend on Y axis
		--MONOVal   | -M   | 0     | Default for MONO (Range: 0 to 1)
		--CASLVal   | -C   | 0     | Default for CASL (Range: 0 to 1)
		--wghtVal   | -w   | 300   | Default for wght (Range: 300 to 1000)
		--slntVal   | -s   | 0     | Default for slnt (Range: 0 to -15)
		--italVal   | -i   | 0.5   | Default for ital (Range: 0 to 1, 0.5 for auto)
		--fileTag   | -f   | ""    | File tag, e.g. "01_front" or "05_top" etc (default is empty)

		USAGE EXAMPLE:

		python <path>/create-flattened-noordzij-cube.py -s 5 -c r -x CASL -y wght -a False -b False

		(args left out will use defaults)

		# TODO (maybe): add control over
			- letter sizing
			- colors
			- frames?
			- filetype?
	"""

	newDrawing() # required by drawbot module

	# ----------------------------------------------
	# THE ACTUAL ANIMATION

	padding = getPadding(0)

	for frame in range(0, frames):
		newPage(W, H) # required for each new page/frame
		# fill(*hex2rgb("0021ff"))
		fill(0)
		rect(0,0,W,H) # background

		cubeSize = W - (padding * 2)
		
		

		for xStep in range(0, cols):
			letterAdvanceX = cubeSize / cols
			x = xStep * letterAdvanceX + padding
			t = xStep / (cols - 1)
			if Xasc:
				xAxisVal = round(interpolate(axes[xVar][0], axes[xVar][1], t), 2)
			else:
				xAxisVal = round(interpolate(axes[xVar][1], axes[xVar][0], t), 2)

			for yStep in range(0, rows):
				letterAdvanceY = cubeSize / rows
				t = yStep / (rows - 1)

				if Yasc:
					yAxisVal = round(interpolate(axes[yVar][0], axes[yVar][1], t), 2)
				else:
					yAxisVal = round(interpolate(axes[yVar][1], axes[yVar][0], t), 2)


				print(xVar, xAxisVal, yVar, yAxisVal)

				# allow default vars to be set
				dfltKwargs = {"MONO": MONOVal, "CASL": CASLVal, "wght": wghtVal, "slnt": slntVal, "ital": italVal}
				fontVariations(**dfltKwargs)

				# set x & y axis styles
				kwargs = {xVar: xAxisVal, yVar: yAxisVal}
				fontVariations(**kwargs)
				
				if debug:
					fill(0.9)
					stroke(1, 0, 0)
					strokeWidth(0.25)
					rect(x, y, letterAdvanceX, letterAdvanceY)

				# textSize = letterAdvance*1.5
				textSize = letterAdvanceY
				font(fontFam, textSize) # set a font and font size

				y = yStep * letterAdvanceY + padding + (textSize*0.2)

				print(letterAdvanceX,letterAdvanceY,textSize)


				letterObject = FormattedString()
				letterObject.font(fontFam)
				letterObject.fontVariations(**dfltKwargs)
				letterObject.fontVariations(**kwargs)
				letterObject.fontSize(textSize)
				letterObject.append(letter)


				# strokeWidth(0)
				fill(1)

				textPath = BezierPath()
				textPath.text(letterObject, (x + letterAdvanceX/2, y ), align="center")
				textPath.removeOverlap()
				drawPath(textPath)

	endDrawing() # advised by drawbot docs

	if save:
		import datetime

		now = datetime.datetime.now().strftime("%Y_%m_%d-%H_%M_%S") # -%H_%M_%S

		if not os.path.exists(f"{currentDir}/{outputDir}"):
			os.makedirs(f"{currentDir}/{outputDir}")

		path = f"{currentDir}/{outputDir}/{docTitle}-{now}.{fileFormat}"

		if fileTag != "":
			path = f"{currentDir}/{outputDir}/{fileTag}--{docTitle}-{now}.{fileFormat}"

		print("saved to ", path)

		saveImage(path)

		if autoOpen:
			os.system(f"open --background -a Preview {path}")

if __name__ == '__main__':
	fire.Fire(makeDrawing)