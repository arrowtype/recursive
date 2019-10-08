"""
    A DrawBot script to make flipbook pages for an animated specimen.
    Somewhat similar to Recursive animation at https://codepen.io/thundernixon/pen/wVypxe?editors=1100

    NOTE: is currently set up to be run from a file, with DrawBot installed as a module.

    To do: 
    - Eliminate reliance on 100 frames (link curve dict to t, not to frame)
    - Make axis values travel along curve with smoother acceleration.
    - Allow arbitrary dictionary of timing percentages & axis values, similar to CSS keyframes.
"""

from drawBot import * # requires drawbot to be installed as module
import datetime
from fontTools.misc.bezierTools import splitCubicAtT
newDrawing() # for drawbot module

# ---------------------------------------------------------
# CONFIGURATION -------------------------------------------

debug = True # overlays curve visualizations

prop = 1

if prop is 1:
    fontFam = "/Users/stephennixon/type-repos/recursive/src/proofs/drawbot-diagrams-etc/flipbook/fonts/Recursive-sans--w_ital_slnt-2019_08_12.ttf"
else:
    fontFam = "/Users/stephennixon/type-repos/recursive/src/proofs/drawbot-diagrams-etc/flipbook/fonts/Recursive-mono-full--w_ital_slnt-2019_07_25.ttf"

frames = 100 # currently must be in units of 100
format = "gif" # pdf, gif, or mp4

bookSize = 3.5 # inches
DPI = 144 # dots per inch
pixels = DPI*bookSize

W, H = pixels, pixels # do not edit this

textSize = W/30
rwSize = W/1.4
