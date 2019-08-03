W, H = 1080, 1080

for i in range(0,32):
    
    newPage(W, H)
    
    fill(0,0,1)
    rect(0,0,W, H)
    
    fill(1)
    fontSize(300)
    text(str(i), (300, 300))
    saveImage("~/Desktop/test-stills/"+str(i).rjust(2,"0")+".png")