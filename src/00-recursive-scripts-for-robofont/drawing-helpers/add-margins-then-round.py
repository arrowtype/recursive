### add sidebearings to selected glyphs

import math

f = CurrentFont()

# sidebearing = 40

# get margin from symmetrical glyph

sidebearing = f["o"].leftMargin

roundingUnit = 50

italicOffset = f.lib["com.typemytype.robofont.italicSlantOffset"]

def roundToNearestUnit(x, base):
    # return int(base * round(float(x)/base))
    return int(base * math.ceil(float(x)/base))

for g in f.selection:
    f[g].leftMargin = sidebearing # avg margin for fonts
    f[g].rightMargin = sidebearing # avg margin for fonts
    print(f[g].leftMargin, f[g].rightMargin, f[g].width)
    
    
    roundedWidth = roundToNearestUnit(f[g].width, roundingUnit)
    
    f[g].width = roundedWidth
    
    totalNewMargin = f[g].leftMargin + f[g].rightMargin
    
    print(totalNewMargin)
    
    f[g].leftMargin = totalNewMargin/2
    f[g].rightMargin = totalNewMargin/2
    
    print(f[g].leftMargin, f[g].rightMargin, f[g].width)

    for c in f[g]:     
        c.moveBy((italicOffset, 0))


