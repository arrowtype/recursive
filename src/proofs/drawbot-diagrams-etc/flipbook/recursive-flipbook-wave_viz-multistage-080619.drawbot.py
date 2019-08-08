# make flipbook pages for an animated specimen
# https://codepen.io/thundernixon/pen/wVypxe?editors=1100

# TODO: eliminate reliance on 100 frames (link curve dict to t, not to frame)


from drawBot import * # requires drawbot to be installed as module
import datetime
from fontTools.misc.bezierTools import splitCubicAtT


newDrawing()
# fontFam = "Rec Mono Beta013 Var"

fontFam = "/Users/stephennixon/type-repos/recursive/src/proofs/drawbot-diagrams-etc/flipbook/fonts/Recursive-mono-full--w_ital_slnt-2019_07_25.ttf"
frames = 100
format = "gif"

frontmatter = False
debug = True

# bookSize = 3.5
# DPI = 150
# pixels = DPI*bookSize

pixels = 1000



W, H = pixels, pixels # size is 72 dpi * bookSize



minWeight = 300.01
maxWeight = 899.99

minExpression = 0.01
maxExpression = 1

maxSlant = 0
minSlant = -15
    

def interp(a, b, t):
    distance = b-a
    return(a + distance * t)


# ---------------------------------------------------------
# ANIMATION -----------------------------------------------

curviness = 0.7
        
def getCurveXY(t):
    currrve = ((0,0), (pixels*curviness, 22), (pixels-(pixels*curviness),pixels), (pixels,pixels))
    split = splitCubicAtT(*currrve, t)
    x,y = split[0][-1][0], split[0][-1][1]
    return(x,y)

curveDict = {}

for frame in range(frames+1):
    # frame = frame + 1
    t = frame / frames    
    x,y = getCurveXY(t)

    curveDict[t] = (x,y)

if debug:
    import pprint
    pp = pprint.PrettyPrinter(width=80, compact=False)
    pp.pprint(curveDict)

