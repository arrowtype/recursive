from drawBot import * # requires drawbot to be installed as module
import datetime
from fontTools.misc.bezierTools import splitCubicAtT
newDrawing() # for drawbot module

# ---------------------------------------------------------
# CONFIGURATION -------------------------------------------

debug = False # overlays curve visualizations

prop = 1

if prop is 1:
    fontFam = "/Users/stephennixon/type-repos/recursive/src/proofs/drawbot-diagrams-etc/flipbook/fonts/Recursive-sans--w_ital_slnt-2019_08_13.ttf"
    foreground = 0
    background = 1
else:
    fontFam = "/Users/stephennixon/type-repos/recursive/src/proofs/drawbot-diagrams-etc/flipbook/fonts/Recursive-mono-full--w_ital_slnt-2019_08_12.ttf"
    foreground = 1
    background = 0
    
frames = 60 # 192
frameRate = 1/60 # only applicable to mp4
format = "mp4" # pdf, gif, or mp4

bookSize = 3.5 # inches
DPI = 300 # dots per inch
pixels = DPI*bookSize

W, H = pixels, pixels # do not edit this
# textSize = W/60
textSize = W*.023809524 # 6pt / 8 px

# W, H = 1080, 1920   # instagram story format
# textSize = W/10     # instagram story format

rwSize = W/1.4

# curviness = 0.7 # amount of easing steepness. 0 to 1.

padding = W*0.085714286 # 0.3 inches

# ---------------------------------------------------------
# ANIMATION -----------------------------------------------

def drawMargins():
    # top, right, bottom, left
    margins = (0.75, 0.3, 0.3, 0.3)
    thickness = 1
    fill(0,1,1)

    # x, y, w, h
    rect(0, H - margins[0]*DPI, W, thickness)  # top
    rect(margins[1]*DPI, 0, thickness, H)      # right
    rect(W - margins[2]*DPI, 0, thickness, H)  # bottom
    rect(0, margins[3]*DPI, W, thickness)      # left
    
    fill(0,1,1,0.5)
    rect(0, H*0.5, W, thickness)      # middle
    rect(W*0.5, 0, thickness, H)      # center


def interpolate(a, b, t):
    distance = b-a
    return(a + distance * t)

# You can even make this getCurve() function do a lot more for you, I'll sketch pseudo code here:


def getCurveValue(t, curviness, axMin, axMax, loop="loop"):
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
            
    return value, x, y

def getSlantValue(t, axMin, axMax):
    if t <= 0.5:
        t = t * 2
        f = interpolate(0, 1, t)
    else:
        t = (t - 0.5) * 2
        f = interpolate(1, 0, t)
    
    value = interpolate(axMin, axMax, f)

    return value


def getWeightValue(t, curviness, axMin, axMax):

    curve = ((0,0), (0, H*curviness), (W,H-(H*curviness)), (W,H)) # slow to fast to slow (bell curve)
    split = splitCubicAtT(*curve, t)
    x, y = split[0][-1]
    # if t <= 0.75:
    if t <= 0.5:
        # Scale the y value to the range of 0 and 1, assuming it was in a range of 0 to 1000
        f = x / W * 2
        
        # f *= 2
        value = interpolate(axMin, 800, f)
        
    else:
        # curve = ((W/2,H), (W/2,H-(H*curviness)), (W, H*curviness),(W,0)) # slow to fast to slow (bell curve)
        # curve = ((0,0), (0, H*curviness), (W/2,H-(H*curviness)), (W/2,H)) # slow to fast to slow (bell curve)
        split = splitCubicAtT(*curve, t)
        x, y = split[0][-1]
        # Scale the y value to the range of 0 and 1, assuming it was in a range of 0 to 1000
        f = x / W
        # f = 1 - (f - 0.5) * 2 # reversed
        f = (f - 0.5) * 2 

        value = interpolate(800, axMax, f)

    return value, x, y


def getItalValue(t):
    if t <= 0.5:
        value = 0
    elif t > 0.5 and t <= 0.625:
        value = 0.5
    else:
        value = 1
    return value


