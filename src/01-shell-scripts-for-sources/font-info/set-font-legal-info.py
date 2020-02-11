# setting vertical metrics in Recursive

'''
	Sets legal info in fonts to conform to Google Fonts expectations.

	USAGE:

	python <path>/set-font-legal-info.py <UFOs-dir> <--save>
'''

import sys
import os
import subprocess
from fontParts.world import *
import defcon

# get font dir
try:
	if sys.argv[1]:
		print("Getting UFO paths")
		dirToUpdate = sys.argv[1]
		subDirs = next(os.walk(dirToUpdate))[1]
		ufosToAdjust = [ path for path in subDirs if path.endswith(".ufo")]

		head = dirToUpdate

except IndexError:
	print("Please include directory containing UFOs")

# check whether to save new results
save = False
try:
	if sys.argv[2] == "-s" or sys.argv[2] == "--save" :
		print("Saving new vertical metrics to fonts")
		save = True

except IndexError:
	print("Dry run. Add second arg of --save or -s to save new vertical metrics.")

# run program
for ufo in sorted(ufosToAdjust):
	ufoPath = f"{head}/{ufo}"

	# font = defcon.Font(ufoPath)
	font = OpenFont(ufoPath, showInterface=False)


	print('--------------------------------------------------------')
	print(font.info.styleName)


	font.info.openTypeNameLicense = "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: http://scripts.sil.org/OFL"

	print(font.info.openTypeNameLicense)


	if save:
		font.update()
		font.save()

	subprocess.run(['ufonormalizer', ufoPath, '--no-mod-times'])
