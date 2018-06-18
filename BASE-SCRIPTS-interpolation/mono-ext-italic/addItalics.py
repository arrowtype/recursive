import os
import fontmake
from fontmake.font_project import FontProject

import fontTools
from fontTools.ttLib import TTFont
from fontTools.varLib.featureVars import addFeatureVariations


fontPath = "variable_ttf/recursive-mono-ext-var-italic-VF.ttf"

f = TTFont(fontPath)

condSubst = [
    # A list of (Region, Substitution) tuples.
    ([{"slnt": (0.5, 1.0)}], {"a": "a.italic"}),
    ([{"slnt": (0.5, 1.0)}], {"g": "g.italic"}),
    ([{"slnt": (0.5, 1.0)}], {"i": "i.italic"}),
    ([{"slnt": (0.5, 1.0)}], {"l": "l.italic"}),
    ([{"slnt": (0.5, 1.0)}], {"r": "r.italic"}),
    ([{"slnt": (0.5, 1.0)}], {"y": "y.italic"}),
]

addFeatureVariations(f, condSubst)

newFontPath = fontPath.split(".")[0] + "-italic.ttf" 
f.save(newFontPath)

os.system('open %s' % newFontPath)