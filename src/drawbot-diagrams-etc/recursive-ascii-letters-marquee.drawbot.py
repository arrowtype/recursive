import datetime

def hex2rgb(hex):
    h = hex.lstrip('#')
    RGB = tuple(int(h[i:i+2], 16) for i in (0, 2 ,4))
    r1, g1, b1 = RGB[0] / 255, RGB[1] / 255, RGB[2] / 255
    return(r1, g1, b1)

now = datetime.datetime.now()

W, H = 1500, 1800

startX, startY = 23, H-65

fontSize = 30

rows = 48
cols = 81



# print(hex2rgb('#ffffff'))




def addDot(i):
    print(i)
    fill(1,0,0)
    text('·', (startX + (fontSize * 0.6) * i, startY - fontLineHeight() * i))

frames = 80 #100

for frame in range(frames):
    newPage(W,H)

    fill(*hex2rgb('2F3137'))

    rect(0, 0, W, H)
    
    t = frame * 1/frames
    
    posX = t * W
    
    message = "Mono&Sans"
    messageLength = len(message)
    
    txt = FormattedString()
    
    txt.font("Recursive Mono")
    
    txt.fontSize(H*1.25)
    
    weightRange = 1100 - 300
    
    currentWeight = weightRange*t + 300.01
    
    txt.fontVariations(wght=currentWeight)
    
    txt.append(message)

    bez = BezierPath()
    # bez.text(txt, font="Recursive Mono", fontSize=H*1.25, offset=(W-posX*messageLength,H*0.05))

    bez.text(txt, offset=(W-posX*messageLength,H*0.05))
    
    font("Recursive Mono", 30)
    for col in range(0,cols):
        for row in range(0,rows):
            x, y = (startX + (fontSize * 0.6) * col), (startY - fontLineHeight() * row)
        
            if bez.pointInside((x,y)):
                fill(*hex2rgb('78D9FF'))
                text('%', (x, y))
            else:
                fill(0.25, 0.25, 0.35)    
                text('·', (x, y))


saveImage("./exports/recursive-marquee" + now.strftime("%Y_%m_%d-%H_%M_%S") + ".mp4")