'''
    Glyph Bezier Tweener - Work in Progress

    Will animate between glyph beziers to show variable interpolation.
    
    This must be used within the Drawbot extension for RoboFont.
'''

from datetime import datetime
from vanilla.dialogs import *
from mojo.UI import AskString
import os
import sys

currentDir = os.path.dirname(os.path.abspath(__file__))
print(currentDir)

docTitle = "interp_anime" # update this for your output file name
saveOutput = True
outputDir = "exports"
autoOpen = False

fileFormat = "gif" # pdf, gif, or mp4 # if just 1 frame, can also be jpg or png

frames = 40


def normalRGB(r, g, b):
    """Use like: fill(*normalRGB(255,255,255))"""
    r1, g1, b1 = r / 255, g / 255, b / 255
    return((r1, g1, b1))


timestamp = datetime.now().strftime("%Y_%m_%d")

# glyphToAnimate = AskString('Enter glyph name to animate')
# startFont = getFile("Select file to start animation from", allowsMultipleSelection=False, fileTypes=["ufo"])
# endFont = getFile("Select file to end animation at", allowsMultipleSelection=False, fileTypes=["ufo"])

# glyphToAnimate = 'r.mono' #'x.italic'
# startFont = "/Users/stephennixon/type-repos/recursive/src/masters/mono/Recursive Mono-Casual B Slanted.ufo"
# endFont = "/Users/stephennixon/type-repos/recursive/src/masters/mono/Recursive Mono-Linear A.ufo"

glyphToAnimate = 'ampersand' #'x.italic'
startFont = "/Users/stephennixon/type-repos/recursive/src/masters/mono/Recursive Mono-Casual B.ufo"
endFont = "/Users/stephennixon/type-repos/recursive/src/masters/mono/Recursive Mono-Linear B.ufo"

print(startFont)
print(endFont)

# settings
#glyphScale = 0.975 # descender to ascender
#glyphScale, yShift = 1.5, 0.93 # baseline to x-height
glyphScale, yShift = 1.25, 0.6 #capHeight
W, H = 1080, 1080

captionSize = 16

def hex2rgb(hex):
    h = hex.lstrip('#')
    RGB = tuple(int(h[i:i+2], 16) for i in (0, 2 ,4))
    r1, g1, b1 = RGB[0] / 255, RGB[1] / 255, RGB[2] / 255
    return(r1, g1, b1)

colors = {
    "points": hex2rgb("#ffffff"),
    "offcurvePoints":  hex2rgb("#ffffff"),
    "pointFill": hex2rgb("#0051FF"),         # primary blue
    "background": hex2rgb("#080822"),        # dark blue
    "glyphBox": hex2rgb("#080811"), #(0,0,0),
    "glyphFill": (0.8,0.8,1,0.2),
    "glyphStroke": hex2rgb("#B3CAFF"),
    "guides": hex2rgb("#003099"),
    "labels": (1,1,1)
}

def interpolate(a, b, t):
    return(a + (b-a) * t)


def getCurveValue(t, curviness, axMin, axMax, loop="loop"):
    from fontTools.misc.bezierTools import splitCubicAtT
    # curve = ((0,0), (W*curviness, 0), (W-(W*curviness),H), (W,H)) # fast to slow to fast (not sure?)
    curve = ((0,0), (0, H*curviness), (W,H-(H*curviness)), (W,H)) # slow to fast to slow, based on x over time (bell curve)
    # curve = ((0, 20), (-2689.98, 30), (-2000,H), (W,H))
    split = splitCubicAtT(*curve, t)
    x, y = split[0][-1]
    # Scale the y value to the range of 0 and 1, assuming it was in a range of 0 to 1000
    # f = y / H # for some reason, y isn't working as well for me as x to attain different curves...
    f = x / W
        
    # go up with curve for first half, then back down
    if loop is "loop":
        if t <= 0.5:
            f *= 2
        else:
            f = 1 - (f - 0.5) * 2
            
    value = interpolate(axMin, axMax, f)
            
    # return value, x, y
    return value


f1 = OpenFont(startFont, showInterface=False)
f2 = OpenFont(endFont, showInterface=False)


# collect vertical metrics
metricsYf1 = {
    "b": 0,
    "d": f1.info.descender,
    "x": f1.info.xHeight,
    "c": f1.info.capHeight,
    "a": f1.info.ascender,
}

metricsYf2 = {
    "b": 0,
    "d": f2.info.descender,
    "x": f2.info.xHeight,
    "c": f2.info.capHeight,
    "a": f2.info.ascender,
}

# get box height
boxHeight = (max(metricsYf1.values()) - min(metricsYf1.values())) * glyphScale
boxY = (H - boxHeight) * 0.5

# ------------------------------------------------------------------
# draw glyphs

