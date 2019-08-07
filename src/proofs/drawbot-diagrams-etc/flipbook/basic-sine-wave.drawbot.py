
canvasSize = 500

numSteps = 25
dotSize = canvasSize / numSteps

numFrames = 20




for frame in range(numFrames):
    t = frame / numFrames
    print(t)
    newPage(500,500)
    
    amplitude = 100
    ampChange = 50
    # counter = 1
    # if frame < numFrames * .5:
    #     counter += 1
    #     amplitude += ampChange * counter
    # else:
    #     counter -= 1
    #     amplitude -= ampChange * counter
    for i in range(numSteps + 1):
        x = i * dotSize
        angle = 360 * i / numSteps
        angle += t * 360 # change this number to see wave move! 0 and 360 give the same result
        print(i, angle)
        # y  = 500 + 200 * sin(-0.14) # sin wave multiplier naturally eases
        y = 250 + amplitude * sin(radians(angle)) # converts current angle to radians # the other added values will change position and amplitude
        oval(x,y, dotSize, dotSize) 
        
saveImage("exports/wavyWave-2-111717.gif")