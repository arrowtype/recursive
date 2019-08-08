from fontTools.misc.bezierTools import splitCubicAtT

debug = True

newPage(1000,1000)

curve = ((0,0), (500,0), (500,620), (1000,1000))

split = splitCubicAtT(*curve, 0.5)
print(split)
print(split[0])

print(split[1])

frames = 72

for i in range(frames):
    t = i / frames
    split = splitCubicAtT(*curve, t)
    
    loc = split[0][-1]
    
    if debug:
        oval(loc[0], loc[1], 10, 10)