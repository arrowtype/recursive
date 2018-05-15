# make canvas
# make a box the size of the canvas
# divide the box in half, and make two boxes
# repeat

W = 1000
H = 750

size(W,H)

rect(0,0,W,H)


fill(1,1,1,0)
stroke(0,1,0)
strokeWidth(2)

rect(0,0,W,H)

def makeRects(i, width, height):
    
    newWidth = width/2
    rect(0,0,newWidth, height)

    newHeight = height/2
    rect(0,0,newWidth, newHeight)
    
    # set a counter
    # while counter is less than x, fire makeRects with newWidth
    
    i += 1
    
    if i < 6:
        makeRects(i, newWidth, newHeight)
        
    
makeRects(0, W, H)

# for i in range(3):
    # i += 1
    # newWidth = W/i/2
    # make rect at half of width and full height
    # rect(0,0,newWidth,H)
    # makeRects(W, H)
    
    # make rect at same half width and half height

