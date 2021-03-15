"""
    A script to check GDEF class of glyphs with FontTools.
"""

import sys
from fontTools.ttLib import TTFont

fontPath = "fonts/ArrowType-Recursive-1.077/Recursive_Desktop/Recursive_VF_1.077.ttf"

check = "0300, 0301, 0302, 0303, 0304, 0306, 0307, 0308, 0309, 030A, 030B, \
030C, 030F, 0311, 0312, 0315, 031B, 0323, 0324, 0325, 0326, 0327, 0328, \
032E, 0331, 0335".split(", ")

font = TTFont(fontPath)

for definition in font['GDEF'].table.GlyphClassDef.classDefs.items():
    if definition[0].replace("uni","") in check:
        if definition[1] == 3:
            print(definition, " → looks good!")
        else:
            print(definition, " → ⚠️ is incorrect")
