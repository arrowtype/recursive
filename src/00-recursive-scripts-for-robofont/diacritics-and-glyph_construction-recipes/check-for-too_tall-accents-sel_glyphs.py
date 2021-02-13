"""
    Check for parts of selected glyphs that are higher than the hhea.ascent. 
    
    Place guideline to show when top should be.
    
    See:

    https://github.com/arrowtype/recursive/issues/308#issuecomment-778657913
"""

f = CurrentFont()

for gname in f.selection:    
    if f[gname].bounds[3] >= f.info.openTypeHheaAscender:
        print(gname, end=" ")
        #print(f[gname].bounds[3])
        
        f[gname].appendGuideline((0, f.info.openTypeHheaAscender-2), 0)