"""
    Script to determine permutations and weights of recursive subsets

    Observations:
    - An axis can be limited, so long as the default location is included (e.g. if wght default is 300, wght=300:600 works but wght=800:1000 doesn’t)
    - A limited axis carries the same weight as a full axis, if it includes the same number of source locations
    - Freezing an axis at one location vs another has only a small effect on size, e.g. MONO=1 is 214KB while MONO=0.5 is 218KB while MONO=0 is 219KB
    - CRSV has no impact on filesize, but does have impact on design
"""


import itertools
from pprint import pprint
import sys
import subprocess
# from fontTools import ttLib
# from fontTools.varLib import instancer

fontPath = sys.argv[1]

# inputdata = [
#     ["", "MONO=0", "MONO=0.5"],
#     ["", "wght=300:700", "wght=300:800","wght=400"],
#     ["","slnt=-7.5"],
#     ["", "CASL=1"],
#     ["", "CRSV=0", "CRSV=1"]
# ]

# -------------------------------------------------------------------------------
# determine basic permutations

inputdata = [
    ["", "MONO=1"],
    ["wght=300:800"], # "", "wght=500", "wght=300:1000", # temporary removed
    ["","slnt=-7.5"],
    ["", "CASL=1"],
    # ["", "CRSV=1"]
]

results = list(itertools.product(*inputdata))

permutations = []

for result in results:
    resultList = [i for i in result if i != ""]
    permutations.append(" ".join(resultList))

pprint(permutations)



# -------------------------------------------------------------------------------
# The actual subsetting

# varfont = ttLib.TTFont(fontPath)

for permutation in permutations:
    # partialFont = instancer.instantiateVariableFont(varfont, {"wght": 300})
    print(permutation)

    if permutation is "":
        continue

    command = f"fonttools varLib.instancer {fontPath} {permutation} -o {fontPath.replace('Recursive_VF','partial-fonts/Rec').replace('.woff2', '--'+permutation.replace(' ','_')+'.woff2')}"
    subprocess.check_call(command.split())

    # TODO: 
    # get output file size, rounding to nearest 5kb
    # record permutation & size in dictionary
    # 
    # somehow get this into javascript...

