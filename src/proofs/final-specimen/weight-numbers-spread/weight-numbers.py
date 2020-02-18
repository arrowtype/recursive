# 1000.00 999.00 998.00 997.00 996.00 995.00 994.00 993.00 992.00 991.00 
#  992.00 991.00 990.00 989.00 988.00 987.00 986.00 985.00 984.00 983.00 
#  982.00 981.00 980.00 979.00 978.00 977.00 976.00 975.00 974.00 973.00 
#  972.00 971.00 970.00 969.00 968.00 967.00 966.00 965.00 964.00 963.00

# 999.99  999.00 998.00 997.00 996.00 995.00 994.00 993.00 992.00 991.00 
# 992.00 991.00 990.00 989.00 988.00 987.00 986.00 985.00 984.00 983.00 
# 982.00 981.00 980.00 979.00 978.00 977.00 976.00 975.00 974.00 973.00 
# 972.00 971.00 970.00 969.00 968.00 967.00 966.00 965.00 964.00 963.00

# ten columns across (actually 70 characters across)
# 35 rows
# max 1000, min 1

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

fileFormat = "pdf" # pdf, gif, or mp4

pageW = 5.216 # inches
pageH = 7.216 # inches
padding = 0.1667  # inches
DPI = 300 # dots per inch


# ----------------------------------------------
# Helper functions

W = DPI*pageW # do not edit
H = DPI*pageH # do not edit
padding = DPI*padding # do not edit

# turn font size into usable value for given pageSize
# def computeFontSizePoints(pts):
# 	return W * (pts / (pageSize * 72))

# a frequently-useful function
def interpolate(a, b, t):
	return(a + (b-a) * t)

# ----------------------------------------------
# Pages

newPage(W, H) # required for each new page/frame
fill(0,0,1)
rect(0,0,W, H)







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