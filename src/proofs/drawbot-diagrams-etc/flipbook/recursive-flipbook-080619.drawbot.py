# make flipbook pages for an animated specimen

import datetime
from math import sin, pi

bookSize = 3

W, H = 72*bookSize, 72*bookSize # size is 72 dpi * bookSize

pages = 5 # 200


# interpolate axis function

for page in range(0,pages):
    newPage(W, H)
    frameDuration(1/60)



now = datetime.datetime.now()


saveImage("./exports/recursive-flipbook-" + now.strftime("%Y_%m_%d-%H_%M_%S") + ".gif")