# make flipbook pages for an animated specimen
# https://codepen.io/thundernixon/pen/wVypxe?editors=1100

import datetime
from math import sin, pi

bookSize = 3

W, H = 72*bookSize, 72*bookSize # size is 72 dpi * bookSize

pages = 25 # 200

amplitude = 200
ampChange = 50

# interpolate axis function

for page in range(0,pages):
    newPage(W, H)
    
    t = page/pages
    
    
    # currentWeight = weights[page]
    # currentExpression = expressions[page]*0.001 + 0.001

    currentRate = 360 * t
    
    angle = 360 * t

    angle += t * 360

    y = 250 + amplitude * sin(radians(angle))

    print("page: ".ljust(10), page)
    print("t: ".ljust(10), t)
    print("angle: ".ljust(10), angle)
    print("y: ".ljust(10), y, "\n")
    rect(100, y/2, 10, 10)
    
#     fontVariations(
#         wght=currentWeight, 
#         XPRN=currentExpression,
#         slnt=-15*currentExpression
#         )
#     text("rw", (W/16, H/12))


now = datetime.datetime.now()


saveImage("./exports/recursive-flipbook-" + now.strftime("%Y_%m_%d-%H_%M_%S") + ".gif")