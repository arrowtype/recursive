"""
	A script to generate Recursive fonts for code with:
	- An abbreviated family name to avoid macOS style-linking bug
		- Rec Mono
	- A reduced italic slant (probably -10 degrees)
	- The following static instances:
		- Linear
		- Linear Italic
		- Linear Bold
		- Linear Bold Italic
		- Casual
		- Casual Italic
		- Casual Bold
		- Casual Bold Italic

	USAGE:

	python <path>/instantiate-code-fonts.py <recursive-VF>

	NOTE: assumes it will act on the Recursive variable font as of e84015de.
"""

import os
import pathlib
from fontTools import ttLib
from fontTools.varLib import instancer
import fire

# instances to split

instanceValues = {
	# Linear package
	'Linear': {
		'Linear': {
			'MONO': 1,
			'CASL': 0,
			'wght': 400,
			'slnt': 0,
			'style': 'Regular'
		},
		'Linear Italic': {
			'MONO': 1,
			'CASL': 0,
			'wght': 400,
			'slnt': -10,
			'style': 'Italic'
		},
		'Linear Bold': {
			'MONO': 1,
			'CASL': 0,
			'wght': 700,
			'slnt': 0,
			'style': 'Bold'
		},
		'Linear Bold Italic': {
			'MONO': 1,
			'CASL': 0,
			'wght': 700,
			'slnt': -10,
			'style': 'Bold Italic'
		},
	},
	# Casual package
	'Casual': {
		'Casual': {
			'MONO': 1,
			'CASL': 1,
			'wght': 400,
			'slnt': 0,
			'style': 'Regular'
		},
		'Casual Italic': {
			'MONO': 1,
			'CASL': 1,
			'wght': 400,
			'slnt': -10,
			'style': 'Italic'
		},
		'Casual Bold': {
			'MONO': 1,
			'CASL': 1,
			'wght': 700,
			'slnt': 0,
			'style': 'Bold'
		},
		'Casual Bold Italic': {
			'MONO': 1,
			'CASL': 1,
			'wght': 700,
			'slnt': -10,
			'style': 'Bold Italic'
		},
	},
	# SemiCasual package
	'SemiCasual': {
		'SemiCasual': {
			'MONO': 1,
			'CASL': 0.5,
			'wght': 400,
			'slnt': 0,
			'style': 'Regular'
		},
		'SemiCasual Italic': {
			'MONO': 1,
			'CASL': 0.5,
			'wght': 400,
			'slnt': -10,
			'style': 'Italic'
		},
		'SemiCasual Bold': {
			'MONO': 1,
			'CASL': 0.5,
			'wght': 700,
			'slnt': 0,
			'style': 'Bold'
		},
		'SemiCasual Bold Italic': {
			'MONO': 1,
			'CASL': 0.5,
			'wght': 700,
			'slnt': -10,
			'style': 'Bold Italic'
		},
	},
	# Duotone package
	'Duotone': {
		'Duotone': {
			'MONO': 1,
			'CASL': 0,
			'wght': 400,
			'slnt': 0,
			'style': 'Regular'
		},
		'Duotone Italic': {
			'MONO': 1,
			'CASL': 1,
			'wght': 400,
			'slnt': -10,
			'style': 'Italic'
		},
		'Duotone Bold': {
			'MONO': 1,
			'CASL': 0,
			'wght': 700,
			'slnt': 0,
			'style': 'Bold'
		},
		'Duotone Bold Italic': {
			'MONO': 1,
			'CASL': 1,
			'wght': 700,
			'slnt': -10,
			'style': 'Bold Italic'
		}
	},
}


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

# ----------------------------------------------
# MAIN FUNCTION

oldName = "Recursive"

def splitFont(fontPath, outputDirectory="fonts/rec_mono-for-code", newName="Rec Mono"):

	# access font as TTFont object
	varfont = ttLib.TTFont(fontPath)

	fontFileName = os.path.basename(fontPath)

	for package in instanceValues:
		for instance in instanceValues[package]:

			print(instance)

			instanceFont = instancer.instantiateVariableFont(
						varfont, {"wght": instanceValues[package][instance]['wght'], "CASL": instanceValues[package][instance]['CASL'], "MONO": instanceValues[package][instance]['MONO'], "slnt": instanceValues[package][instance]['slnt']}
					)
		
			# UPDATE NAME ID 6, postscript name
			currentPsName = getFontNameID(instanceFont, 6)
			newPsName = currentPsName.replace('Sans','').replace(oldName, newName.replace(' ','')).replace('LinearLight',instance.replace(' ',''))
			setFontNameID(instanceFont, 6, newPsName)

			# UPDATE NAME ID 4, full font name
			currentFullName = getFontNameID(instanceFont, 4)
			newFullName = currentFullName.replace('Sans','').replace(oldName, newName).replace(' Linear Light',instance)
			setFontNameID(instanceFont, 4, newFullName)

			# UPDATE NAME ID 3, unique font ID
			currentUniqueName = getFontNameID(instanceFont, 3)
			newUniqueName = currentUniqueName.replace('Sans','').replace(oldName, newName.replace(' ','')).replace('LinearLight',instance.replace(' ',''))
			setFontNameID(instanceFont, 3, newUniqueName)

			# ADD name 2, style linking name
			newStyleLinkingName = instanceValues[package][instance]['style']
			setFontNameID(instanceFont, 2, newStyleLinkingName)
			setFontNameID(instanceFont, 17, newStyleLinkingName)

			# UPDATE NAME ID 1, unique font ID
			currentFamName = getFontNameID(instanceFont, 1)
			newFamName = currentFamName.replace(' Sans','').replace(oldName, newName).replace('Linear Light',instance.replace(" " + instanceValues[package][instance]['style'],''))
			setFontNameID(instanceFont, 1, newFamName)
			setFontNameID(instanceFont, 16, newFamName)



			# TODO: remove version number from filename?

			newFileName = fontFileName.replace(oldName,newName.replace(' ','')).replace('_VF_','-'+instance.replace(' ','')+'-')
			outputSubDir = f"{outputDirectory}/{package}"

			# make dir for new fonts
			pathlib.Path(outputSubDir).mkdir(parents=True, exist_ok=True) 

			instanceFont.save(f"{outputSubDir}/{newFileName}")

	import shutil
	shutil.make_archive(f"{outputDirectory}", 'zip', outputDirectory)
	shutil.move(f"{outputDirectory}.zip",f"{outputDirectory}/{outputDirectory.split('/')[-1]}.zip")



if __name__ == '__main__':
	fire.Fire(splitFont)