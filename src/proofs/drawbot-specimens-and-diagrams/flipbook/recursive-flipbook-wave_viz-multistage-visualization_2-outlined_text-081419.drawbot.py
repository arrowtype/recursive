from drawBot import * # requires drawbot to be installed as module
import datetime
from fontTools.misc.bezierTools import splitCubicAtT
newDrawing() # for drawbot module

# ---------------------------------------------------------
# CONFIGURATION -------------------------------------------

prop = 1 # 0 for mono, 1 for sans

export = True
autoOpen = True
book = True
debug = False # overlays curve visualizations

frames = 0 # 96 for full animation
frameRate = 1/30 # only applicable to mp4
exportFormat = "pdf" # pdf, gif, mp4, or bmp

DPI = 72 # dots per inch – must be 72 to print at dimensions set in inches

blankStart = False

if book:
    # endPages = 4 #4
    endPages = 0
else:
    endPages = 0

bookSize = 3.5 # inches
marginSize = 0.25 # inches

# marginSides = 0.3
# marginBottom = 0.2

## top, right, bottom, left
# margins = (0.75, 0.3, 0.2, 0.3)
margins = (0.75, 0.25, 0.2, 0.3)

if prop is 0:
    indent = "    "
else:
    indent = "\n"

textPts = 7 # 6.75
textLineHeight = 1.5
headerPts = 14
headerLineHeight = 1.125
rwPts =  170 # 152

recursiveVersion="Beta v1.014"
now = datetime.datetime.now().strftime("%Y_%m_%d-%H_%M") # -%H_%M_%S
parentDir = "/Users/stephennixon/type-repos/recursive/src/proofs/drawbot-diagrams-etc/flipbook"

# ---------------------------------------------------------

pageNum = 0

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

def newPagePlz(pageNum):
    pageNum += 1
    newPage(W, H)
    fill(background)
    rect(0,0,W, H)

    return pageNum

# this will draw cyan guides to help align content
def drawMargins():
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


def ifBitmapSaveBitmap(pageNum):
    # exportFolder = f"{parentDir}/exports/{docTitle}-bitmaps-{now}"
    exportFolder = f"/Users/stephennixon/Dropbox/KABK_netherlands/type_media/000-casual-mono/000-googlefonts-minisite_and_specimens-support/flipbook/{docTitle}-bitmaps-{now}"
    import os
    os.system(f"mkdir -p {exportFolder}")

    if save and exportFormat == "bmp":

        page = str(pageNum).rjust(3, "0")

        path = f"{exportFolder}/{page}-{docTitle}.bmp"
        saveImage(path, imageResolution=2400)
        print("saved bitmap: ", path)

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
    if blankStart:
        pageNum = newPagePlz(pageNum)
        ifBitmapSaveBitmap(pageNum)

    # CREDITS ---------------------------------------------


    pageNum = newPagePlz(pageNum)

    
    if debug:
        drawMargins()
    
    fill(foreground)

    font(fontFam)
    fontSize(textSize)
    fontVariations(wght=500, XPRN=0.001, slnt=0, ital=0)

    textPath = BezierPath()
    
    textPath.textBox(credits, (marginLeft,marginBottom - textSize * 0.5, W - (marginLeft * 2), H * 0.52 - marginBottom))
    
    textPath.textBox(url, (marginLeft,marginBottom - textSize* 0.35 , W - (marginLeft * 2), textSize * textLineHeight))

    drawPath(textPath)
    
    ifBitmapSaveBitmap(pageNum)



description = FormattedString()
description.fill(foreground)
description.font(fontFam)
description.fontVariations(wght=500, XPRN=0.999, slnt=-14.99, ital=0.99)
description.fontSize(headerSize)
description.lineHeight(headerSize * headerLineHeight)
description.append("A highly customizable variable font for code and design")
description.fontVariations(wght=500, XPRN=0.01, slnt=0, ital=0)
description.fontSize(textSize)
description.lineHeight(textSize * textLineHeight)
description.append(f"""\n
Recursive is a versatile variable font with five stylistic axes (Weight, Slant, Italic, Proportion, and Expression) so you can customize your typography. It also comes with a curated selection of predefined styles to get you up and running. 
{indent}It offers a novel range of personality along the Expression axis, from a sturdy and rational """)

