"""
    Recursive is intended to have tabular figures by default. However, there are some kerns present in these figures, which disrupts their tabularity.

    A known issue is kerning between /seven and /period. But, there may be other kerns beyond that. This will check for them so they can be removed.
"""

# from fontParts.fontshell import RFont as Font
from ufoLib2 import Font
from fontTools.ufoLib.kerning import lookupKerningValue

font = Font("src/ufo/sans/Recursive Sans-Casual A.ufo")

numbers = "zero one two three four five six seven eight nine".split(" ")

grouped = []
for value in font.groups.values():
    for name in value:
        grouped.append(name)

numberKerns = {}

for number in numbers:
    numberKerns[number] = []
    for name in font.keys():
        kern1 = lookupKerningValue((number, name), font.kerning, font.groups)
        kern2 = lookupKerningValue((name, number), font.kerning, font.groups)

        if kern1 != 0:
            numberKerns[number].append(((number, name), kern1))
        if kern2 != 0:
            numberKerns[number].append(((name, number), kern2))

import pprint
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(numberKerns)
