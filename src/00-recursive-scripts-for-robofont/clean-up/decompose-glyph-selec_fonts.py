'''
	Decompose named glyph in selected fonts
'''

from mojo.UI import AskString
from vanilla.dialogs import *

glyphsToDecompose = AskString('Glyph to decompose').split(' ')

files = getFile("Select files to decompose glyph in", allowsMultipleSelection=True, fileTypes=["ufo"])

for file in files:
	font = OpenFont(file, showInterface=False)

	print("\n",font.info.styleName)

	for glyphName in glyphsToDecompose:

		if glyphName in font.keys():
			font[glyphName].decompose()
			print(f"{glyphName} decomposed")
		else:
			print(f"{glyphName} not in font")

	font.save()
	font.close()