# add italic words
description.fontVariations(wght=500, XPRN=0.01, slnt=-9, ital=0.99)
description.append("Linear ")
description.fontVariations(wght=500, XPRN=0.01, slnt=0, ital=0)
description.append("to a friendly and energetic ")
description.fontVariations(wght=500, XPRN=0.01, slnt=-9, ital=0.99)
description.append("Casual. ")

# back to normal
description.fontVariations(wght=500, XPRN=0.01, slnt=0, ital=0)
description.append(f"""\
With the Proportion axis, you can adjust the monospace design into a natural-width sans serif that is intended to be more readable in text and interface elements.
{indent}Along the Proportion axis, every glyph is carefully designed to maintain the exact same width through changes in every other axis. This allows smooth stylistic transitions without affecting line length – enabling new levels of typographic flexibility & interactivity.
""")

# \u00A0 = non-breaking space, to help control text wrap


description.fontVariations(wght=500, XPRN=0.999, slnt=-9, ital=0.999)
description.append(f"""
Google Fonts teamed up with Arrow Type to make Recursive available to be used and customized freely in any of your projects. Check out the source files and learn more at github.com/arrowtype/recursive
""")



googleLogo = FormattedString()
googleLogo.font("Google Sans")
googleLogo.fontSize(computeFontSizePoints(16.5))
googleLogo.lineHeight(computeFontSizePoints(16.5) * 0.5)
googleLogo.append("google_logo")



