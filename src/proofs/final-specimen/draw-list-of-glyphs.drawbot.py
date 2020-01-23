
'''
    Glyph Proofer
    
    Run this in RoboFont.
'''



saveOutput = True
outputDir = "exports"
docTitle = "recursive-beziers"
fileFormat = "svg"

# exampleFont = "/Users/stephennixon/type-repos/recursive/src/masters/mono/Recursive Mono-Casual C Slanted.ufo"
# glyphNames = "a.italic".split()

# exampleFont = "/Users/stephennixon/type-repos/recursive/src/masters/mono/Recursive Mono-Casual A.ufo"
# glyphNames = "S".split()

# exampleFont = "/Users/stephennixon/type-repos/recursive/src/masters/mono/Recursive Mono-Linear C.ufo"
# glyphNames = "Z".split()

# exampleFont = "/Users/stephennixon/type-repos/recursive/src/masters/mono/Recursive Mono-Linear B Slanted.ufo"
# glyphNames = "l.italic".split()

exampleFont = "/Users/stephennixon/type-repos/recursive/src/masters/mono/Recursive Mono-Casual A.ufo"
glyphNames = "g".split()

f = OpenFont(exampleFont, showInterface=False)

# settings
glyphScale = 0.8
canvasWidth = 650
canvasHeight = 900

captionSize = 14

def hex2rgb(hex):
    h = hex.lstrip('#')
    RGB = tuple(int(h[i:i+2], 16) for i in (0, 2 ,4))
    r1, g1, b1 = RGB[0] / 255, RGB[1] / 255, RGB[2] / 255
    return(r1, g1, b1)


colors = {
    "points": hex2rgb("#000000"), # primary blue
    "offcurvePoints":  hex2rgb("#000000"),
    "pointFill": hex2rgb("#ffffff"),      
    "handles": hex2rgb("#000000"),   
    "background": hex2rgb("#0050FF"),        # dark blue
    "glyphBox": hex2rgb("#0050FF"), #(0,0,0),
    "glyphFill": (*hex2rgb("#ffffff"),1),
    "glyphStroke": (*hex2rgb("#222266"),1), #hex2rgb("#B3CAFF"),
    "guides": (*hex2rgb("#FFFFFF"), 0.25), #hex2rgb("#003099"),
    "labels": (0,0,0),
    "connections": hex2rgb("#0050FF")
}

# collect vertical metrics
metricsY = {
    0,
    f.info.descender,
    f.info.xHeight,
    f.info.capHeight,
    f.info.ascender,
}

# get box height
boxHeight = (max(metricsY) - min(metricsY)) * glyphScale
boxY = (canvasHeight - boxHeight) * 0.5

# get glyph names
# glyphNames = f.selectedGlyphNames if len(f.selectedGlyphs) else f.keys()


# draw glyphs
for glyphName in f.glyphOrder:
    if not glyphName in glyphNames:
        continue

    # get glyph
    g = f[glyphName]
    boxWidth = g.width * glyphScale

    # make new page
    newPage(canvasWidth, canvasHeight)
    fill(*colors["background"])
    rect(0,0,canvasWidth, canvasHeight)

    # calculate origin position
    x = (canvasWidth - boxWidth) * 0.5
    y = boxY + abs(f.info.descender) * glyphScale

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
    for guideY in metricsY:
        guideY = y + guideY * glyphScale
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
            
            fill(*colors["offcurvePoints"])
            
            if abs(ptIn[0]) > 0 or abs(ptIn[1]) > 0:
                ptInX = pt[0]+ptIn[0]
                ptInY = pt[1]+ptIn[1]
                stroke(*colors["handles"])
                line((ptX, ptY), (ptInX, ptInY))
                stroke(*colors["offcurvePoints"])
                rect(ptInX - offcurveSize/2, ptInY - offcurveSize/2, offcurveSize, offcurveSize)
                
            
            if abs(ptOut[0]) > 0 or abs(ptOut[1]) > 0:
                ptOutX = pt[0]+ptOut[0]
                ptOutY = pt[1]+ptOut[1]
                stroke(*colors["handles"])
                line((ptX, ptY), (ptOutX, ptOutY))
                stroke(*colors["offcurvePoints"])
                rect(ptOutX - offcurveSize/2, pt[1]+ptOut[1] - offcurveSize/2, offcurveSize, offcurveSize)
                
                
            # now draw oncurve point so it's on top
            fill(*colors["pointFill"])
            stroke(*colors["points"])

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
    textBox(g.name, captionBox, align='left')
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

    
    # path = f"/Users/stephennixon/type-repos/recursive/src/proofs/robofont-drawbot-specimens-and-diagrams/draw-beziers/exports/beziers-glyph_{glyphName}-{timestamp}.pdf"
    # saveImage(path)

    if saveOutput:
        import datetime
        import os
        
        currentDir = os.path.dirname(os.path.abspath(__file__))

        now = datetime.datetime.now().strftime("%Y_%m_%d-%H_%M") # -%H_%M_%S

        if not os.path.exists(f"{currentDir}/{outputDir}"):
            os.makedirs(f"{currentDir}/{outputDir}")

        path = f"{currentDir}/{outputDir}/{docTitle}-{glyphName}-{now}.{fileFormat}"

        print("saved to ", path)

        saveImage(path)

    
