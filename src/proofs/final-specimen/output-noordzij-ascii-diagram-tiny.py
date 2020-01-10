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
import re

newDrawing() # required by drawbot module

# currentDir = sys.argv[0]
currentDir = os.path.dirname(os.path.abspath(__file__))
print(currentDir)

# diagram = """\
# ·····················
# ·········• – – – •···
# ·······/···5···/ |···
# ··↑··• – – – • 2 •···
# ··z··|···1···| /··↗··
# ·····• – – – •··y····
# ········x →··········
# ·····················\
# """

# """
diagram = """\
·························
·········• – – – – – •···
·······/·····5·····/ |···
·····• – – – – – •···|···
··↑··|···········| 2 |···
··z··|·····1·····|···•···
·····|···········| /··↗··
·····• – – – – – •··y····
··········x →············
·························\
"""
# ---------------------------------------------------------
# CONFIGURATION -------------------------------------------

docTitle = "drawbot-export" # update this for your output file name
save = True
outputDir = "exports"
autoOpen = True

fontFam = f"{currentDir}/Recursive_VF_1.031.ttf" # Update as needed. Easiest when font file is in same directory.

frames = 1
# fps = 3
# frameRate = 1/fps # only applicable to mp4 and gif; can be buggy
fileFormat = "png" # pdf, gif, or mp4

pageSize = 3.6 # inches
DPI = 300 # dots per inch

paddingInPts = 8

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
	""" 
		Use with a '*' like: 
		fill(*hex2rgb("F5E4CB"))
	"""
	h = hex.lstrip('#')
	RGB = tuple(int(h[i:i+2], 16) for i in (0, 2 ,4))
	r1, g1, b1 = RGB[0] / 255, RGB[1] / 255, RGB[2] / 255
	return(r1, g1, b1)

# ----------------------------------------------
# THE ACTUAL ANIMATION

for frame in range(frames):
	newPage(W, H) # required for each new page/frame

	# background
	fill(*hex2rgb("001728"))
	rect(0,0,W,H)

	t = frame / frames
	# x = interpolate(0, W*0.9, t)

	txt = FormattedString()

	for char in diagram:
		txt.fontVariations(MONO=0.999, CASL=0.999)

		# background dots, etc
		if char in "· ¦".split():
			txt.fill(1,1,1,0.075)
			# txt.fontVariations(MONO=0.999, CASL=0)

		# punctutation
		elif char in "| – • . /".split():
			txt.fill(*hex2rgb("D18DF0")) #purple
			# txt.fontVariations(MONO=0.999, CASL=0)

		# numbers
		elif char in "0 1 2 3 4 5 6 7 8 9".split():
			txt.fill(*hex2rgb("FF8563")) # orange

		# text
		else:
			txt.fill(*hex2rgb("F4C384")) # orange sorbet

		# textSize=W*0.07
		textSize=W*0.06

		txt.lineHeight(textSize*1.65)
		txt.append(char, font=fontFam, fontSize=textSize)
		# # adding more text
		# txt.append("world", font="Times-Italic", fontSize=50, fill=(0, 1, 0))

	# drawing the formatted string
	text(txt, (W/2, H-(W*0.0725)), align="center")
	
	font(fontFam, computeFontSizePoints(8)) # set a font and font size
	# draw text

	


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