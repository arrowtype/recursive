"""
                                                                           
                                                                           
        |– – – – – – –|                                    NOORDZIJCUBE    
    z5  | s5. top     |                                    CONSTRUCTION    
        |             |                                                    
        |             |                                                    
        |             |                                                    
        |– – – – – – –|                                                    
        |– – – – – – –| |– – – – – – –| |– – – – – – –| |– – – – – – –|    
    z4  | s1. front   | | s2. right   | | s3. back    | | s4. left    |    
    z3  |             | |             | |             | |             |    
    z2  |             | |             | |             | |             |    
    z1  |             | |             | |             | |             |    
        |– – – – – – –| |– – – – – – –| |– – – – – – –| |– – – – – – –|    
        |– – – – – – –|                                                    
    z0  | s0. bottom  |                                                    
        |             |                                      • – – – •     
        |             |                                    /   5   / |     
        |             |                               ↑  • – – – • 2 •     
        |– – – – – – –|                               z  |   1   | /  ↗    
                                                         • – – – •  y      
                                                            x →            
                                                                           
                                                                           
"""

# given -x CASL -y wght -z slnt --Xasc True --Yasc True --Zasc True

# def makeDrawing(xVar="wght", yVar="slnt", Xasc=True, Yasc=True, letter="a", rows=6, cols=6, MONOVal=0, CASLVal=0, wghtVal=300, slntVal=0, italVal=0.5, fileTag=""):
#     print("xVar", xVar)
#     print("yVar", yVar)
#     print("Xasc", Xasc)
#     print("Yasc", Yasc)
#     print("letter", letter)
#     print("rows", rows)
#     print("cols", cols)
#     print("MONOVal", MONOVal)
#     print("CASLVal", CASLVal)
#     print("wghtVal", wghtVal)
#     print("slntVal", slntVal)
#     print("italVal", italVal)
#     print("fileTag", fileTag)
#     print()

axes = {
	'MONO': (0, 1),
	'CASL': (0, 1),
	'wght': (300, 1000),
	'slnt': (0, -15)
	# 'ital': (0, 1), # intentionally left out
}

def makeCube(xAxis, yAxis, zAxis, Xasc=True, Yasc=True, Zasc=True, rows=6):

    zVal = f"{zAxis}Val"

    # go through rows+2, because you need sides, plus bottom & top
    for z in range(rows+2):
        if z == 0:
            # s0: X↑, Y↓, Zmin
            kwargs = {"xVar": xAxis, "yVar": yAxis, "Yasc": False, zVal: axes[zAxis][0]}
            makeDrawing(**kwargs)
        elif z > 0 and z < (rows+2):
            # s1: X↑, Z↑, Ymin
            kwargs = {"xVar": xAxis, "yVar": zAxis, zVal: axes[yAxis][0]}
            makeDrawing(**kwargs)
            # s2: Y↑, Z↑, Xmax
            kwargs = {"xVar": yAxis, "yVar": zAxis, zVal: axes[xAxis][1]}
            makeDrawing(**kwargs)
            # s3: X↓, Z↑, Ymax
            kwargs = {"xVar": xAxis, "yVar": zAxis, Xasc=False, zVal: axes[yAxis][1]}
            makeDrawing(**kwargs)
            # s4: Y↓, Z↑, Xmin
            kwargs = {"xVar": yAxis, "yVar": zAxis, Xasc=False, zVal: axes[xAxis][0]}
            makeDrawing(**kwargs)
        elif z == (rows+2):
            # s5: X↑, Y↑, Zmax
            kwargs = {"xVar": xAxis, "yVar": yAxis, zVal: axes[xAxis][1]}
            makeDrawing(**kwargs)

makeCube("CASL", "wght", "slnt")