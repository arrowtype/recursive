from mojo.UI import AskString
import math

f = CurrentFont()

af = AllFonts()

# glyphName = CurrentGlyph().name
glyphName = AskString('Glyph to duplex / multiplex / superplex')

width = int(AskString('Glyph width'))

for f in af:
    
    print("----------------------------------")
    
    print(f.info.styleName)
    
    g = f[glyphName]
    
    g.width = width
    
    totalMargin = g.leftMargin + g.rightMargin
    
    print(totalMargin)
    
    g.leftMargin = totalMargin/2
    g.rightMargin = totalMargin/2

    g.width = width
    
    # print(g.leftMargin, g.rightMargin, g.width, g.name)
    
    #italic offset

    try:
        if f.info.italicAngle:
            
            halfOfGlyph = math.floor((g.bounds[1] + g.bounds[3]) / 2)
            
            print(g.bounds, g.bounds[1], g.bounds[-1])
        
            print(halfOfGlyph)
        
            italicSlantOffset = math.tan(f.info.italicAngle * math.pi / 180) * (f.info.xHeight * 0.5) # * halfOfGlyph
            
            print(italicSlantOffset)
        
            # italicOffset = f.lib["com.typemytype.robofont.italicSlantOffset"]
        
            g.moveBy((-italicSlantOffset/2,0))
            
            print(g.leftMargin, g.rightMargin)
    except:
        print("no italic angle")
    
    