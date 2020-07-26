"""
    Script to determine number of permutations possible for recursive subsets / instances.

    End goal: make a tool with which users could get custom instances of Recursive.

    See https://github.com/arrowtype/recursive/issues/356.

    Question:

    > "How would it be to generate all permutations and keep them pre-generated,
      then just point to a simple CDN/download for the specific combination chosen by the user?"

    Results:
    - 17984 permutations with stylistic sets & code ligature options included
    - 7228 permutations if variable axis ranges are excluded 
      (e.g. if you were making a tool *only* for outputting static fonts for code, 
      but not partial fonts for other purposes)
    - 4528 permutations if if we excluded axis ranges, really limited the weight options 
      to only steps of 100 rather than 25 and capped it at wght=800, and limited italics 
      to just 0, -9,-12, -15.
    - 4240 permutations if we only allow weights 400 & 700 (Regular and Bold presets)

    Potential Complications:
    - Users would wish to mix & match for RIBBI families (RIBBI = "Regular, Italic, Bold, Bold Italic")
    - Users may wish to give custom families custom naming. If so,
      the naming would have to be edited w/ FontTools after permutations are created.
"""

import itertools
from pprint import pprint

# -------------------------------------------------------------------------------
# determine basic permutations

# minWght = 300
# maxWght = 1000
# wghtStep = 25

# inputdata = {
#     "MONO": ["full", "0","0.5","1"],
#     "CASL": ["full", "0", "0.5", "1"],
#     "wght": ["full", "300:800"] + \
#             [str(minWght + (n * wghtStep)) for n in range(int((maxWght-minWght)/wghtStep) + 1)], # finding options with a step of wghtStep
#     "slnt": ["full","0","-3","-6","-9","-12","-15"],
#     "CRSV": ["full","0","0.5","1"]
# }

# # input data, excluding axis ranges
# inputdata = {
#     "MONO": ["0","0.5","1"],
#     "CASL": ["0", "0.5", "1"],
#     "wght": [str(minWght + (n * wghtStep)) for n in range(int((maxWght-minWght)/wghtStep) + 1)], # finding options with a step of wghtStep
#     "slnt": ["0","-3","-6","-9","-12","-15"],
#     "CRSV": ["0","1"]
# }

# limited scope, excluding axis ranges
# maxWght = 800
# inputdata = {
#     "MONO": ["0","0.5","1"],
#     "CASL": ["0", "0.5", "1"],
#     "wght": [str(minWght + (n * wghtStep)) for n in range(int((maxWght-minWght)/wghtStep) + 1)], # finding options with a step of wghtStep
#     "slnt": ["0","-9","-12","-15"],
#     "CRSV": ["0","1"]
# }

inputdata = {
    "MONO": ["0","0.5","1"],
    "CASL": ["0", "0.5", "1"],
    "wght": ["400","700"], # finding options with a step of wghtStep
    "slnt": ["0","-9","-12","-15"],
    "CRSV": ["0","1"]
}


# each of these could be "frozen" either off or on, in any combination
stylisticSets = [
    ["","ss01"],
    ["","ss02"],
    ["","ss03"],
    ["","ss04"],
    ["","ss05"],
    ["","ss06"],
    ["","ss07"],
    ["","ss08"],
    ["","ss09"],
    ["","ss010"],
    ["","ss011"],
    ["","dlig"] # code ligatures
]

stylisticSets = list(itertools.product(*stylisticSets))

results = list(itertools.product(*inputdata.values())) + stylisticSets

permutations = []

# print(len(permutations))

for result in results:
    resultList = [i for i in result if i != ""]
    permutations.append(" ".join(resultList))

# pprint(permutations)
print(len(permutations))

## to print permutations of stylistic sets as a sanity check

# stylisticSetOptions = []

# for set in stylisticSets:
#     setList = [i for i in set if i != ""]
#     stylisticSetOptions.append(" ".join(setList))

# pprint(stylisticSetOptions)