for frame in range(frames):

    newPage(W, H)
    font(fontFam)
    fontSize(textSize)

    fill(background)
    rect(0,0,W,H)

    frameDuration(frameRate)
    

    t = frame / (frames - 1)

    xprnVals = getCurveValue(t, 0.5, 0.001, 0.999)
    wghtVals = getWeightValue(t, 0.7, 300.001, 899.999)
    slntVals = getSlantValue(t, 0.001, -14.999)
    italVals = getItalValue(t)

    fontVariations(wght=wghtVals[0], XPRN=xprnVals[0], slnt=slntVals, ital=italVals)

    

    # print(round(slntVal, 2), round(wghtVal, 2))
    
    size = padding * 0.375

    # fill(1,0,0)

    # rect(0,0,100,100)
    fill(foreground)
    
    fontSize(rwSize)
    overflow = textBox("rw", (0, padding - rwSize*0.3, W, rwSize*1.25), align="center")
    # a text box returns text overflow
    # text that did not make it into the box
    print(overflow)


    # ----------------------------------------------------------------------
    # BAR CHARTS / SLIDERS FOR AXES ----------------------------------------
    
    x = str('{:4.2f}'.format(xprnVals[0]))
    w = str('{:3.2f}'.format(wghtVals[0]))
    # s = str('{:05.2f}'.format(abs(slntVals)))
    s = str('{:5.2f}'.format(slntVals))
    i = str('{:4.2f}'.format(italVals))
    p = str('{:4.2f}'.format(prop))

    xprnVal = xprnVals[0]
    minWght, maxWght = 300, 900
    wghtVal = (wghtVals[0] - minWght) / (maxWght - minWght)
    minSlnt, maxSlnt = 0, -15
    # slntVal = abs(((slntVals - minSlnt) / (minSlnt - maxSlnt)))
    slntVal = ((slntVals - minSlnt) / (minSlnt - maxSlnt))
    minItal, maxItal = 0, 1
    italVal = italVals

    fontSize(textSize)
    

    if prop == 0:
        
        trackFill = "*"
        maxLength = 61
        def showAxisVals(label, value, valueString, infoHeight):

            # fontVariations(wght=wghtVals[0], XPRN=xprnVals[0], slnt=slntVals, ital=italVals)
            
            fill(foreground)
            
            textBox(label, (padding, infoHeight, (W- (padding*2)), textSize*1.75))
            
            textBox(valueString,(padding, infoHeight, (W- (padding*2)), textSize*1.75), align="right")

            with savedState():
                
                fontVariations(wght=500, XPRN=xprnVals[0], slnt=0)
                fill(foreground,foreground,foreground,0.25)
                textBox("".ljust(floor(maxLength), trackFill), (padding, infoHeight-textSize, (W- (padding*2)), textSize*1.75))
                
                fill(foreground,foreground,foreground,0.625)
                textBox("".ljust(floor(maxLength*value), trackFill), (padding, infoHeight-textSize, (W- (padding*2)), textSize*1.75))

            # reset this
            # fontVariations(wght=wghtVals[0], XPRN=xprnVals[0], slnt=slntVals, ital=italVals)
            
        infoSpacing = H * 0.056
        infoHeight = H * 0.5 + textSize
        showAxisVals("ital", italVal, i, infoHeight)

        infoHeight += infoSpacing
        showAxisVals("slnt", -slntVal, s, infoHeight)

        infoHeight += infoSpacing
        showAxisVals("wght", wghtVal, w, infoHeight)

        infoHeight += infoSpacing
        showAxisVals("XPRN", xprnVal, x, infoHeight)

        propVal = prop
        infoHeight += infoSpacing
        showAxisVals("PROP", propVal, p, infoHeight)

        

    else: # if proportion is sans
        trackSize = padding*0.025
        ovalSize = padding*0.1875

        def showAxisVals(label, value, valueString, infoHeight):
            fill(foreground,foreground,foreground,0.25)
            rect(padding, infoHeight, (W- (padding*2)), trackSize)
            fill(foreground)
            oval(((W - (padding*2)) * value) -(ovalSize/2) + padding,infoHeight-(ovalSize/2)+(trackSize/2), ovalSize, ovalSize)

            textBox(label, (padding, infoHeight, (W- (padding*2)), textSize*1.75))
                
            textBox(valueString,(padding, infoHeight, (W- (padding*2)), textSize*1.75), align="right")
            
        infoSpacing = H * 0.056
        infoHeight = H * 0.5 + textSize
        showAxisVals("Italic", italVal, i, infoHeight)

        infoHeight += infoSpacing
        showAxisVals("Slant", -slntVal, s, infoHeight)

        infoHeight += infoSpacing
        showAxisVals("Weight", wghtVal, w, infoHeight)

        infoHeight += infoSpacing
        showAxisVals("Expression", xprnVal, x, infoHeight)

        propVal = prop
        infoHeight += infoSpacing
        showAxisVals("Proportion", propVal, p, infoHeight)


    # ----------------------------------------------------------------------
    # PAGE NUMBER ----------------------------------------------------------

    # page number
    textBox(str(frame + 1), (padding, padding*0.5, (W- (padding*2)), textSize*1.5), align="right")


    
    
    print("T: " + str(t))
    # ----------------------------------------------------------------------
    # DEBUGGING VISUALS ----------------------------------------------------
    if debug:
        
        print("-------------------------------------")
        print("#: " + str(frame))
        print("x: " + str(round(abs(xprnVals[0]), 0)))
        print("w: " + str(round(abs(wghtVals[0]), 0)))
        print("s: " + str(round(abs(slntVals), 2)))
        print('')

        drawMargins()
        
        # fill(1,0,1)
        # fontSize(textSize/2)
        # # text("t" + str(round(abs(t), 2)), (W*t, padding))
        # text("@", (W*t, padding))
        # text("s" + str(round(abs(slntVals), 2)), (slntVals[1]-W/10, slntVals[2]+textSize))
        # text("w" + str(round(wghtVals[0], 0)), (wghtVals[1]-W/10, wghtVals[2]))
        # text("x" + str(round(xprnVals[0], 2)), (xprnVals[1]-W/10, xprnVals[2]-textSize))

        
        # size = padding * 0.15
        # x8 = getCurveValue(t, 0.8, 0, W, loop="nope")[0]
        # # oval(x8-size/2, (padding/2)-(size/2), size, size)
        # text("0.8", (x8-size/2, (padding/2)-(size/2)))
        
        # x3 = getCurveValue(t, 0.3, 0, W, loop="nope")[0]
        # text("0.3", (x8-size/2, (padding/2)-(size*1.5)))


    
    # for i in range(frames):
    #     fill(0.6,0.6,0.6,0.375)  
    #     t = i / (frames - 1)
    
    #     slntVal = getSlntValue(t)
    
    
    #     x,y = getCurveXY(t)
    #     oval(x-size/2, (y)-(size/2), size, size)


now = datetime.datetime.now().strftime("%Y_%m_%d-%H") # -%H_%M_%S

saveImage(f"/Users/stephennixon/type-repos/recursive/src/proofs/drawbot-diagrams-etc/flipbook/exports/multi-timing-curves-prop_{prop}-{now}.{format}")

endDrawing()