from drawBot import * # requires drawbot to be installed as module
import datetime
from fontTools.misc.bezierTools import splitCubicAtT
newDrawing() # for drawbot module

# ---------------------------------------------------------
# CONFIGURATION -------------------------------------------

prop = 0 # 0 for mono, 1 for sans

export = False
autoOpen = False
book = False
debug = False # overlays curve visualizations

frames = 48         # 192
frameRate = 1/15 # only applicable to mp4
format = "mp4" # pdf, gif, or mp4

DPI = 300 # dots per inch – must be 72 to printed at dimensions set in inches, 300 is nicer for screen display

if book:
    endPages = 4 #4
else:
    endPages = 0

bookSize = 3.5 # inches
marginSize = 0.25 # inches

# marginSides = 0.3
# marginBottom = 0.2

margins = (0.75, 0.3, 0.2, 0.3)



textPts = 7 # 6.75
textLineHeight = 1.5
headerPts = 14
headerLineHeight = 1.125
rwPts =  170 # 152

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
headerSize = computeFontSizePoints(headerPts)
rwSize =  computeFontSizePoints(rwPts)

mono = "/Users/stephennixon/type-repos/recursive/src/proofs/drawbot-diagrams-etc/flipbook/fonts/Recursive-mono--w_ital_slnt-2019_08_13.ttf"
sans = "/Users/stephennixon/type-repos/recursive/src/proofs/drawbot-diagrams-etc/flipbook/fonts/Recursive-sans--w_ital_slnt-2019_08_13.ttf"

if prop is 0:
    fontFam = mono
    foreground = 0
    background = 1
    docTitle = "recursive-mono-flipbook_side_1"
else:
    fontFam = sans
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
    
    fill(1,0,1,0.5)
    rect(0, H*0.5, W, thickness)      # middle
    rect(W*0.5, 0, thickness, H)      # center

# ---------------------------------------------------------
# FRONTMATTER ---------------------------------------------


credits = FormattedString()
credits.fill(foreground)
credits.font(fontFam)
credits.fontSize(textSize)
credits.lineHeight(textSize * textLineHeight)
credits.fontVariations(wght=800.01, XPRN=0.001, slnt=0, ital=0)
credits.append("Recursive")

credits.fontVariations(wght=500, XPRN=0.001, slnt=0, ital=0)
credits.append(f""" ({recursiveVersion}, Aug 2019,  3da10a84)
Made by Arrow Type. Type design by Stephen Nixon, with contributions from Katja Schimmel, Lisa Huang, and Rafał Buchner, plus early guidance from faculty and instructors for KABK TypeMedia 2018. Type mastering by Ben Kiel.

Book design by Math Practice.
Typeset with DrawBot by Stephen Nixon.
""")

# URL ----------------------------

url = FormattedString()
url.font(fontFam)
url.fontSize(textSize)
url.lineHeight(textSize * textLineHeight)
url.fontVariations(wght=800.01, XPRN=0.001, slnt=0, ital=0)
url.fontVariations(wght=800.01, XPRN=0.001, slnt=0, ital=0)
url.append("https://recursive.design")

if book:
    newPage(W, H)
    fill(background)
    rect(0,0,W, H)

    # CREDITS ---------------------------------------------

    newPage(W, H)
    fill(background)
    rect(0,0,W, H)

    
    if debug:
        drawMargins()
    
    fill(foreground)

    font(fontFam)
    fontSize(textSize)
    fontVariations(wght=500, XPRN=0.001, slnt=0, ital=0)

    textBox(credits, (marginLeft,marginBottom - textSize * 0.5, W - (marginLeft * 2), H * 0.52 - marginBottom))
    
    textBox(url, (marginLeft,marginBottom - textSize* 0.35 , W - (marginLeft * 2), textSize * textLineHeight))
    



description = FormattedString()
description.fill(foreground)
description.font(fontFam)
description.fontVariations(wght=500, XPRN=0.999, slnt=-14.99, ital=0.99)
description.fontSize(headerSize)
description.lineHeight(headerSize * headerLineHeight)
description.append("A highly customizable variable font for design, code, and UI.")
description.fontVariations(wght=500, XPRN=0.01, slnt=0, ital=0)
description.fontSize(textSize)
description.lineHeight(textSize * textLineHeight)
description.append("""\n
Recursive is a versatile new variable font with five stylistic axes. These variation axes enable customizable control within five stylistic ranges: Proportion, Expression, Weight, Slant, and Italic. Carefully-planned named instances also allow selection within a set of predefined styles.

Recursive offers a range of personality, from a\u00A0sturdy, rational Linear to a friendly, energetic Casual. It comes in two subfamilies:\u00A0Mono & Sans. Within these subfamilies, characters maintain the exact same width across all font styles. This allows for smooth stylistic transitions without affecting line length, enabling new levels of typographic flexibility & interactivity.

Flip the pages to see Recursive in motion!
""")


description.fontVariations(wght=500, XPRN=0.999, slnt=-9, ital=0.999)
description.append("""
Recursive has been sponsored by Google Fonts, through which it will soon be released. Recursive is available under the SIL Open Font License and can be freely used in or adapted for any project.
""")



googleLogo = FormattedString()
googleLogo.font("Google Sans")
googleLogo.fontSize(computeFontSizePoints(16.5))
googleLogo.lineHeight(computeFontSizePoints(16.5) * 0.5)
googleLogo.append("google_logo")



