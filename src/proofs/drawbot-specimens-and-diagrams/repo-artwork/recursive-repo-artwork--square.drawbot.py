from drawBot import * # requires drawbot to be installed as module
import datetime
from fontTools.misc.bezierTools import splitCubicAtT
from fontTools.ttLib import TTFont
import os
import shutil

newDrawing() # for drawbot module

export = True
autoOpen = True
exportFormat = "jpg" # pdf, gif, mp4, jpeg, png, or bmp
# W,H = 1280, 1280 # pixels
W,H = 1500, 1500 # pixels

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
fill(0)
rect(0,0,W,H)

# Draw Rs
font(fontFam)
fill(1,1,1,0)

strokeWidth(W * .0025)


sizeOfFont = H*1.2
fontSize(sizeOfFont)


def interpolate(a, b, t):
    distance = b-a
    return(a + distance * t)

numOfRs = 40 #80

minWght = 300.01
maxWght = 999.99

minCasl = 0.99 # 0.01
maxCasl = 0.99

def getCurrentWeight(t):
    return interpolate(minWght, maxWght, t)

def getCurrentOpacity(t):
    fill = interpolate(0.0125, 0.05, t)

    maxStrokeOpacity = 0.6
    if t <= 0.5:
        stroke = interpolate(maxStrokeOpacity, -maxStrokeOpacity, t)
    else:
        stroke = interpolate(-maxStrokeOpacity, maxStrokeOpacity, t)

    return fill, stroke

for i in range(numOfRs):
    t = i/numOfRs
    
    fontVariations(wght=getCurrentWeight(t), CASL=interpolate(minCasl, maxCasl, t))

    # fill(1, 1, 1, getCurrentOpacity(t)[0])
    stroke(1,1, 1, getCurrentOpacity(t)[1])
    # stroke(getCurrentOpacity(t)[1], getCurrentOpacity(t)[1], 1, getCurrentOpacity(t)[1])

    text(backgroundLetter, (((W - sizeOfFont*0.6)/numOfRs)*i - (sizeOfFont*0.0125), H*0.075))


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


