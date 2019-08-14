from drawBot import * # requires drawbot to be installed as module
import datetime
from fontTools.misc.bezierTools import splitCubicAtT
newDrawing() # for drawbot module

# ---------------------------------------------------------
# CONFIGURATION -------------------------------------------

prop = 0 # 0 for mono, 1 for sans

export = True
autoOpen = True
book = True
debug = True # overlays curve visualizations

frames = 2 # 192
frameRate = 1/30 # only applicable to mp4
format = "pdf" # pdf, gif, or mp4

DPI = 72 # dots per inch – must be 72 to print at dimensions set in inches

endPages = 0


bookSize = 3.5 # inches
marginSize = 0.25 # inches

# marginSides = 0.3
# marginBottom = 0.2

margins = (0.75, 0.3, 0.2, 0.3)



textPts = 6.75
textLineHeight = 1.25
rwPts =  152

# ---------------------------------------------------------

recursiveVersion="Beta v1.014"


pixels = DPI*bookSize

marginTop, marginRight, marginBottom, marginLeft = margins[0]*DPI, margins[1]*DPI, margins[2]*DPI, margins[3]*DPI

padding = marginRight



paddingSides = marginRight
paddingBottom = marginBottom

W, H = pixels, pixels # do not edit this


def computeFontSizePoints(pts):
    return W * (pts / (bookSize * 72))
    
textSize = computeFontSizePoints(textPts)
rwSize =  computeFontSizePoints(rwPts)

if prop is 0:
    fontFam = "/Users/stephennixon/type-repos/recursive/src/proofs/drawbot-diagrams-etc/flipbook/fonts/Recursive-mono--w_ital_slnt-2019_08_13.ttf"
    foreground = 0
    background = 1
    docTitle = "recursive-mono-flipbook_side_1"
else:
    fontFam = "/Users/stephennixon/type-repos/recursive/src/proofs/drawbot-diagrams-etc/flipbook/fonts/Recursive-sans--w_ital_slnt-2019_08_13.ttf"
    foreground = 0
    background = 1
    docTitle = "recursive-sans-flipbook_side_2"

# this will draw cyan guides to help align content
def drawMargins():
    # top, right, bottom, left
    # margins = (0.75, 0.25, 0.25, 0.25)
    margins = (0.75, 0.3, 0.2, 0.3)
    thickness = 1
    fill(0,1,1)

    # x, y, w, h
    rect(0, H - margins[0]*DPI, W, thickness)  # top
    rect(W - margins[1]*DPI, 0, thickness, H)      # right
    rect(0, margins[2]*DPI, W, thickness)  # bottom
    rect(margins[3]*DPI, 0, thickness, H)      # left
    
    fill(0,1,1,0.5)
    rect(0, H*0.5, W, thickness)      # middle
    rect(W*0.5, 0, thickness, H)      # center

# ---------------------------------------------------------
# FRONTMATTER ---------------------------------------------

credits=f"""\
Recursive ({recursiveVersion}, Aug 2019,  d430fa628c)

Made by Arrow Type. Type design by Stephen Nixon, with contributions from Katja Schimmel, Lisa Huang, and Rafał Buchner, plus early guidance from faculty and instructors for KABK TypeMedia 2018. Type mastering by Ben Kiel.

Book design by Math Practice.
Typeset with DrawBot by Stephen Nixon.

→ https://recursive.design

Recursive has been sponsored by Google Fonts, through which it will soon be released. Recursive is released under the SIL Open Font License and can be freely used in or adapted for any project.
"""

tagline = "A highly customizable variable font\nfor design, code, and UI."

description = """\
Recursive is a versatile new variable font with five stylistic axes. These variation axes enable customizable control within five stylistic ranges: Proportion, Expression, Weight, Slant, and Italic. Carefully-planned named instances also allow selection within a set of predefined styles.

Recursive offers a range of personality, from a sturdy, rational Linear to a friendly, energetic Casual. It comes in two subfamilies: Mono & Sans. Within these subfamilies, characters maintain the exact same width across all font styles. This allows for smooth stylistic transitions without affecting line length, enabling new levels of typographic flexibility & interactivity.

Flip the pages to see Recursive in motion!
"""


