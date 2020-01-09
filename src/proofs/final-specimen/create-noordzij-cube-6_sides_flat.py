"""
                                                                           
                                                                           
        |– – – – – – –|                                       FLATTENED    
    z5  | s5. top     |                                   NOORDZIJ CUBE    
        |             |                                    CONSTRUCTION    
        | X↑ Y↓       |                                                    
        | Zmax        |                                                    
        |– – – – – – –|                                                    
        |– – – – – – –| |– – – – – – –| |– – – – – – –| |– – – – – – –|    
    z4  | s1. front   | | s2. right   | | s3. back    | | s4. left    |    
    z3  |             | |             | |             | |             |    
    z2  | X↑ Z↑       | | Y↓ Z↑       | | X↓ Z↑       | | Y↑ Z↑       |    
    z1  | Ymin        | | Xmax        | | Ymax        | | Xmin        |    
        |– – – – – – –| |– – – – – – –| |– – – – – – –| |– – – – – – –|    
        |– – – – – – –|                                                    
    z0  | s0. bottom  |                                                    
        |             |                                      • – – – •     
        | X↑ Y↑       |                                    /   5   / |     
        | Zmin        |                               ↑  • – – – • 2 •     
        |– – – – – – –|                               z  |   1   | /  ↗    
                                                         • – – – •  y      
                                                            x →            
                                                                           
                                                                           
"""

import cubeHelpers
from cubeHelpers.drawCubeSide import *
import importlib
importlib.reload(cubeHelpers.drawCubeSide)
from cubeHelpers.drawCubeSide import *

axes = {
	'MONO': (0, 1),
	'CASL': (0, 1),
	'wght': (300, 1000),
	'slnt': (-15, 0)
	# 'ital': (0, 1), # intentionally left out
}


def makeCube(xAxis, yAxis, zAxis, Xasc=True, Yasc=True, Zasc=True, rows=6, cols=4, mono=0):

    xVal = f"{xAxis}Val"
    yVal = f"{yAxis}Val"
    zVal = f"{zAxis}Val"
    name = f"{xAxis}_{yAxis}_{zAxis}"

    # TODO: if Zasc is False, feed in axes[zAxis] reversed

    # go through sides of cube
    for s in range(0,6):
        if s == 0:
            # s0: X↑, Y↑, Zmin
            kwargs = {"MONOVal": mono, "letter": "rw", "cols": cols, "axes": axes, "fileTag": f"00_bottom-{name}", "xVar": xAxis, "yVar": yAxis, "Xasc": Xasc, "Yasc": Yasc, zVal: axes[zAxis][0]}
            drawFlatCubeSide(**kwargs)
        elif s == 1:
            # s1: X↑, Z↑, Ymin
            kwargs = {"MONOVal": mono, "letter": "rw", "cols": cols, "axes": axes, "fileTag": f"01_front-{name}", "xVar": xAxis, "yVar": zAxis,"Xasc": Xasc, "Yasc": Yasc, yVal: axes[yAxis][1]}
            drawFlatCubeSide(**kwargs)
        elif s == 2:
            # s2: Y↓, Z↑, Xmax
            kwargs = {"MONOVal": mono, "letter": "rw", "cols": cols, "axes": axes, "fileTag": f"02_right-{name}", "xVar": yAxis, "yVar": zAxis, "Xasc": not Xasc, "Yasc": Yasc, xVal: axes[xAxis][1]}
            print(kwargs)
            drawFlatCubeSide(**kwargs)
        elif s == 3:
            # s3: X↓, Z↑, Ymax
            kwargs = {"MONOVal": mono, "letter": "rw", "cols": cols, "axes": axes, "fileTag": f"03_back-{name}", "xVar": xAxis, "yVar": zAxis, "Xasc": not Xasc, "Yasc": Yasc, yVal: axes[yAxis][0]}
            print(kwargs)
            drawFlatCubeSide(**kwargs)
        elif s == 4:
            # s4: Y↑, Z↑, Xmin
            kwargs = {"MONOVal": mono, "letter": "rw", "cols": cols, "axes": axes, "fileTag": f"04_left-{name}", "xVar": yAxis, "yVar": zAxis, "Xasc": Xasc, "Yasc": Yasc, xVal: axes[xAxis][0]}
            drawFlatCubeSide(**kwargs)
        elif s == 5:
            # s5: X↑, Y↓, Zmax
            kwargs = {"MONOVal": mono, "letter": "rw", "cols": cols, "axes": axes, "fileTag": f"05_top-{name}", "xVar": xAxis, "yVar": yAxis, "Xasc": Xasc, "Yasc": not Yasc,  zVal: axes[zAxis][1]}
            drawFlatCubeSide(**kwargs)

# xyz values - to generate monospace cube, use arg mono=1
makeCube("CASL", "wght", "slnt", mono=1)
# makeCube( "wght", "CASL", "slnt")
# makeCube("slnt", "wght", "CASL")