if book:

    
    # DESCRIPTION ---------------------------------------------
    
    newPage(W, H)
    fill(background)
    rect(0,0,W, H)
    
    if debug:
        drawMargins()

    overflow = textBox(description, (marginLeft,marginBottom - textSize * 0.85 + (H * 0.05), W - (marginLeft * 2)- marginLeft * 0.4, H * 0.75 - marginBottom))
    
    newPage(W, H)
    fill(background)
    rect(0,0,W, H)

    textBox(overflow, (marginLeft,marginBottom - textSize *0.125, W - (marginLeft * 2) - marginLeft * 0.4, H * 0.8 - marginBottom))
    

    textBox(googleLogo,(marginLeft,marginBottom + textSize * 0.85, W - (marginLeft * 2), headerSize))

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
    
    size = padding * 0.375

    fill(foreground)
    
    fontSize(rwSize)
    overflow = textBox("rw", (0, padding - rwSize*0.21, W, rwSize*1.25), align="center")

    # ----------------------------------------------------------------------
    # BAR CHARTS / SLIDERS FOR AXES ----------------------------------------
    
    x = str('{:4.2f}'.format(xprnVals[0]))
    w = str('{:3.2f}'.format(wghtVals[0]))    
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
    infoSpacing = textSize * 1.5 # textLineHeight 
    infoHeight = H * 0.55 + textSize

    if prop == 0:
        
        # maxLength = 40

        maxLength = (W- (marginLeft*2)) / (textSize * 0.6) - 16

        def showAxisVals(label, value, valueString, infoHeight):

            # fontVariations(wght=wghtVals[0], XPRN=xprnVals[0], slnt=slntVals, ital=italVals)
            
            with savedState():
                fill(foreground)
                # fontVariations(wght=500, XPRN=xprnVals[0], slnt=0, ital=0)
                # textBox(f"{label} {valueString.rjust(7)}  {'{}'.rjust(floor(maxLength*value), ' ')}", (marginLeft, infoHeight, (W- (marginLeft*2)), textSize*1.625))

                txt = FormattedString()
                txt.font(mono)
                txt.fontSize(textSize)

                txt.fontVariations(wght=500, XPRN=xprnVals[0], slnt=0, ital=0)
                txt.append(f"{label} {valueString.rjust(7)}")
                txt.append("  ")

                txt.fontVariations(wght=300, XPRN=0, slnt=0, ital=0)
                txt.append("".rjust(floor(maxLength*value), "·"))

                txt.fontVariations(wght=800, XPRN=xprnVals[0], slnt=0, ital=0)
                txt.append("*")

                textBox(txt, (marginLeft, infoHeight, (W- (marginLeft*2)), textSize*1.625))
                

            
        
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

        
    # SANS, prop = 1
    else: 
        trackSize = padding*0.05
        ovalSize = padding*0.2 # 0.1875

        def showAxisVals(label, value, valueString, infoHeight):
            # fill(foreground,foreground,foreground,0.25)
            # rect(padding, infoHeight, (W- (padding*2)), trackSize)
            with savedState():

                font(mono)
                fontVariations(wght=500, XPRN=xprnVals[0], slnt=0, ital=0)

                fill(foreground)
                # oval(((W - (padding*2)) * value) -(ovalSize/2) + padding,infoHeight-(ovalSize/2)+(trackSize/2), ovalSize, ovalSize)
                # oval(((W - (padding*2) - ovalSize) * value) + padding,infoHeight-(ovalSize/2)+(trackSize/2), ovalSize, ovalSize)

                labelWidth = W * 0.125
                # x = (W - (padding*2)) * value + padding
                x = ((W - (padding*2) - labelWidth) * value) + padding
                y = infoHeight
                w = labelWidth
                h = textSize*1.625

                textBox(label, (x,y,w,h))

                font(sans)
                    
                textBox(valueString,((x,y,w,h)), align="right")
            
        # infoSpacing = H * 0.056
        # infoHeight = H * 0.5 + textSize
        showAxisVals("i", italVal, i, infoHeight)

        infoHeight += infoSpacing
        showAxisVals("s", -slntVal, s, infoHeight)

        infoHeight += infoSpacing
        showAxisVals("w", wghtVal, w, infoHeight)

        infoHeight += infoSpacing
        showAxisVals("x", xprnVal, x, infoHeight)

        propVal = prop
        infoHeight += infoSpacing
        showAxisVals("p", propVal, p, infoHeight)


    # ----------------------------------------------------------------------
    # PAGE NUMBER ----------------------------------------------------------
    
    # with savedState():
    #     fontVariations(wght=400, XPRN=xprnVals[0], slnt=0, ital=0)

    footerHeight = marginBottom*0.75

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

# -----------------------------------------------------------------------------
# END PAGES -------------------------------------------------------------------

for page in range(endPages):
    newPage(W, H)
    fill(background)
    rect(0,0,W, H)


endDrawing()

if export:
    now = datetime.datetime.now().strftime("%Y_%m_%d-%H") # -%H_%M_%S

    path = f"/Users/stephennixon/type-repos/recursive/src/proofs/drawbot-diagrams-etc/flipbook/exports/{docTitle}-{frames + 8}_pages-{now}.{format}"

    print("saved to ", path)

    saveImage(path)

    if autoOpen:
        import os
        # os.system(f"open --background -a Preview {path}")
        os.system(f"open -a Preview {path}")


