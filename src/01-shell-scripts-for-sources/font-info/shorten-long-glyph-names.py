"""
	A script to make list of abbreviated long names in code ligatures.

	This is so you can manually copy-paste the abbreviations into 
	setProductionNames() in mastering/prep_fonts.py

	USAGE:

	python <path>/shorten-long-glyph-names.py <ufo_path>
"""

import sys
import os
import subprocess
from fontParts.world import *
import defcon

abbreviations = {
	"quotesingle": 	"qutsng",
	"quotedbl":		"qutdbl",
	"bracket": 		"brkt",
	"left": 		"lf",
	"right": 		"rt",
	"numbersign": 	"num",
	"ampersand": 	"and",
	"space": 		"spc",
	"asterisk":		"astr",
	"question":		"qust"
}

# get font dir
try:
	if sys.argv[1]:
		ufoPath = sys.argv[1]

except IndexError:
	print("Please include path to UFO")


font = OpenFont(ufoPath, showInterface=False)


print('--------------------------------------------------------')
print(font.info.styleName)

# if glyph name ends with ".code" abbreviate
for glyph in font:
	if ".code" in glyph.name:
		for key in abbreviations.keys():
			if key in glyph.name:
				print(f"'{glyph.name}': ", end="")
				glyph.name = glyph.name.replace(key, abbreviations[key])
				print(f"'{glyph.name}',")

font.close()