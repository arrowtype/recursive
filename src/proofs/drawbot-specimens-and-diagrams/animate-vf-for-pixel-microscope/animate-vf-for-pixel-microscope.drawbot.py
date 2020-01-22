"""
  animate variable axes in small text, specifically to record with usb microscope
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

fontFam = f"{currentDir}/Recursive_VF_1.031.ttf" # Update as needed. Easiest when font file is in same directory.

frames = 100
fps = 3
frameRate = 1/fps # only applicable to mp4 and gif; can be buggy
fileFormat = "gif" # pdf, gif, or mp4

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

def hex2rgb(hex):
    h = hex.lstrip('#')
    RGB = tuple(int(h[i:i+2], 16) for i in (0, 2 ,4))
    r1, g1, b1 = RGB[0] / 255, RGB[1] / 255, RGB[2] / 255
    return(r1, g1, b1)

# ----------------------------------------------
# THE ACTUAL ANIMATION

for frame in range(frames):
	newPage(W, H) # required for each new page/frame

	# t = 1 - 1/frames * frame
	f = frame / frames
	t = frame / frames
	if t <= 0.5:
		f *= 2
	else:
		f = 1 - (f - 0.5) * 2
	# wghtVal = interpolate(300, 1000, f)
	slntVal = interpolate(0, -15, f)

	# fill(0.7)
	fill(*hex2rgb("001022"))
	rect(0,0,W,H)
	
	with savedState():
		# rotate(180, center=(W/2,H/2))
		transform((1, 0, 0, -1, 0, 0),center=(W/2,H/2))
		# fill(0.7)
		# fill(0)
		fill(1)
		fontVariations(wght=400, MONO=0.999, slnt=slntVal)
		font(fontFam, computeFontSizePoints(16)) # set a font and font size
		# draw text
		text("ri", (W/2, H/2))

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