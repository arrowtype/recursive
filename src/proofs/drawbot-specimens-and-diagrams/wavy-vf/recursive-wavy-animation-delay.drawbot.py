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
rows = 11
pages = rows * 5
weights = get_font_sizes(pages, 300.01, 1100)

W,H = 750, 900
now = datetime.datetime.now()



# txt.font("./recursive-sans-ext-var-italic-VF.ttf")



print(weights)

for page in range(0,pages):
    newPage(W, H)
    frameDuration(1/60)
    fill(*hex2rgb('2F3137'))
    rect(0, 0, W, H)
    # fill(0,0,0)
    stroke(*hex2rgb('F3B665'))
    strokeWidth(0.5)
    fill(*hex2rgb('ffffff'),0.125)

    font("Recursive Mono")
    
    lineHeight(160)
    
    message = "RECURSIVE"

    
    
    fontSize((W/len(message)) * .832)
    
    for i in range(0,rows):
        advance = page + i*2
        if advance  >= pages:
            currentWeight = weights[page - pages + i*2]
        else:
            currentWeight = weights[advance ]
        fontVariations(wght=currentWeight, XPRN=0.01,slnt=0)
        # text("VERY NICE", (W/11.5, H/20*i + H/150))
        text("MONO&SANS", (W/(rows*2) *i * 1.105, H/rows*i + H/60))
        
    for j in range(0,rows):
        advance = pages - page + j*2
        if advance  >= pages:
            currentWeight = weights[advance - pages]
        else:
            currentWeight = weights[advance]
        fontVariations(wght=currentWeight, XPRN=1, slnt=0)
        # text("VERY NICE", (W/11.5, H/20*i + H/150))
        text("RECURSIVE", (W - ((rows*2) * j * 1.7), H/rows*j + H/60), align="right")
    
    
saveImage("./exports/recursive-wavy-" + now.strftime("%Y_%m_%d-%H_%M_%S") + ".mp4")
