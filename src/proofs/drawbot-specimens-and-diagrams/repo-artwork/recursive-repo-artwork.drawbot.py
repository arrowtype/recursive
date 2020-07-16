from drawBot import * # requires drawbot to be installed as module
import datetime
from fontTools.misc.bezierTools import splitCubicAtT
from fontTools.ttLib import TTFont
import os
import shutil

newDrawing() # for drawbot module

export = True
autoOpen = True
exportFormat = "png" # pdf, gif, mp4, jpeg, png, or bmp
# W,H = 1280, 640 # pixels
# W,H = 1800, 900 # pixels
W,H = 1280, 640 # pixels - opengraph image
# W,H = 1600, 640 # pixels - github repo artwork

mainColor = (0, 0.25, 1)

now = datetime.datetime.now().strftime("%Y_%m_%d-%H_%M")
timestamp = datetime.datetime.now().strftime("%Y-%m-%d, %H:%M")
parentDir = "/Users/stephennixon/type-repos/recursive/src/proofs/drawbot-specimens-and-diagrams/repo-artwork"
docTitle="recursive-repo-art"

fontFam = "/Users/stephennixon/type-repos/recursive/src/proofs/drawbot-specimens-and-diagrams/repo-artwork/font/recursive-MONO_CASL_wght_slnt_ital--2019_10_31-23_25.ttf"

backgroundLetter = "R" # ã S &

# ------------------------------------------------
# draw background --------------------------------

def hex2rgb(hex):
    h = hex.lstrip('#')
    RGB = tuple(int(h[i:i+2], 16) for i in (0, 2 ,4))
    r1, g1, b1 = RGB[0] / 255, RGB[1] / 255, RGB[2] / 255
    return(r1, g1, b1)

newPage(W,H)


# fill(*hex2rgb("#0050FF"))
fill(*mainColor)
# fill(0)
rect(0,0,W,H)

# Draw Rs
font(fontFam)
fill(1,1,1,0.015)
# fill(1,1,1,0)

strokeWidth(W * .0005) # for larger images: 0.00015


sizeOfFont = H*1.2
fontSize(sizeOfFont)


def interpolate(a, b, t):
    distance = b-a
    return(a + distance * t)

numOfRs = 80

minWght = 300.01
maxWght = 999.99

minCasl = 0.01
maxCasl = 0.99

def getCurrentWeight(t):
    return interpolate(minWght, maxWght, t)

def getCurrentOpacity(t, maxOpacity):
    fill = interpolate(0.0125, 0.05, t)

    maxStrokeOpacity = maxOpacity
    if t <= 0.5:
        stroke = interpolate(maxStrokeOpacity, -maxStrokeOpacity*1.25, t)
    else:
        stroke = interpolate(-maxStrokeOpacity*1.25, maxStrokeOpacity, t)

    return fill, stroke

for i in range(numOfRs):
    t = i/numOfRs
    
    fontVariations(wght=getCurrentWeight(t), CASL=interpolate(maxCasl, minCasl, t))

    # fill(1, 1, 1, getCurrentOpacity(t)[0])
    # stroke(1,1, 1, getCurrentOpacity(t)[1])
    stroke(getCurrentOpacity(t,1)[1], getCurrentOpacity(t,1)[1], 1, getCurrentOpacity(t,0.75)[1])
    # stroke(getCurrentOpacity(t,0)[1], getCurrentOpacity(t,0)[1], 0, getCurrentOpacity(t,0.75)[1])

    text(backgroundLetter, (((W - sizeOfFont*0.6)/numOfRs)*i - (sizeOfFont*0.02), H*0.075))


# ------------------------------------------------
# add text ---------------------------------------

line1 = "recursive"
line2 = "sans*mono"

fontSizing = (W/len(line1)*1.666666667) * 0.95

fontSize(fontSizing)

miterLimit(3)

def writeText(fillColor, strokeThickness):
    fill(fillColor)
    # stroke(*hex2rgb("#0050FF"))
    # stroke(*hex2rgb("#0050FF"))
    stroke(*mainColor)
    strokeWidth(strokeThickness)
    fontVariations(wght=850, CASL=0.999, slnt=-14.99, MONO=0.999)
    text(line1, (W/2, H/2+fontSizing*0.05), align="center")

    fontVariations(wght=350.001, CASL=0.001, slnt=0, MONO=0.999)
    text(line2, (W/2, H/2-fontSizing*0.7), align="center")

# write with outline
writeText(1, W*0.006)

# write again to overlap without outline
with savedState():
    translate(0, 0)
    writeText(1, 0)

strokeWidth(0)

# ------------------------------------------------
# add logo ---------------------------------------

fill(1)

if W >= 1400:
    logoText = "@ArrowType"
    # logoText = "@"

    fontSizing = (W/len(logoText)*1.666666667) * 0.1 #*1.25
    # fontSizing = (W/10*1.666666667) * 0.1
    fontSize(fontSizing)
    fontVariations(wght=800.999, CASL=0.999, slnt=0, MONO=0.999)
    # fontVariations(wght=300.999, CASL=0.001, MONO=0.001)

    # fill(*mainColor)
    text(logoText, (W*0.5, H*0.1), align='center')
    
else:
    fill(1,1,1,0.75)
    logoText = "@"
    fontSizing = (W/len(logoText)*1.666666667) * 0.05
    fontSize(fontSizing)
    fontVariations(wght=800, CASL=0.999, slnt=0, MONO=0.001)

    # stroke(1)
    # rect(W*0.05, H*0.1, W*0.9, H*0.1)

    # paddingUnit = W*0.035
    paddingUnit = -W*0.005

    textBox(logoText, (paddingUnit, paddingUnit*2.5, W-(paddingUnit*2), fontSizing*1.25), align='right')

# ------------------------------------------------
# save result ------------------------------------

endDrawing()

if export and exportFormat is not "bmp":

    if not os.path.exists(f"{parentDir}/exports"):
        os.makedirs(f"{parentDir}/exports")

    path = f"{parentDir}/exports/{docTitle}-{now}.{exportFormat}"

    print("saved to ", path)

    saveImage(path)

    if autoOpen:
        import os
        # os.system(f"open --background -a Preview {path}")
        os.system(f"open -a Preview {path}")


