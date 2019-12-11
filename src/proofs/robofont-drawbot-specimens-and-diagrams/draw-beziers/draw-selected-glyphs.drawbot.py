'''
    Glyph Proofer
    
    This must be used within the Drawbot extension for RoboFont.
'''

from datetime import datetime

timestamp = datetime.now().strftime("%Y_%m_%d")

f = CurrentFont()

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


blueDark2 = hex2rgb("#002066")        # a bit darker still
blueDark1 = hex2rgb("#003099")        # a bit darker still
blueDark = hex2rgb("#0040CC")         # a bit darker
blue = hex2rgb("#0051FF")             # primary blue
blueLight = hex2rgb("#6696FF")        # a bit lighter
blueLight1 = hex2rgb("#B3CAFF")       # a bit lighter still

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
glyphNames = f.selectedGlyphNames if len(f.selectedGlyphs) else f.keys()

# draw glyphs
for glyphName in f.glyphOrder:
    if not glyphName in glyphNames:
        continue

    # get glyph
    g = f[glyphName]
    boxWidth = g.width * glyphScale

    # make new page
    newPage(canvasWidth, canvasHeight)
    fill(0.05)
    #fill(*blueDark2)
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
    
    fill(*blue)
    rect(x, boxY, boxWidth, boxHeight)
    restore()

    # -----------
    # draw guides
    # -----------

    save()
    lineDash(2, 2)
    stroke(*blueDark1)

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
    fill(*blueDark)
    stroke(*blueLight)
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
            
            fill(*blue)
            
            if abs(ptIn[0]) > 0 or abs(ptIn[1]) > 0:
                ptInX = pt[0]+ptIn[0]
                ptInY = pt[1]+ptIn[1]
                stroke(*blueLight1)
                line((ptX, ptY), (ptInX, ptInY))
                stroke(1)
                rect(ptInX - offcurveSize/2, ptInY - offcurveSize/2, offcurveSize, offcurveSize)
                
            
            if abs(ptOut[0]) > 0 or abs(ptOut[1]) > 0:
                ptOutX = pt[0]+ptOut[0]
                ptOutY = pt[1]+ptOut[1]
                stroke(*blueLight1)
                line((ptX, ptY), (ptOutX, ptOutY))
                stroke(1)
                rect(ptOutX - offcurveSize/2, pt[1]+ptOut[1] - offcurveSize/2, offcurveSize, offcurveSize)
                
                
            # now draw oncurve point so it's on top
            fill(*blueLight)
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
    font('RecursiveMonoLinearB027st-Rg')
    fontSize(captionSize)
    fill(*blueLight)

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

    
    path = f"/Users/stephennixon/type-repos/recursive/src/proofs/robofont-drawbot-specimens-and-diagrams/draw-beziers/exports/beziers-glyph_{glyphName}-{timestamp}.pdf"
    saveImage(path)
    
