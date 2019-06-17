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
pages = 30
weights = get_font_sizes(pages, 300.01, 1100)

W,H = 500, 500
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
    fill(*hex2rgb('EA8D91'),0.125)
    print(weights[page])
    font("Recursive Mono")
    fontSize(200)
    lineHeight(180)
    currentWeight = weights[page]
    print("currentWeight is ", currentWeight)
    fontVariations(wght=currentWeight)
    text("very \nnice", (10, 285))
    
saveImage("./exports/recursive-wavy-" + now.strftime("%Y_%m_%d-%H_%M_%S") + ".gif")
