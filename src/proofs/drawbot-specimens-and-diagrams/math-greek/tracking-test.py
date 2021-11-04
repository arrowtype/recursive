# set up to use drawbot as a module in an external code editor
from drawBot import *
newDrawing() # required by drawbot module

#--------------------------------------------------
# tracking test

newPage(200, 100)
fs = FormattedString(
    'TESTING',
    fontSize=24,
    tracking=5)
    
textBox(fs, (10, 10, 200, 50))

#--------------------------------------------------
# saving the file

import os

currentDir = os.path.dirname(os.path.abspath(__file__))

saveImage(f"{currentDir}/tracking-test.png")