for frame in range(frames):
    
    #TODO: add curve to factor
    

    
    # if frame <= frames/2:
    #     t = frame*2/(frames)
    # else:
    #     t = 1 - (frame*2/(frames-1)-1)
    
    t = frame/frames
    factor = getCurveValue(t, 1, 0, 1)
    
    
    g = RGlyph()
    g.interpolate(factor, f1[glyphToAnimate], f2[glyphToAnimate])

    # get glyph
    # g = f1[glyphToAnimate]
    boxWidth = g.width * glyphScale

    # make new page
    newPage(W, H)
    fill(*colors["background"])
    #fill(*blueDark2)
    rect(0,0,W, H)

    # calculate origin position
    x = (W - boxWidth) * 0.5
    y = boxY + abs(f1.info.descender) * glyphScale * yShift

    # collect horizontal metrics
    guidesX = {x, x + boxWidth}

    # --------
    # draw box
    # --------

    save()

    fill(*colors["glyphBox"])
    rect(x, boxY, boxWidth, boxHeight)
    restore()

    # -----------
    # draw guides
    # -----------

    save()
    lineDash(2, 2)
    stroke(*colors["guides"])

    # draw guides x
    for guideX in guidesX:
        line((guideX, 0), (guideX, height()))

    # draw guides y
    for key in metricsYf1.keys():
        if key == "x":
            guideY = interpolate(metricsYf1[key], metricsYf2[key], factor) * glyphScale + y
            line((0, guideY), (width(), guideY))
        else:
            guideY = y + metricsYf1[key] * glyphScale
            line((0, guideY), (width(), guideY))

    restore()

    # ----------
    # draw glyph
    # ----------

    save()
    #fill(None)
    fill(*colors["glyphFill"])
    stroke(*colors["glyphStroke"])
    strokeWidth(1)
    lineJoin('round')
    translate(x, y)
    scale(glyphScale)
    drawGlyph(g)
    restore()

    # ------------
    # draw points
    # ------------

    oncurveSize = 8

    offcurveSize = 4

    save()
    translate(x, y)
    scale(glyphScale)
    for c in g:
        for bPt in c.bPoints:
            pt = bPt.anchor
            ptX = pt[0]
            ptY = pt[1]
        
            # draw offcurve points
            ptIn = bPt.bcpIn
            ptOut = bPt.bcpOut 
        
            fill(*colors["pointFill"])
        
            if abs(ptIn[0]) > 0 or abs(ptIn[1]) > 0:
                ptInX = pt[0]+ptIn[0]
                ptInY = pt[1]+ptIn[1]
                stroke(*colors["points"])
                line((ptX, ptY), (ptInX, ptInY))
                stroke(1)
                rect(ptInX - offcurveSize/2, ptInY - offcurveSize/2, offcurveSize, offcurveSize)
            
        
            if abs(ptOut[0]) > 0 or abs(ptOut[1]) > 0:
                ptOutX = pt[0]+ptOut[0]
                ptOutY = pt[1]+ptOut[1]
                stroke(*colors["points"])
                line((ptX, ptY), (ptOutX, ptOutY))
                stroke(1)
                rect(ptOutX - offcurveSize/2, pt[1]+ptOut[1] - offcurveSize/2, offcurveSize, offcurveSize)
            
            
            # now draw oncurve point so it's on top
            fill(*colors["pointFill"])
            stroke(1)

            if bPt.type == "corner":
                rect(ptX - oncurveSize/2, ptY - oncurveSize/2, oncurveSize, oncurveSize)
            else:
                oval(ptX - oncurveSize/2, ptY - oncurveSize/2, oncurveSize, oncurveSize)
                
    restore()

    # ------------
    # draw caption
    # ------------

    captionX = captionSize
    captionW = width() - captionSize * 2
    captionH = captionSize * 2

    save()
    font('RecursiveMonoLnr-Regular')
    fontSize(captionSize)
    fill(*colors["labels"])

    # top
    captionY = height() - captionSize * 3
    captionBox = captionX, captionY, captionW, captionH
    textBox(glyphToAnimate, captionBox, align='left')
    if g.unicode:
        uni = str(hex(g.unicode)).replace("0x", '')
        uni = uni.zfill(4).upper()
        textBox(uni, captionBox, align='right')

    # bottom
    captionY = 0
    captionBox = captionX, captionY, captionW, captionH
    textBox('%.2f' % g.width, captionBox, align='center')
    if g.bounds:
        textBox('%.2f' % g.leftMargin, captionBox, align='left')
        textBox('%.2f' % g.rightMargin, captionBox, align='right')

    restore()

# ------------
# save image
# ------------

if saveOutput:
    import datetime

    now = datetime.datetime.now().strftime("%Y_%m_%d-%H_%M") # -%H_%M_%S

    if not os.path.exists(f"{currentDir}/{outputDir}"):
        os.makedirs(f"{currentDir}/{outputDir}")

    path = f"{currentDir}/{outputDir}/{docTitle}-{now}.{fileFormat}"

    print("saved to ", path)

    saveImage(path)

    if autoOpen:
        os.system(f"open --background -a Preview {path}")

