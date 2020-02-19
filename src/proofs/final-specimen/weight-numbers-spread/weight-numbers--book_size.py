# 1000.00 999.00 998.00 997.00 996.00 995.00 994.00 993.00 992.00 991.00 
#  992.00 991.00 990.00 989.00 988.00 987.00 986.00 985.00 984.00 983.00 
#  982.00 981.00 980.00 979.00 978.00 977.00 976.00 975.00 974.00 973.00 
#  972.00 971.00 970.00 969.00 968.00 967.00 966.00 965.00 964.00 963.00

# 999.99  999.00  998.00  997.00  996.00  995.00  994.00  993.00  992.00  991.00
# 992.00  991.00  990.00  989.00  988.00  987.00  986.00  985.00  984.00  983.00
# 982.00  981.00  980.00  979.00  978.00  977.00  976.00  975.00  974.00  973.00
# 972.00  971.00  970.00  969.00  968.00  967.00  966.00  965.00  964.00  963.00

# ten columns across (actually 70 characters across)
# 35 rows
# max 1000, min 300

"""
  This is a set of Python I use many times I wish to make an animation or multipage doc with Drawbot, 
  but code in my preferred editor (currently, VS Code) rather than in the Drawbot app.

  USAGE:

  First, install DrawBot as a module:
  pip install git+https://github.com/typemytype/drawbot
  
  Adapt script as needed, then run from the command line with:
  
  python3 <path>/weight-numbers.py.py
"""

from drawBot import * # requires drawbot to be installed as module
import sys
import os

newDrawing() # required by drawbot module

currentDir = os.path.dirname(os.path.abspath(__file__))
print(currentDir)          

# ---------------------------------------------------------
# CONFIGURATION -------------------------------------------

docTitle = "drawbot-export" # update this for your output file name
save = True
outputDir = "exports"
autoOpen = True
debug = False # useful to tie guides / helper visuals to this

fontFam = f"{currentDir}/Recursive_VF_1.039.ttf" # Update as needed. Easiest when font file is in same directory.

fileFormat = "png" # pdf, gif, or mp4

pageW = 5.2126 # inches
pageH = 7.7126 # inches
padding = 0.04  # inches
DPI = 300 # dots per inch

# ----------------------------------------------
# Helper functions

W = DPI*pageW # do not edit
H = DPI*pageH # do not edit
padding = DPI*padding # do not edit


# turn font size into usable value for given pageSize
def computeFontSizePoints(pts):
	return pts * DPI / 72

# a frequently-useful function
def interpolate(a, b, t):
	return(a + (b-a) * t)

# ----------------------------------------------
# Pages


font(fontFam)
minWght = listFontVariations()["wght"]["minValue"]
maxWght = listFontVariations()["wght"]["maxValue"]

# make maxWght just 6 digits in length for graphic
if maxWght == 1000.0:
	maxWght = 999.99

cols = 10
rows = 35

wghtRange = maxWght - minWght
numSteps = (cols * rows) * 2
stepSize = wghtRange / (numSteps - 1)

# calculates steps, formats with 2 decimal places, and puts in list, then joins that into a string separated by "  "
# stepsList = ["{:0.2f}".format(minWght+stepSize*step) for step in range(numSteps)]
stepsList = [f"{(minWght+stepSize*step):0.2f}" for step in range(numSteps)]
stepsStr = "  ".join(stepsList)

print(stepsStr)

txt = FormattedString()
txt.fontSize(computeFontSizePoints(8))
txt.lineHeight(computeFontSizePoints(16))
txt.fill(1)
txt.font(fontFam)
txt.align("center")

for page in range(2):

	newPage(W, H) # required for each new page/frame
	# fill(0,0,0)
	# rect(0,0,W, H)

	# make font 8pt/16pt
	

	for i, step in enumerate(stepsList):
		txt.fontVariations(MONO=1,wght=float(step))
		# don't add a space to final column
		txt.tracking(None)
		if (i+1) % cols == 0:
			if debug:
				txt.fill(1,0,0)
			txt.append(f"{step}\n")
		else:
			txt.fill(1)
			txt.append(f"{step}")
			txt.tracking(-computeFontSizePoints(8)*0.045)
			txt.append("  ")
			
	box = (padding, -padding*0.125, W-padding*2, H+padding*2)
	txt = textBox(txt, box)

	if debug:
		stroke(1,0,0)
		fill(1,1,1,0)
		rect(box)

	if save:
		import datetime

		now = datetime.datetime.now().strftime("%Y_%m_%d-%H_%M_%S") # -%H_%M_%S

		if not os.path.exists(f"{currentDir}/{outputDir}"):
			os.makedirs(f"{currentDir}/{outputDir}")

		path = f"{currentDir}/{outputDir}/{docTitle}-{now}.{fileFormat}"

		print("saved to ", path)

		saveImage(path)

		if autoOpen:
			os.system(f"open --background -a Preview {path}")

print()



endDrawing() # advised by drawbot docs

