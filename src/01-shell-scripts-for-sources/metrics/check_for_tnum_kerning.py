"""
    Recursive is intended to have tabular figures by default. However, there are some kerns present in these figures, which disrupts their tabularity.

    A known issue is kerning between /seven and /period. But, there may be other kerns beyond that. This will check for them so they can be removed.
"""

from fontParts.fontshell import RFont as Font

font = Font("src/ufo/sans/Recursive Sans-Casual A.ufo")

numbers = "zero one two three four five six seven eight nine".split(" ")

for key in font.kerning.keys():
    if key[0] in numbers or key[1] in numbers:
        print(key)

