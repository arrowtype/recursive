from drawBot import * # requires drawbot to be installed as module
import datetime
from fontTools.misc.bezierTools import splitCubicAtT
import content
from content.specimenContent import *
newDrawing() # for drawbot module

refresh = True
if refresh == True:
    import importlib
    importlib.reload(content.specimenContent)
    from content.specimenContent import *

# ---------------------------------------------------------
# CONFIGURATION -------------------------------------------

docTitle = "recursive-text-style-gradient--line_breaks"

save = True
autoOpen = True
book = True
debug = False # overlays curve visualizations
    
frames = 6 # 192
frameRate = 1/60 # only applicable to mp4
fileFormat = "pdf" # pdf, gif, or mp4

bookSizeW = 5.9 # inches
bookSizeH = 8.5 # inches
DPI = 72 # dots per inch
pixelsW = DPI*bookSizeW *2
pixelsH = DPI*bookSizeH

W, H = pixelsW, pixelsH # do not edit this

background = 1

# def computeFontSizePoints(pts):
#     return W * (pts / (bookSizeW * 72))
# textSize = computeFontSizePoints(7)
textSize = 11

fontFam = "/Users/stephennixon/type-repos/recursive/src/proofs/drawbot-specimens-and-diagrams/running-test-style-gradient/fonts/recursive-MONO_CASL_wght_slnt_ital--full_gsub--2019_11_22-20_38.ttf"

# rwSize =  computeFontSizePoints(152)

padding = DPI*0.5


# # this will draw cyan guides to help align content
# def drawMargins():
#     # top, right, bottom, left
#     margins = (0.75, 0.25, 0.25, 0.25)
#     thickness = 1
#     fill(0,1,1)

#     # x, y, w, h
#     rect(0, H - margins[0]*DPI, W, thickness)  # top
#     rect(margins[1]*DPI, 0, thickness, H)      # right
#     rect(W - margins[2]*DPI, 0, thickness, H)  # bottom
#     rect(0, margins[3]*DPI, W, thickness)      # left
    
#     fill(0,1,1,0.5)
#     rect(0, H*0.5, W, thickness)      # middle
#     rect(W*0.5, 0, thickness, H)      # center


def interpolate(a, b, t):
    distance = b-a
    return(a + distance * t)

# You can even make this getCurve() function do a lot more for you, I'll sketch pseudo code here:


newPage(W, H)
fill(background)
rect(0,0,W, H)

font(fontFam)
fontSize(textSize)

fill(0)

txt = FormattedString()

# specimenText = specimenText.replace("\n\n", " ¶ ").replace("§","\n\n") # pilcrows for paragraph breaks
specimenText = specimenText.replace("\n\n", "\n    ").replace("§","\n") # tabs for paragraph breaks

specimenWords = specimenText.split(" ")

wordCount = len(specimenWords)

minMONO, maxMono = 0.001, 0.999
minCASL, maxCASL = 0.001, 0.999

for num, word in enumerate(specimenWords):
    txt.font(fontFam)
    leading = textSize*1.5
    txt.lineHeight(leading)

    currentMONO = interpolate(maxMono, minMONO, num/wordCount)
    currentCASL = interpolate(maxCASL, minCASL, num/wordCount)
    txt.fontVariations(MONO=currentMONO, CASL=currentCASL, wght=400)

    if word == "§":
        txt.fontVariations(MONO=currentMONO, CASL=currentCASL, wght=700)
        # output next words until you hit "\n"

    if word == "¶":
        txt.fill(0,0,1,1)
        # txt.fontVariations(MONO=currentMONO, CASL=currentCASL, wght=350)
    elif num < 9:
        txt.fill(0,0,1,1)
        txt.fontVariations(MONO=currentMONO, CASL=currentCASL, wght=700)
    else:
        txt.fill(0)
    txt.append(word + " ")



overflow = textBox(txt, (padding,padding,W/2-(padding*2),H-(padding*2)))

textBox(overflow, (W/2+padding,padding,W/2-(padding*2),H-(padding*2)))


    
    
    
# # ----------------------------------------------------------------------
# # DEBUGGING VISUALS ----------------------------------------------------
# if debug:
    
#     print("-------------------------------------")
#     print("#: " + str(frame))
#     print("x: " + str(round(abs(xprnVals[0]), 0)))
#     print("w: " + str(round(abs(wghtVals[0]), 0)))
#     print("s: " + str(round(abs(slntVals), 2)))
#     print('')

#     drawMargins()
    


endDrawing()

if save:
    now = datetime.datetime.now().strftime("%Y_%m_%d-%H_%M") # -%H_%M_%S

    path = f"/Users/stephennixon/type-repos/recursive/src/proofs/drawbot-specimens-and-diagrams/running-test-style-gradient/exports/{docTitle}-{now}.{fileFormat}"

    print("saved to ", path)

    saveImage(path)

    if autoOpen:
        import os
        os.system(f"open --background -a Preview {path}")


