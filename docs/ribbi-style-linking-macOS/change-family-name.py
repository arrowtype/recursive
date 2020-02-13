# coding=utf8

'''

	Style-linking for Regular, Italic, Bold, Bold Italic ("RIBBI") does not work well in macOS. 
	https://github.com/arrowtype/recursive/issues/153

	This script will change the family name of a TrueType font, in order to test whether the name "Recursive" is triggering the problem.
	(E.g. could the substring "cursive" be leading macOS to think it is literally a cursive family?)

	USAGE:

	python <path>/change-family-name.py -o "Old Name" -n "New Name" --inplace $(ls <folder_of_fonts>/*.otf)

	(Will accept one or more font paths.)

'''

import os
import argparse
from fontTools.ttLib import TTFont

# GET / SET NAME HELPER FUNCTIONS

def getFontNameID(font, ID, platformID=3, platEncID=1):
	name = str(font['name'].getName(ID, platformID, platEncID))
	return name

def setFontNameID(font, ID, newName):
	
	print(f"\n\t• name {ID}:")
	macIDs = {"platformID": 3, "platEncID": 1, "langID": 0x409}
	winIDs = {"platformID": 1, "platEncID": 0, "langID": 0x0}

	oldMacName = font['name'].getName(ID, *macIDs.values())
	oldWinName = font['name'].getName(ID, *winIDs.values())

	if oldMacName != newName:
		print(f"\n\t\t Mac name was '{oldMacName}'")
		font['name'].setName(newName, ID, *macIDs.values())
		print(f"\n\t\t Mac name now '{newName}'")

	if oldWinName != newName:
		print(f"\n\t\t Win name was '{oldWinName}'")
		font['name'].setName(newName, ID, *winIDs.values())
		print(f"\n\t\t Win name now '{newName}'")


# PARSE ARGUMENTS

parser = argparse.ArgumentParser(description='Add version numbering to font name IDs')

parser.add_argument('fonts', nargs="+")

parser.add_argument(
		"-i",
		"--inplace",
		action='store_true',
		help="Edit fonts and save under the same filepath, without an added suffix.",
	)

parser.add_argument(
		"-o",
		"--oldname",
		required=True,
		help="The old font family name you wish to replace.",
	)

parser.add_argument(
		"-n",
		"--newname",
		required=True,
		help="The new font family name you wish to give fonts.",
	)

# NAME_IDS = {
# 	1: 'familyName',	# Recursive Sans Linear A
# 	3: 'uniqueID',	  # 1.005;ARRW;RecursiveSans-LinearA
# 	4: 'fullName',	  # Recursive Sans Linear A
# 	5: 'version',	   # Version 1.005
# 	6: 'psName',		# RecursiveSans-LinearA
# 	16: 'typeFamily'	# Recursive Sans
# }

def main():
	args = parser.parse_args()

	for font_path in args.fonts:
		# open font path as a font object, for manipulation
		ttfont = TTFont(font_path)

		# UPDATE NAME ID 16, typographic family name
		try:
			currentTypoFamName = getFontNameID(ttfont, 16)
			if currentTypoFamName != 'None':
				newTypoFamName = currentTypoFamName.replace(args.oldname, args.newname)
				print(currentTypoFamName + " → " + newTypoFamName)
				setFontNameID(ttfont, 16, newTypoFamName)
		except:
			print("The font does not seem to have a name ID 16 (typographic family name)")

		# UPDATE NAME ID 6, postscript name
		currentPsName = getFontNameID(ttfont, 6)
		newPsName = currentPsName.replace(args.oldname, args.newname)
		print(currentPsName + " → " + newPsName)
		setFontNameID(ttfont, 6, newPsName)

		# UPDATE NAME ID 4, postscript name
		currentFullName = getFontNameID(ttfont, 4)
		newFullName = currentFullName.replace(args.oldname, args.newname)
		print(currentFullName + " → " + newFullName)
		setFontNameID(ttfont, 4, newFullName)

		# UPDATE NAME ID 3, unique font ID
		currentUniqueName = getFontNameID(ttfont, 3)
		newUniqueName = currentUniqueName.replace(args.oldname, args.newname)
		print(currentUniqueName + " → " + newUniqueName)
		setFontNameID(ttfont, 3, newUniqueName)

		# UPDATE NAME ID 1, unique font ID
		currentFamName = getFontNameID(ttfont, 1)
		newFamName = currentFamName.replace(args.oldname, args.newname)
		print(currentFamName + " → " + newFamName)
		setFontNameID(ttfont, 1, newFamName)

		# SAVE FONT
		if args.inplace:
			#  ttfont.save(font_path)
			 ttfont.save(font_path.replace(args.oldname, args.newname))
		else:
			 ttfont.save(font_path.replace('.ttf','.fix.ttf').replace('.otf','.fix.otf'))


if __name__ == '__main__':
	main()