if book:
    newPage(W, H)
    fill(background)
    rect(0,0,W, H)

    # CREDITS ---------------------------------------------

    newPage(W, H)
    fill(background)
    rect(0,0,W, H)

    
    fill(foreground)

    font(fontFam)
    fontSize(textSize)
    fontVariations(wght=450, XPRN=0.001, slnt=0, ital=0)

    if prop is 0:
        textBox(credits, (marginLeft,H - 2.86*DPI,W - (marginLeft * 2), textSize * 22))
    else:
        textBox(credits, (marginLeft,H - 2.86*DPI,W - (marginLeft * 3), textSize * 22))



    # logo

    googleLogoSize = computeFontSizePoints(15)

    font("Google Sans")

    fontSize(googleLogoSize)

    text("google_logo", (marginLeft,marginBottom*1.05))

    if debug:
        drawMargins()


    # DESCRIPTION ---------------------------------------------

    newPage(W, H)
    fill(background)
    rect(0,0,W, H)


    taglineSize = computeFontSizePoints(10)

    font(fontFam)

    fill(foreground)

    fontSize(taglineSize)
    fontVariations(wght=850, XPRN=1, slnt=-14.999, ital=1)

    textBox(tagline, (marginLeft,H - 1.065*DPI,W - marginLeft * 1.8, taglineSize * 2.5))

    fontSize(textSize)
    fontVariations(wght=450, XPRN=0.001, slnt=0, ital=0)


    if prop is 0:
        textBox(description, (marginLeft,H - 3.36*DPI, W - (marginLeft * 2), textSize * 22))
    else:
        # textBox(description, (padding,H - 2.86*DPI, W - (padding * 4.0), textSize * 22))
        textBox(description, (marginLeft,H - (3.475*DPI), W - (marginLeft * 3.0), textSize * 22))
        
    if debug:
        drawMargins()


# ---------------------------------------------------------
# ANIMATION -----------------------------------------------




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
    # elif t > 0.5 and t <= 0.625:
    #     value = 0.5
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
    
    if book:
        t = 1 - (frame / (frames - 1)) # reverse
    else:
        t = frame / (frames - 1) # forward

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
    overflow = textBox("rw", (0, padding - rwSize*0.20, W, rwSize*1.25), align="center")
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
        
        maxLength = 61
        def showAxisVals(label, value, valueString, infoHeight):

            # fontVariations(wght=wghtVals[0], XPRN=xprnVals[0], slnt=slntVals, ital=italVals)
            
            fill(foreground)
            
            textBox(label, (padding, infoHeight, (W- (padding*2)), textSize*1.625))
            
            textBox(valueString,(padding, infoHeight, (W- (padding*2)), textSize*1.625), align="right")

            with savedState():
                
                scale(1.008) # hack to make the asterisk metrics match the label/value text above
                
                fontVariations(wght=500, XPRN=xprnVals[0], slnt=0)
                fill(foreground,foreground,foreground,0.25)
                textBox("".ljust(floor(maxLength), "·"), (padding, infoHeight-textSize, (W- (padding*2)), textSize*1.625))
                
                fill(foreground,foreground,foreground,0.625)
                textBox("".ljust(floor(maxLength*value), "•"), (padding, infoHeight-textSize, (W- (padding*2)), textSize*1.625))

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
        trackSize = padding*0.05
        ovalSize = padding*0.2 # 0.1875

        def showAxisVals(label, value, valueString, infoHeight):
            fill(foreground,foreground,foreground,0.25)
            rect(padding, infoHeight, (W- (padding*2)), trackSize)
            fill(foreground)
            # oval(((W - (padding*2)) * value) -(ovalSize/2) + padding,infoHeight-(ovalSize/2)+(trackSize/2), ovalSize, ovalSize)
            oval(((W - (padding*2) - ovalSize) * value) + padding,infoHeight-(ovalSize/2)+(trackSize/2), ovalSize, ovalSize)

            textBox(label, (padding, infoHeight, (W- (padding*2)), textSize*1.625))
                
            textBox(valueString,(padding, infoHeight, (W- (padding*2)), textSize*1.625), align="right")
            
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
    
    with savedState():
        fontVariations(wght=400, XPRN=xprnVals[0], slnt=0, ital=0)

        footerHeight = marginBottom*0.84
        
        print(marginLeft)

        if prop == 0:
            textBox("Recursive Mono", (marginLeft, footerHeight, (W- (marginLeft*2)), textSize*1.5), align="left")
        else:
            textBox("Recursive Sans", (marginLeft, footerHeight, (W- (marginLeft*2)), textSize*1.5), align="left")

        # foundry name, nudged to the right just slightly
        textBox("Arrow Type", (W/2, footerHeight, (W- (padding*2)), textSize*1.5), align="left")
        # page number

        if book:
            textBox(str(frames-(frame)), (marginLeft, footerHeight, (W- (marginLeft*2)), textSize*1.5), align="right") # reverse
        else:
            textBox(str(frame + 1), (marginLeft, footerHeight, (W- (marginLeft*2)), textSize*1.5), align="right") # forward



    
    
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


# -----------------------------------------------------------------------------
# END PAGES -------------------------------------------------------------------

if book:
    for page in range(endPages):
        newPage(W, H)
        fill(background)
        rect(0,0,W, H)


endDrawing()

if save:
    now = datetime.datetime.now().strftime("%Y_%m_%d-%H") # -%H_%M_%S

    path = f"/Users/stephennixon/type-repos/recursive/src/proofs/drawbot-diagrams-etc/flipbook/exports/{docTitle}-{now}.{format}"

    print("saved to ", path)

    saveImage(path)

    if autoOpen:
        import os
        os.system(f"open --background -a Preview {path}")


