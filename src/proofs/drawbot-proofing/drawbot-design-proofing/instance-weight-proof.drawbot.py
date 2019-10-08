from drawBot import * # requires drawbot to be installed as module
import datetime
import sys

newDrawing() # for drawbot module

# fontFam = sys.argv[1] # feed as argument

save = False
autoOpen = True
fileFormat = "pdf"

size('LetterLandscape')

docTitle = "recursive-weight_test"

testString = "Recursion in computer science is a method of solving a problem where the solution depends on solutions to smaller instances of the same problem (as opposed to iteration)¹. The approach can be applied to many types of problems, and recursion is one of the central ideas of computer science²."

# font(fontFam)

font('/Users/stephennixon/type-repos/recursive/font-betas/recursive-prop_xprn_weight_slnt_ital--2019_08_26.ttf')


W, H = width(), height()

minWght = 300.001

for i in range(0, 7):

    currentWght = minWght + i * 100

    fontVariations(wght=currentWght, XPRN=1, slnt=-14.999, ital=1)
    
    textHeight = 50
    blockHeight= 150
    
    padding = 80

    textBox(str(floor(currentWght)), (40,blockHeight + textHeight*i,W-padding*2,textHeight))
    
    textBox(testString, (padding,blockHeight + textHeight*i,W/2-padding,textHeight))






endDrawing()

if save:
    now = datetime.datetime.now().strftime("%Y_%m_%d-%H_%M") # -%H_%M_%S

    path = f"/Users/stephennixon/type-repos/recursive/src/proofs/drawbot-design-proofing/exports/{docTitle}-{now}.{fileFormat}"

    print("saved to ", path)

    saveImage(path)

    if autoOpen:
        import os
        # os.system(f"open --background -a Preview {path}")
        os.system(f"open -a Preview {path}")