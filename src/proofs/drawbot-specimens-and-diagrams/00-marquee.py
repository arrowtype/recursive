W, H = 1024,900
frames = 10 #100
for frame in range(frames):
    newPage(W,H)
    frameDuration(.25)
    fill(0)
    rect(0,0,W,H)
    print("frame " + str(frame))
    t = frame * 1/frames
    print(t)
    
    # translate(40,40)
    resolution = 32
    posX = t*W/resolution
    print(posX)
    message = "nerds"
    # message = message.upper()
    messageLength = len(message)
    print(messageLength)
    bez = BezierPath()
    bez.text(message, font="RecurMono-Bold", fontSize=16, offset=(resolution-posX*messageLength/4.5,1)) #offset=(20-posX,1)
    
    # get pixel dimensions to fit screen
    pixW, pixH = W/resolution*.75, W/resolution*.75
    
    # make grid and light up pixels that are inside letters
    for x in range(resolution):
        save()
        translate(resolution/2,resolution/2)
        for y in range(resolution): 
            if bez.pointInside((x,y)):
                # fill(1,0,0,.35)
                # oval(x*W/resolution, y*W/resolution, pixW, pixH)
                
                fill(.15,0,0,1)
                sizeFactor = 1.5
                oval((x*W/resolution)-(pixW*(1-sizeFactor/2)), (y*W/resolution)-(pixW*(1-sizeFactor/2)), pixW*sizeFactor, pixH*sizeFactor)
                fill(1,0,0)
                oval((x*W/resolution)+(pixW*.125), (y*W/resolution)+(pixW*.125), pixW*.75, pixH*.75)
            else:
                fill(1,0,0,.1)
                oval(x*W/resolution, y*W/resolution, pixW, pixH)
                # oval(x*W/resolution+(pixW*.75/2)-pixW*.35, y*W/resolution + (pixH*.75/2)-pixH*0.35, pixW*.35,pixH*0.35)
        restore()
        
# saveImage("exports/welcome-font-nerds-3.gif")