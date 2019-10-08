
W, H = 1920, 1080
size(W, H)
# rect(0,0,W,H)
# pick a font
font("RecursiveMonoVar-StrictLight")

# list all axis from the current font
for axis, data in listFontVariations().items():
    print((axis, data))

maxWeight = 1100
minWeight = 220

maxExpression = 1
minExpression = 0.01

maxSlant = 14
minSlant = 0


stepsX = 20
stepsY = 8
padding = 20

string = "S"

gridDictionary = {}

def interpFunc(a, b, numSteps, currentStep):
    distance = b-a
    stepSize = distance/numSteps 
    progress = currentStep/numSteps
    value = a + distance*progress
    return(value)
    
def normalRGB(r, g, b):
    r1, g1, b1 = r / 255, g / 255, b / 255
    return(r1, g1, b1)
    
# print(normalRGB(83, 59, 230)) # blue
# print(normalRGB(210, 46, 237)) # magenta
# print(normalRGB(251, 208, 0)) # yellow
# print(normalRGB(16, 205, 103)) # green

fontSize(W/stepsX/.7) # 1.5

for i in range(0,stepsX):
    # set x position
    x = padding + i * (W-padding) / stepsX
    # set XPRN
    # currentExpression = minExpression + stepExpression * i
    
    currentExpression = interpFunc(minExpression, maxExpression, stepsX-1, i)
    
    
    # this is unnecessarily cumbersome. make a tuple interpolatetion func
    red = interpFunc(0.325,0.823, stepsX, i)
    green = interpFunc(0.231,0.180, stepsX, i)
    blue = interpFunc(0.90,0.92, stepsX, i)
    # blue    ### magenta #
    #####################
    # green   ### yellow  #
    
    # if the first or last column
    if i == 0 or i == stepsX-1:
        strokeWidth(0)
        fill(red, green, blue, 1)
    # if in the middle columns
    else:
        strokeWidth(1)
        stroke(red, green, blue, 0.65)
        fill(red, green, blue, 0.05)
        
    currentSlant = interpFunc(minSlant, maxSlant, stepsX, i)

    
    
    for j in range(0,stepsY):
        
        currentWeight = interpFunc(minWeight, maxWeight, stepsY-1, j)
        # currentSlant = interpFunc(minSlant, maxSlant, stepsY, j)

        # TODO: make slant in bottom-right corner and top-left corners?
        # currentSlant = maxSlant-currentSlant
        
        y = padding + j * (H-padding) / stepsY
        
        # fontVariations(XPRN=currentExpression, wght=currentWeight, slnt=currentSlant)
        fontVariations(XPRN=currentExpression, wght=currentWeight)
        text(string, (x, y))
        
        # if i == 0 or i == stepsX -1:
        #     gridDictionary[i, j] = x, y, currentExpression, currentWeight
            
        gridDictionary[i, j] = x, y, currentExpression, currentWeight, (red, green, blue)
        
# print(gridDictionary)

# gridDictionary = {
#     col0 = {
#         x: 100,
#         y: 300,
#         XPRN: 0.4,
#         wght: 340
#         }
#     }
################################
### part 2: diagonals
################################

# get value of grid for arbitrary y1 and y2 (e.g. 2 up on left, 5 up on right)
# this probably could use a dictionary set up by the previous code
# col: row: (x, y, wght, XPRN)

interSteps = 80 #140
# x1, y1 = 100, 100
# x2, y2 = 896, 718

def drawInterPath(x1, y1, x2, y2, wght1, wght2, xprn1, xprn2,rgb1,rgb2):
    
    print(rgb1,rgb2)

    for interLetter in range(0, interSteps+1):
        interX = interpFunc(x1, x2, interSteps, interLetter)
        interY = interpFunc(y1, y2, interSteps, interLetter)
        
        interExpression = interpFunc(xprn1, xprn2, interSteps, interLetter)
        interWeight = interpFunc(wght1, wght2, interSteps, interLetter)
        
        fontVariations(XPRN=interExpression, wght=interWeight)
        
        interR = interpFunc(rgb1[0],rgb2[0],interSteps, interLetter)
        interG = interpFunc(rgb1[1],rgb2[1],interSteps, interLetter)
        interB = interpFunc(rgb1[2],rgb2[2],interSteps, interLetter)
        
        print(interR,interG, interB,)
        
        strokeOpacity = interpFunc(0.05, 1, interSteps, interLetter)
        # print(strokeOpacity)
        r,g,b = normalRGB(240,164,63)
        print(interLetter, interSteps)
        if interLetter != interSteps:
            strokeWidth(1)
            # stroke(1,1,1,strokeOpacity)
            
            r,g,b = normalRGB(240,164,63)
            stroke(r,g,b,strokeOpacity)
            shadow((0,0),0,(1,1, 1,0))
        if interLetter == interSteps:
            strokeWidth(0)
            # shadow((0,0),5,(r,g,b,1))
            strokeWidth(1)
            stroke(1)
        # shadow((0,0),2,(0,0, 0,strokeOpacity))

        # if interLetter % 5 == 0:
        #    fill(1,1,1,1) 
        # else:
        #     fill(1,1,1,strokeOpacity)
        # fill(1,1,1,strokeOpacity)
        fill(interR,interG,interB, strokeOpacity)
        text(string, (interX, interY))
    

def drawDiagonals(col1,row1, col2,row2):
    posX1 = gridDictionary[col1,row1][0]
    posY1 = gridDictionary[col1,row1][1]
    
    posX2 = gridDictionary[col2,row2][0]
    posY2 = gridDictionary[col2,row2][1]
    
    xprn1 = gridDictionary[col1,row1][2]
    wght1 = gridDictionary[col1,row1][3]
    
    xprn2 = gridDictionary[col2,row2][2]
    wght2 = gridDictionary[col2,row2][3]
    
    rgb1  = gridDictionary[col1,row1][4]
    rgb2  = gridDictionary[col2,row2][4]
    
    # print(posX1,posY1,posX2,posY2)
    drawInterPath(posX1,posY1,posX2,posY2,wght1, wght2,xprn1,xprn2, rgb1,rgb2)

# x1 y1 x2 y2
# drawDiagonals(0,stepsY-1, stepsX-1,1)
drawDiagonals(3, stepsY-2,stepsX-4,1)
drawDiagonals(stepsX-4, stepsY-2,3,2)
drawDiagonals(6, stepsY-1,stepsX-3,stepsY-3)


# drawInterPath(x1, y1, x2, y2, interSteps)
    
# drawInterPath(1000, 400, 100, 1000, interSteps)
# be able to plug in multiple values for this – it should be a function

# use for-loop to place interpolated instances between (0,y1) and (-1,y2)


    
# saveImage("/Users/stephennixon/Dropbox/KABK_netherlands/type_media/000-casual-mono/specimens-and-presentations/01-graduation/presentation/assets/var-grid-S-grid-transition4.png")
    