if book:

    
    # DESCRIPTION ---------------------------------------------
    
    pageNum = newPagePlz(pageNum)
    # pageNum += 1

    if debug:
        drawMargins()

    textPath = BezierPath()

    fill(foreground)

    overflow = textPath.textBox(
        description,
        (
            marginLeft,
            marginBottom - textSize * 0.85 + (H * 0.05),
            W - (marginLeft + marginRight),
            H * 0.75 - marginBottom)
        )
    # textPath.textBox(description, (marginLeft,marginBottom - textSize * 0.85 + (H * 0.05), W - (marginLeft * 2)- marginLeft * 0.4, H * 0.75 - marginBottom))

    drawPath(textPath)

    ifBitmapSaveBitmap(pageNum)

    # second page ---------------------------------------------
    
    pageNum = newPagePlz(pageNum)
    # pageNum += 1

    textPath = BezierPath()
    
    # continued from overflow above
    textPath.textBox(
        overflow,
        (
        marginLeft,
        marginBottom - textSize *0.125,
        W - (marginLeft + marginRight),
        H * 0.8 - marginBottom)
        )
    
    fill(foreground)
    drawPath(textPath)
    
    textPath = BezierPath()

    fill(foreground)
    
    textPath.textBox(googleLogo,(marginLeft,marginBottom + textSize * 0.85, W - (marginLeft * 2), headerSize))
    
    drawPath(textPath)

    if debug:
        drawMargins()
    
    ifBitmapSaveBitmap(pageNum)


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

    pageNum = newPagePlz(pageNum)

    frameDuration(frameRate)
    
    if book:
        t = 1 - (frame / (frames - 1)) # reverse
    else:
        t = frame / (frames - 1) # forward    

    xprnVals = getCurveValue(t, 0.5, 0.001, 0.999)
    wghtVals = getWeightValue(t, 0.7, 300.001, 899.999)
    slntVals = getSlantValue(t, 0.001, -14.999)
    italVals = getItalValue(t)
    
    size = padding * 0.375

    rw = FormattedString()

    rw.fontSize(rwSize)
    rw.fill(foreground)
    rw.font(fontFam)
    rw.fontVariations(wght=wghtVals[0], XPRN=xprnVals[0], slnt=slntVals, ital=italVals)
    rw.align("center")

    rw.append("rw")

    textPath = BezierPath()

    # continued from overflow above
    textPath.textBox(rw, (0, padding - rwSize*0.21, W, rwSize*1.25))
    
    fill(foreground) # fill must come before drawPath, not in FormattedString object
    drawPath(textPath)


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

                textPath = BezierPath()

                textPath.textBox(txt, (marginLeft, infoHeight, (W- (marginLeft*2)), textSize*1.625))

                fill(foreground)
                drawPath(textPath)
                

            
        
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
            with savedState():

                # axis label ---------------

                txt = FormattedString()
                txt.font(mono)
                txt.fontVariations(wght=500, XPRN=xprnVals[0], slnt=0, ital=0)
                txt.fontSize(textSize)
                txt.append(label)

                
                textPath = BezierPath()

                labelWidth = W * 0.125
                x = ((W - (padding*2) - labelWidth) * value) + padding
                y = infoHeight
                w = labelWidth
                h = textSize*1.625
                textPath.textBox(txt, (x,y,w,h))

                fill(foreground)
                drawPath(textPath)

                # axis value ---------------

                txt = FormattedString()
                txt.font(sans)                                                     # MUST be here
                txt.fontSize(textSize)                                             # MUST be here
                txt.fontVariations(wght=500, XPRN=xprnVals[0], slnt=0, ital=0)     # styling
                txt.align("right")                                                 # styling
                txt.append(valueString)

                valueTextPath = BezierPath()
                fill(foreground)                                                   # MUST be here between BezierPath() setup and drawPath(), *not* in formatted string,
                valueTextPath.textBox(txt,((x,y,w,h)))
                drawPath(valueTextPath)
            
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

    txt = FormattedString()
    txt.font(sans)                                                     # MUST be here
    txt.fontSize(textSize)                                             # MUST be here
    txt.fontVariations(wght=500, XPRN=xprnVals[0], slnt=0, ital=0)     # styling
    txt.align("left")                                                 # styling

    if prop == 0:
        # textBox("Recursive Mono", (marginLeft, footerHeight, (W- (marginLeft*2)), textSize*1.5), align="left")
        txt.append("Recursive Mono")
    else:
        # textBox("Recursive Sans", (marginLeft, footerHeight, (W- (marginLeft*2)), textSize*1.5), align="left")
        txt.append("Recursive Sans")

    path = BezierPath()
    fill(foreground)                                                   # MUST be here between BezierPath() setup and drawPath(), *not* in formatted string,
    path.textBox(txt,(marginLeft, footerHeight, (W- (marginLeft*2)), textSize*1.5))
    drawPath(path)

    txt = FormattedString()
    txt.font(sans)                                                     # MUST be here
    txt.fontSize(textSize)                                             # MUST be here
    txt.fontVariations(wght=500, XPRN=xprnVals[0], slnt=0, ital=0)     # styling
    txt.align("left")  
    txt.append("Arrow Type")

    path = BezierPath()
    fill(foreground)                                                   # MUST be here between BezierPath() setup and drawPath(), *not* in formatted string,
    path.textBox(txt,(W/2, footerHeight, (W- (padding*2)), textSize*1.5))
    drawPath(path)


    # page number
    txt = FormattedString()
    txt.font(sans)                                                     # MUST be here
    txt.fontSize(textSize)                                             # MUST be here
    txt.fontVariations(wght=500, XPRN=xprnVals[0], slnt=0, ital=0)     # styling
    txt.align("right")  

    if book:
        txt.append(str(frames-(frame))) # current page number
    else:
        txt.append(str(frame + 1)) # current page number

    path = BezierPath()
    fill(foreground)                                                   # MUST be here between BezierPath() setup and drawPath(), *not* in formatted string,
    path.textBox(txt,(marginLeft, footerHeight, (W- (marginLeft*2)), textSize*1.5))
    drawPath(path)


    ifBitmapSaveBitmap(pageNum)
    
    
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
    pageNum = newPagePlz(pageNum)

    ifBitmapSaveBitmap(pageNum)

endDrawing()

if save and exportFormat is not "bmp":

    path = f"/Users/stephennixon/type-repos/recursive/src/proofs/drawbot-diagrams-etc/flipbook/exports/{docTitle}-{frames + 8}_pages-{now}.{exportFormat}"

    print("saved to ", path)

    saveImage(path)

    if autoOpen:
        import os
        # os.system(f"open --background -a Preview {path}")
        os.system(f"open -a Preview {path}")


