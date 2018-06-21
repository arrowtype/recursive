H= 525

W = 1000

size(W, H)
# pick a font
font("RecursiveMonoVar-StrictLight")

# list all axis from the current font
for axis, data in listFontVariations().items():
    print((axis, data))

maxWeight = 1100
minWeight = 220

maxExpression = 1.0
minExpression = 0.01

maxSlant = 14
minSlant = 0

stepsX = 20 #8
stepsY = 8 # 6
padding = 20

string = "R" # Rr

# stepWeight =     (maxWeight - minWeight)/stepsX
# stepExpression = (maxExpression - minExpression)/steps

def interpFunc(a, b, numSteps, currentStep):
    distance = b-a
    stepSize = distance/numSteps 
    progress = currentStep/numSteps
    value = a + distance*progress
    return(value)
    
def normalRGB(r, g, b):
    r1, g1, b1 = r / 255, g / 255, b / 255
    return(r1, g1, b1)
    
print(normalRGB(83, 59, 230)) # blue
print(normalRGB(210, 46, 237)) # magenta
print(normalRGB(251, 208, 0)) # yellow
print(normalRGB(16, 205, 103)) # green

fontSize(W/stepsX/.75) # 1.5

for i in range(0,stepsX):
    # set x position
    x = padding + i * (W-padding) / stepsX
    # set XPRN
    # currentExpression = minExpression + stepExpression * i
    
    currentExpression = interpFunc(minExpression, maxExpression, stepsX, i)
    
    
    # this is unnecessarily cumbersome. make a tuple interpolatetion func
    red = interpFunc(0.6,0.1, stepsX, i)
    green = interpFunc(0.6,0.1, stepsX, i)
    blue = interpFunc(0.6,0.1, stepsX, i)
    # blue    ### magenta #
    #####################
    # green   ### yellow  #
    
    # if the first or last column
    if i == 0 or i == stepsX-1:
        strokeWidth(0)
        fill(0, 0, 0, 1)
    # if in the middle columns
    else:
        strokeWidth(.5)
        stroke(0, 0, 0, 1)
        fill(red, green, blue, 0.05)
        
    currentSlant = interpFunc(minSlant, maxSlant, stepsX, i)
    
    for j in range(0,stepsY):
        
        currentWeight = interpFunc(minWeight, maxWeight, stepsY, j)
        # currentSlant = interpFunc(minSlant, maxSlant, stepsY, j)

        # TODO: make slant in bottom-right corner and top-left corners?
        # currentSlant = maxSlant-currentSlant
        
        y = padding + j * (H-padding) / stepsY
        
        # fontVariations(XPRN=currentExpression, wght=currentWeight, slnt=currentSlant)
        fontVariations(XPRN=currentExpression, wght=currentWeight)
        text(string, (x, y))
    
saveImage("/Users/stephennixon/type/01-casual_mono-project/drawbot/specimen/exports/recursive-var-grid--wght_xprn-lines-BW.pdf")
    