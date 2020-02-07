"""
                                                                           
                                                                           
                                                                           
        |– – – – – – –| |– – – – – – –| |– – – – – – –| |– – – – – – –|    
    z4  | s1. front   | | s2. right   | | s3. back    | | s4. left    |    
    z3  |             | |             | |             | |             |    
    z2  | X↑ Z↑       | | Y↓ Z↑       | | X↓ Z↑       | | Y↑ Z↑       |    
    z1  | Ymin        | | Xmax        | | Ymax        | | Xmin        |    
        |– – – – – – –| |– – – – – – –| |– – – – – – –| |– – – – – – –|    
                                                                           
                                                                           
                                                                           

"""

import cubeHelpers
from cubeHelpers.drawVarGrid import *
import importlib
importlib.reload(cubeHelpers.drawVarGrid)
from cubeHelpers.drawVarGrid import *

axes = {
	'MONO': (0, 1),
	'CASL': (0, 1),
	'wght': (300, 1000),
	'slnt': (-15, 0)
	# 'ital': (0, 1), # intentionally left out
}

name="wght_CASL"

letter="a"

columns = 1
reps = 6

for rep in range(0,reps):
    factor = rep + 1
    columns *= 2
    kwargs = {"MONOVal": 1, "letter": letter, "cols": columns, "rows": int(columns/1.333333333), "axes": axes, "fileTag": f"00_side_a-{name}", "xVar": "slnt,CASL", "Xasc": "1,1", "yVar": "wght", "Yasc": "0"}
    drawVarGrid(**kwargs)

    kwargs = {"MONOVal": 1, "letter": letter, "cols": columns, "rows": int(columns/1.333333333), "axes": axes, "fileTag": f"00_side_a-{name}", "xVar": "slnt,CASL", "Xasc": "0,1", "yVar": "wght", "Yasc": "0"}
    drawVarGrid(**kwargs)
