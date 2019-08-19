W,H = 500,500
newPage(W,H)

size = 5
increment = H/10

def branch(startX, startY, endX, endY, level, levels, increment):
    fill(0.625)
    rect(startX-size*0.125, startY/2,size*0.25,startY/2)
    fill(0,0,1,1)
    oval(startX-size*0.5,startY,size, size)
    
    if level < levels:
        startX = startX
        startY = startY + increment
        increment *= 0.75
        branch(startX, startY, endX, endY, level + 1, levels, increment)
    
branch(W/2, H/5, 0, 8, increment)