import datetime
now = datetime.datetime.now()

# make canvas
# make a box the size of the canvas
# divide the box in half, and make two boxes
# repeat

W = 1600
H = 900

# size(W,H)

# rect(0,0,W,H)




# rect(0,0,W,H)


# fps = 30
# # duration of the movie
# seconds = 3
# # calculate the lenght of a single frame
# duration = 1 / fps
# # calculate the amount of frames needed
# totalFrames = seconds * fps

frames = 15

for frame in range(frames):
    
    
    
    # take ratio from 3 to 1
    
    newPage(W,H)
     # set the frame duration
    frameDuration(.5)
    
    fill(0)
    rect(0,0,W,H)
    fill(1,1,1,0)
    stroke(0,1,0)
    strokeWidth(2)
    
    
    # start = 3
    # end = 1
    # distance = start - end
    
    # ratioChange = (distance / frames) * frame
    
    # ratio = start - ratioChange

    def makeRects(counter, loops, width, height):
    
        ratio = 2
        
        green = 1 / 20 + (1/15 * counter)
        
        newWidth = width/ratio
        newHeight = height/ratio

        # if frame % 2 == 0:
        stroke(0,1,0)
        
        # print(green)
        fill(0,green,0,.25)

        # newWidth = width/ratio
        rect(0,0,newWidth, height)

        # with savedState():
        #     # stroke(1,1,0) # yellow
        #     # fill(1,green,0,0.25) #orange
        #     rotate(180, center=(W/2, H/2))
        #     rect(0,0,newWidth, height)
    
        stroke(0,1,1)
        fill(0,green,1,.25)

        # newHeight = height/ratio
        rect(0,0,newWidth, newHeight)
    
            # with savedState():
            #     # stroke(1,1,0) # yellow
            #     # fill(1,green,0,0.25) #orange
            #     stroke(0,1,1)
            #     fill(0,green,1,0.25)
            #     rotate(180, center=(W/2, H/2))
            #     rect(0,0,newWidth, newHeight)
    
        ### TO DO: add rectangles in a loop so that 
            # rects are placed to certain loops number
            # every odd frame, a rectangle is added using the newWidth and existing height
            # every even frame, a rectangle is added using the newWidth and newHeight
            # you can run this with steps, to add them up
            
        if frame % 2 == 0:
            green = 1 / 20 + (1/15 * counter)
        
            newWidth = width/ratio
            newHeight = height/ratio

            # if frame % 2 == 0:
            stroke(0,1,0)
        
            # print(green)
            fill(0,green,0,.25)

            # newWidth = width/ratio
            rect(0,0,newWidth, height)
        
        else:
            green = 1 / 20 + (1/15 * counter)
        
            newWidth = width/ratio
            newHeight = height/ratio

            # if frame % 2 == 0:
            stroke(0,1,0)
        
            # print(green)
            fill(0,green,0,.25)

            # newWidth = width/ratio
            rect(0,0,newWidth, newHeight)
    
    
        # set a counter
        # while counter is less than x, fire makeRects with newWidth
    
        counter += 1
    
        if counter < loops:
            makeRects(counter, frame, newWidth, newHeight)
        
    
    makeRects(0, frame, W, H)

# for i in range(3):
    # i += 1
    # newWidth = W/i/2
    # make rect at half of width and full height
    # rect(0,0,newWidth,H)
    # makeRects(W, H)
    
    # make rect at same half width and half height
    
dateTime = now.strftime("%Y_%m_%d-%H_%M_%S")

# fileName = "exports/recursive-"+dateTime+".svg"

# saveImage(fileName)
# print("done! '" + fileName + "' is saved")


gifName = "exports/recursive-"+dateTime+".gif"
# saveImage(gifName)
# print("done! '" + gifName + "' is saved")
