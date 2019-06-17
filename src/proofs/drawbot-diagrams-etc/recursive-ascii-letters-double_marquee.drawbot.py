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

frames = 50 # 60

longMessage = "@@@@@@ Recursive Mono & Sans: A typographic palette for vibrant code & UI @@@@@@".upper()

message = "&&"

for frame in range(frames):
    newPage(W,H)

    fill(*hex2rgb('2F3137'))

    rect(0, 0, W, H)
    
    t = frame * 1/frames
    
    messageLength = len(message)
    
    posX = t * W * messageLength * 0.7
    
    txt = FormattedString()
    
    txt.font("Recursive Mono")
    
    txt.fontSize(H*1.26)
    
    weightRange = 1100 - 220
    currentWeight = weightRange*t + 220.01
    
    slantRange = 14 - 0
    currentSlant = slantRange*t + 0.01
    
    currentExpression = 1 * t + 0.001
    
    txt.fontVariations(wght=currentWeight)
    
    txt.append(message)

    bez = BezierPath()
    # bez.text(txt, font="Recursive Mono", fontSize=H*1.25, offset=(W-posX*messageLength,H*0.05))

    bez.text(txt, offset=(-W*1.75+posX*messageLength, H*0.05))
    
    font("Recursive Mono", 30)
    
    fontVariations(slnt=currentSlant, XPRN=currentExpression)
    
    for col in range(0,cols):
        for row in range(0,rows):
            x, y = (startX + (fontSize * 0.6) * col), (startY - fontLineHeight() * row)
        
            if bez.pointInside((x,y)):
                
                if longMessage[col-1] == ' ':
                    fontVariations(slnt=0.01)
                    fill(*hex2rgb('EA8D91'))
                    text('•', (x, y))
                elif longMessage[col-1] == '@':
                    fill(*hex2rgb('EA8D91'))
                    fontVariations(slnt=0.01)
                    text('@', (x, y))
                else:
                    fontVariations(slnt=currentSlant)
                    fill(*hex2rgb('F3B665'))
                    text(longMessage[col-1], (x, y))
            else:
                fill(0.25, 0.25, 0.35)    
                text('·', (x, y))


saveImage("./exports/recursive-marquee" + now.strftime("%Y_%m_%d-%H_%M_%S") + ".mp4")