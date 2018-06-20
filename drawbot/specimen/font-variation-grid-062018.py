H= 700

W = 1000

size(W, H)
# pick a font
font("RecursiveMonoVar-StrictLight")

# list all axis from the current font
# for axis, data in listFontVariations().items():
#     print((axis, data))

maxWeight = 1100
minWeight = 220

maxExpression = 1.0
minExpression = 0.01

steps = 8
padding = 20

string = "Rr"

stepWeight =     (maxWeight - minWeight)/steps
stepExpression = (maxExpression - minExpression)/steps

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

fontSize(W/steps/1.5)

for i in range(0,steps):
    # set x position
    x = padding + i * (W-padding) / steps
    # set XPRN
    currentExpression = minExpression + stepExpression * i
    
    red = interpFunc(0.325,0.823, steps, i)
    green = interpFunc(0.231,0.180, steps, i)
    blue = interpFunc(0.90,0.92, steps, i)
    # blue    ### magenta #
    #####################
    # green   ### yellow  #

    # or

    # (0,0,1) ### (1,0,1) #
    #######################
    # (0,1,0) ### (1,1,0) #
    
    # if the first or last column
    if i == 0 or i == steps -1:
        fill(red, green, blue, 1)
    # if in the middle columns
    else:
        fill(red, green, blue, 0.65)
    
    for j in range(0,steps):
        
        # if the first or last column
        if i == 0 or i == steps -1:
            fill(red, green, blue, 1)
        # if in the middle columns
        else:
            fill(red, green, blue, 0.65)
        
            
        
        currentWeight = minWeight + stepWeight * j
        
        y = padding + j * (H-padding) / steps
        
        fontVariations(XPRN=currentExpression, wght=currentWeight)
        text(string, (x, y))
    
saveImage("/Users/stephennixon/type/01-casual_mono-project/drawbot/specimen/exports/recursive-var-grid--wght_xprn.pdf")
    