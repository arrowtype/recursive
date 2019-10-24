import datetime
from typing import List, TypeVar, Callable
from math import sin, pi

def hex2rgb(hex):
    h = hex.lstrip('#')
    RGB = tuple(int(h[i:i+2], 16) for i in (0, 2 ,4))
    r1, g1, b1 = RGB[0] / 255, RGB[1] / 255, RGB[2] / 255
    return(r1, g1, b1)

# TypeVar for a generic number type
Num = TypeVar('Num', int, float)

"""
Function that generates a List of integers that represent a interpolation of font sizes from min to max along
a sin wave function that has been transformed to have the desired properties.
Returns a List of Integers (List[int]) of size num_pages containing font sizes interpolated between min and max.
"""
def get_font_sizes(num_pages: int, min: int = 6, max: int = 72, round_strategy: Callable[[Num], float] = round) -> List[int]:
    # Define a function y that transforms an input t from [0 .. 2pi] to a font size between min and max
    amplitude = (max - min) / 2.0
    y = lambda t: round_strategy(amplitude * sin(t - (pi / 2.0)) + amplitude + min)
    # Transform the range of inputs from [0 .. N] to [0 .. 2*pi] where N = num_pages
    delta = 2.0 * pi / num_pages
    # Invoke y with inputs translated to [0 .. 2pi] using delta constant
    return [ y(t) for t in [ delta * n for n in range(num_pages) ] ]

# This example interpolates between size 10 and 60 instead of the default 6 and 72
rows = 25
pages = rows * 3
interpolatedCurve = get_font_sizes(pages, 0.001, 100)

W,H = 1500, 1800
now = datetime.datetime.now()



# txt.font("./recursive-sans-ext-var-italic-VF.ttf")

wghtMin = 300
wghtMax = 1100
wghtRange = wghtMax - wghtMin

XPRNMin = 0.01
XPRNMax = 1
XPRNRange = XPRNMax - XPRNMin

slntMin = 0
slntMax = 14
slntRange = slntMax - slntMin

print(interpolatedCurve)

for page in range(0,pages):
    newPage(W, H)
    frameDuration(1/60)
    fill(*hex2rgb('2F3137'))
    rect(0, 0, W, H)
    # fill(0,0,0)
    # fill(*hex2rgb('ffffff'),0.125)
    fill(*hex2rgb('FFFFFF'))

    font("Recursive Sans")
    
    lineHeight(160)
    
    message = "A typographic pallete for vibrant code & UI"

    
    
    fontSize((W/len(message)) * 2)
    
    for i in range(0,rows):
        advance = page + i*2
        if advance  >= pages:
            currentWeight = wghtMin + wghtRange * interpolatedCurve[page - pages + i*2] /100
            currentSlant = slntMax - slntRange * interpolatedCurve[page - pages + i*2] /100
            currentExpression = XPRNMin + XPRNRange * interpolatedCurve[page - pages + i*2] /100
        else:
            currentWeight = wghtMin + wghtRange * interpolatedCurve[advance] /100
            currentSlant = slntMax - slntRange * interpolatedCurve[advance] /100
            currentExpression = XPRNMin + XPRNRange * interpolatedCurve[advance] /100
        fontVariations(wght=currentWeight, XPRN=currentExpression,slnt=currentSlant)
        # text("VERY NICE", (W/11.5, H/20*i + H/150))
        text(message, (0, H/rows*i + H/100))
        
    # for j in range(0,rows):
    #     advance = pages - page + j*2
    #     if advance  >= pages:
    #         currentWeight = weights[advance - pages]
    #     else:
    #         currentWeight = weights[advance]
    #     fontVariations(wght=currentWeight, XPRN=1, slnt=0)
    #     # text("VERY NICE", (W/11.5, H/20*i + H/150))
    #     text("MONO&SANS", (W, H/rows*j + H/200), align="right")
    
    
saveImage("./exports/recursive-wavy-" + now.strftime("%Y_%m_%d-%H_%M_%S") + ".mp4")
