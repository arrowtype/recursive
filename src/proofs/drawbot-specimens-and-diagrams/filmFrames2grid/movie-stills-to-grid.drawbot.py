'''
Start by cropping an iphone video into a square:

    ffmpeg -i "IMG_0769.MOV" -filter:v "crop=1080:1080" -c:a copy "IMG_0769-square.MOV"


Extract frames to jpg:

     ffmpeg -i "IMG_0769-square.MOV" -vf fps=16 IMG_0769-still-%04d.jpg -hide_banner

'''

from drawBot import * # requires drawbot to be installed as module
import datetime
import os
newDrawing() # for drawbot module

# newPage()

prop = 0
export=True
autoOpen = True

if prop is 0:
    folderOfFrames = "src/proofs/drawbot-diagrams-etc/filmFrames2grid/mono-stills"
    outputName = "flipbook-frames-mono"
else:
    folderOfFrames = "src/proofs/drawbot-diagrams-etc/filmFrames2grid/sans-stills"
    outputName = "flipbook-frames-sans"

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

stillSize = W/(cols) - (padding/W * (cols + 1))
print(stillSize)

# fill(0,0.1,1)
fill(0)
rect(0,0,W,H)

bg = ImageObject()
with bg:
    # set a size for the image
    size(1100, 1100)
    # draw something
    # fill(0.1, 0.2, 1)
    fill(0)
    rect(0, 0, width(), height())

scale(0.85)
    
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
            # im.vibrance(-1)
            # im.colorControls(saturation=0.001)
            im.screenBlendMode(backgroundImage=bg)
            # rect(x* (1/imageScale), y* (1/imageScale), 1080, 1080) 
            image(im, (x* (1/imageScale),y* (1/imageScale)))

        # rect(x, y, stillSize, stillSize) 
        
        still = still + 1
        

        
endDrawing()

if export:
    now = datetime.datetime.now().strftime("%Y_%m_%d-%H_%M") # -%H_%M_%S

    path = f"src/proofs/drawbot-diagrams-etc/filmFrames2grid/exports/{outputName}-{now}.pdf"

    print("saved to ", path)

    saveImage(path)

    if autoOpen:
        import os
        # os.system(f"open --background -a Preview {path}")
        os.system(f"open -a Preview {path}")

