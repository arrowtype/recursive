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
pages = 100
weights = get_font_sizes(pages, 300.01, 900)
expressions = get_font_sizes(pages, 0, 1000)

W,H = 500, 500
now = datetime.datetime.now()



# txt.font("./recursive-sans-ext-var-italic-VF.ttf")



print(weights)
print(expressions)

for page in range(0,pages):
    newPage(W, H)
    frameDuration(1/60)
    fill(*hex2rgb('222222'))
    rect(0, 0, W, H)
    # fill(0,0,0)
    fill(*hex2rgb('FFFFFF'),1)
    print(weights[page])
    font("Rec Mono Beta013 Var")
    fontSize(W/1.375)
    # lineHeight(180)
    currentWeight = weights[page]
    currentExpression = expressions[page]*0.001 + 0.001
    print("currentWeight is ", currentWeight)
    fontVariations(
        wght=currentWeight, 
        XPRN=currentExpression,
        slnt=-15*currentExpression
        )
    text("rw", (W/16, H/12))
    
    barChartWidth = 14
    wghtChart = f"[{'|'.ljust(int(barChartWidth*currentExpression),'|').ljust(barChartWidth)}]"
    xprnChart = f"[{'|'.ljust(int(barChartWidth*currentExpression),'|').ljust(barChartWidth)}]"
    fontSize(W/20)
    text(f"wght {str(round(currentWeight,0)).ljust(6)} {wghtChart} \n\
XPRN {str(round(currentExpression,2)).ljust(6)} {xprnChart} \n\
slnt {str(round(currentExpression,2)).ljust(6)} {xprnChart}", (W/10, H/1.15))
    
saveImage("./exports/recursive-wavy-" + now.strftime("%Y_%m_%d-%H_%M_%S") + ".gif")
