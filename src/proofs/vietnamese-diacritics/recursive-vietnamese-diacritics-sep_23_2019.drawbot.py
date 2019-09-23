from drawBot import * # requires drawbot to be installed as module
import datetime
from fontTools.misc.bezierTools import splitCubicAtT
newDrawing() # for drawbot module


export = True
autoOpen = True
exportFormat = "pdf" # pdf, gif, mp4, or bmp

now = datetime.datetime.now().strftime("%Y_%m_%d-%H_%M")
parentDir = "/Users/stephennixon/type-repos/recursive/src/proofs/vietnamese-diacritics"
docTitle="recursive-vietnamese-diacritics"

font("/Users/stephennixon/type-repos/recursive/src/proofs/vietnamese-diacritics/recursive-mono--xprn_wght_slnt_ital--2019_09_23.ttf")

testString="Trương, trường, thương, tương, trước, sương, chương, phương hướng, xương sường, tưởng tượng"

variations = [
    {"wght": 300.01, "XPRN":0.01},
    {"wght": 800.01, "XPRN":0.01},
    {"wght": 899.99, "XPRN":0.01},
    {"wght": 300.01, "XPRN":0.999},
    {"wght": 800.01, "XPRN":0.999},
    {"wght": 899.99, "XPRN":0.999}
    ]

for i,var in enumerate(variations):
    fontVariations(**var)
    fontSize(28)
    textBox(testString, (0,0-80*i,1000,1000))

# ------------------------------------------------
# save result ------------------------------------

endDrawing()

if export and exportFormat is not "bmp":

    path = f"{parentDir}/exports/{docTitle}-{now}.{exportFormat}"

    print("saved to ", path)

    saveImage(path)

    if autoOpen:
        import os
        # os.system(f"open --background -a Preview {path}")
        os.system(f"open -a Preview {path}")