for frame in range(frames):
    # frame = frame + 1
    
    newPage(W, H)
    font(fontFam)
    # font("fonts/Recursive-mono-full--w_ital_slnt-2019_07_24.ttf")
    
    frameDuration(1/60)
    fill(0)
    rect(0,0,W,H)
    
    t = frame / frames 
    x,y = getCurveXY(t)
    
    fill(1)
    
    factor = y / pixels
    

    if frame >= frames*0 and frame <= frames*0.25:

        xprn = (0.001,  0.5)
        wght = (300.01, 800 - 0.01)
        slnt = (0.01,   -7.5)
        currentItal = 0

        startPos = curveDict[0.0][1]
        endPos = curveDict[0.25][1]

        stepRange = endPos - startPos

        factor = (y - startPos ) / stepRange

    if frame > frames*0.25 and frame <= frames*0.5:
        xprn = (0.5, 1)
        wght = (800.01, 900 - 0.01)
        slnt = (-7.5, -15)
        currentItal = 0

        startPos = curveDict[0.25][1]
        endPos = curveDict[0.5][1]

        stepRange = endPos - startPos

        factor = (y - startPos ) / stepRange
        
        
    if frame > frames*0.5 and frame <= frames * 0.75:
        xprn = (1, 0.5)
        wght = (900 - .01, 800 + 0.01)
        slnt = (-15, -7.5)
        currentItal = 1

        startPos = curveDict[0.5][1]
        endPos = curveDict[0.75][1]

        stepRange = endPos - startPos

        factor = (y - startPos ) / stepRange
        
    if frame > frames*0.75 and frame <= frames * 1.0:
        xprn = (0.5, 0)
        wght = (800 - .01, 300 + 0.01)
        slnt = (-7.5, 0)
        currentItal = 1

        startPos = curveDict[0.75][1]
        endPos = curveDict[1.0][1]

        stepRange = endPos - startPos

        factor = (y - startPos ) / stepRange
    
    currentXprn = interp(xprn[0], xprn[1], factor)
    currentWght = interp(wght[0], wght[1], factor)
    currentSlnt = interp(slnt[0], slnt[1], factor)
    
    fontVariations(
        wght=currentWght,
        XPRN=currentXprn,
        slnt=currentSlnt,
        ital=currentItal
        )
    
    
    padding = W*0.025
    
    fontSize(W/1.4)
    text("rw", (W/15, padding*2)) # H/12
    
    fontSize(W/30)
    
    # padding = 0.1
    # text(str(round(currentWght)), (((W*0.1)+(W*completionOnCurve * 0.7)), H *0.7))
    
    x = str('{:4.2f}'.format(currentXprn))
    w = str('{:3.0f}'.format(currentWght))
    s = str('{:5.2f}'.format(abs(currentSlnt)))
    i = str('{:4.2f}'.format(currentItal))
    # text(f"prop {str(0)}   xprn {x}   wght {w}   slnt -{s}   ital {i}   {frame+1}", (((W*0.025)), H *0.025))

    # BAR CHARTS FOR AXES

    # minVal, maxVal, currentVal

    minXprn, maxXprn = 0, 1
    xprnVal = interp(minXprn, maxXprn, currentXprn)
    minWght, maxWght = 300, 900
    wghtVal = interp(minWght, maxWght, currentWght)
    minSlnt, maxSlnt = 0, -15
    slntVal = interp(minSlnt, maxSlnt, currentSlnt)
    minItal, maxItal = 0, 1
    italVal = interp(minItal, maxItal, currentItal)


    currentProp = 0
    minProp, maxProp = 0, 1
    propVal = interp(minProp, maxProp, currentProp)


    infoSpacing = H * 0.075

    infoHeight = H * 0.5

    ovalSize = padding
    rect(padding, infoHeight, (W- (padding*2)) * italVal/maxItal, 2)
    text(f"ital {i}", (((W*0.025)), infoHeight + padding))

    infoHeight += infoSpacing
    rect(padding, infoHeight, (W- (padding*2)) * slntVal/maxSlnt, 2)
    text(f"slnt -{s}", (((W*0.025)), infoHeight + padding))

    infoHeight += infoSpacing
    rect(padding, infoHeight, (W- (padding*2)) * wghtVal/maxWght, 2)
    text(f"wght {w}", (((W*0.025)), infoHeight + padding))
    
    infoHeight += infoSpacing
    # rect(padding, infoHeight, (W- (padding*2)) * xprnVal/maxXprn, 2)
    fill(0.5,0.5,0.5,1)
    rect(padding, infoHeight, (W- (padding*2)), 2)
    fill(1)
    oval(((W- (padding*2)) * xprnVal/maxXprn) -(ovalSize/2), infoHeight-(ovalSize/2), ovalSize, ovalSize)
    text(f"xprn {x}", (((W*0.025)), infoHeight + padding))


    currentProp = 0
    infoHeight += infoSpacing
    rect(padding, infoHeight, (W- (padding*2)) * propVal/maxProp, 2)
    text(f"prop {currentProp}", (((W*0.025)), infoHeight + padding))

    # currentXprn = interp(xprn[0], xprn[1], factor)
    # currentWght = interp(wght[0], wght[1], factor)
    # currentSlnt = interp(slnt[0], slnt[1], factor)


    print("*", end=" ")

    if debug:

        print(str(frame).ljust(3), " | factor: ", str(round(factor, 3)).ljust(5)," | t: ", str(round(t, 3)).ljust(5), " | wght: ", str(round(currentWght, 0)).ljust(5),\
        " | y: ", str(round(y, 3)))

        ## visual of each stage along curve
        # fill(0,1,0,1)
        # quarter = curveDict[0.25][0]
        # rect(quarter, 0, 2, H)
        # half = curveDict[0.5][0]
        # rect(half, 0, 2, H)
        # threequarters = curveDict[0.75][0]
        # rect(threequarters, 0, 2, H)

        ## overall y value progress bar
        # fill(1,0,1,1)
        # size = pixels/pixels * 2
        # rect(0,H*.66, W*y/W, size)      # y - curved


        

        for i in range(frames):
            
            fill(0.6,0.6,0.6,0.25)
            t = i / frames

            x,y = getCurveXY(t)
            
            size = pixels/pixels * 4
            # oval(x-size/2, (y*0.375)+(H/12)-(size/2), size, size) # covering letters
            oval(x-size/2, (y)-(size/2), size, size)
            
        fill(1,0,1,1)
        t = frame / frames
        
        x,y = getCurveXY(t)
                
        size = pixels/pixels * 6
        # oval(x-size/2, (y*0.375)+(H/12)-(size/2), size, size) # covering letters
        oval(x-size/2, (y)-(size/2), size, size)


now = datetime.datetime.now().strftime("%Y_%m_%d-%H") # -%H_%M_%S

saveImage("/Users/stephennixon/type-repos/recursive/src/proofs/drawbot-diagrams-etc/flipbook/exports/recursive-flipbook-axes-" + now + "." + format)

endDrawing()