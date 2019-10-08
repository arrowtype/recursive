import datetime
from typing import List, TypeVar, Callable
from math import sin, pi

# TypeVar for a generic number type
Num = TypeVar('Num', int, float)

"""
Function that generates a List of integers that represent a interpolation of font sizes from min to max along
a sin wave function that has been transformed to have the desired properties.
Returns a List of Integers (List[int]) of size num_pages containing font sizes interpolated between min and max.
"""
def get_font_sizes(num_pages: int, min: int = 6, max: int = 72, round_strategy: Callable[[Num], int] = round) -> List[int]:
    # Define a function y that transforms an input t from [0 .. 2pi] to a font size between min and max
    amplitude = (max - min) / 2.0
    y = lambda t: round_strategy(amplitude * sin(t - (pi / 2.0)) + amplitude + min)
    # Transform the range of inputs from [0 .. N] to [0 .. 2*pi] where N = num_pages
    delta = 2.0 * pi / num_pages
    # Invoke y with inputs translated to [0 .. 2pi] using delta constant
    return [ y(t) for t in [ delta * n for n in range(num_pages) ] ]

# This example interpolates between size 10 and 60 instead of the default 6 and 72
pages = 120
sizes = get_font_sizes(pages, 100, 300)

W,H = 500, 500
now = datetime.datetime.now()

for page in range(0,pages):
    newPage(W, H)
    frameDuration(1/60)
    fill(1,1,1)
    rect(0,0,W,H)
    fill(0,0,0)
    rect(100, 100, sizes[page], sizes[page])
    
saveImage("./exports/recursive-wavy" + now.strftime("%Y_%m_%d-%H_%M_%S") + ".gif")
