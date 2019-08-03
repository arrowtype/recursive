'''
Start by cropping an iphone video into a square:

    ffmpeg -i "IMG_0769.MOV" -filter:v "crop=1080:1080" -c:a copy "IMG_0769-square.MOV"


Extract frames to jpg:

     ffmpeg -i "IMG_0769-square.MOV" -vf fps=16 IMG_0769-still-%04d.jpg -hide_banner

'''

import os

# newPage()

folderOfFrames = "~/Downloads/bike-stills/"

W = 6 * 72
H = 8.5 * 72

newPage(W,H)

stillsList = []

for (dirpath, dirname, fnames) in os.walk(os.path.expanduser(folderOfFrames)):
    for f in fnames:
        if f.endswith(".png") or f.endswith(".jpg"):
            stillsList.append(os.path.join(dirpath, f))

stillsList.sort() # necessar to make images go in order

sizingImage = ImageObject(path=stillsList[0])

rows = 6
cols = 4
still = 0

imageScale = W/sizingImage.size()[0] / cols

print(imageScale)

padding = 8

#TODO: figure out how to properly size the image grid based on page size. scale() is just a temporary hack for this. 
scale(0.9)

stillSize = W/(cols) - (padding/W * (cols + 1))
print(stillSize)
    
for currentRow in range(rows):
    
    # x = W/(cols+2) + currentCol*stillSize
    y = H - ((stillSize * currentRow) + (padding*currentRow) + padding)
    for currentCol in range(cols):
    
        # y = W/(rows+2) + currentRow*stillSize
        x = (stillSize * currentCol) + (padding*currentCol) + padding
        
        im = ImageObject(stillsList[still])
        
        print(still)
        
        with savedState():
            scale(imageScale)
            
            print(x,y)
            
            stroke(1,1,0)            
            # rect(x* (1/imageScale), y* (1/imageScale), 1080, 1080) 
            image(im, (x* (1/imageScale),y* (1/imageScale)))

        # rect(x, y, stillSize, stillSize) 
        
        still = still + 1
        

saveImage("exports/grid-of-frames--test-2.png")
        