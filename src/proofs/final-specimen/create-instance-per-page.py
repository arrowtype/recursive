from fontTools import ttLib
from fontTools.varLib import instancer
import os
import shutil
import fire

axes = {
	## move on all axes
	# 'mono': (1, 0),
	# 'casl': (0, 1),
	# 'wght': (300, 1000),
	# 'slnt': (0, -15)
	## sans linear to mono casual
	'mono': (0, 1),
	'casl': (0, 1),
	'wght': (400, 400),
	'slnt': (0, 0)
	## mono casual to sans linear
	# 'mono': (1, 0),
	# 'casl': (1, 0),
	# 'wght': (400, 400),
	# 'slnt': (0, 0)
	# 'ital': (0, 1), # intentionally left out
}

def interpolate(a, b, t):
	distance = b-a
	return(a + distance * t)

def setFontNameID(font, ID, newName, platformID=3, platEncID=1, langID=0x409):
    oldName = font['name'].getName(ID, platformID, platEncID)
    font['name'].setName(newName, ID, platformID, platEncID, langID)
    print(f"\t• name {ID}:  \t {str(oldName).ljust(30, ' ')} \t → {str(newName).ljust(20, ' ')}")

def splitFont(splits=10, fontPath="fonts_1.031/Variable_TTF/Recursive_VF_1.031.ttf", outputDirectoryyyy="recursive-split", run=False):
	"""
		Use to split Recursive VF into an arbitrary number of instances, so that each style is slightly different from the previous one.

		USAGE: On the command line, install dependencies with a virtual environment and pip, then run a command like:
		
		python src/proofs/final-specimen/create-instance-per-page.py -f fonts_1.031/Variable_TTF/Recursive_VF_1.031.ttf -s 57 -r

		Outputs to "recursive-split" directory by default.
	"""

	report = ""

	if run:
		if os.path.exists(outputDirectoryyyy):
			shutil.rmtree(outputDirectoryyyy)
		if not os.path.exists(outputDirectoryyyy):
			os.makedirs(outputDirectoryyyy)	

	varfont = ttLib.TTFont(fontPath)

	for split in range(0,splits):
		t = split / (splits -1)
		mono = round(interpolate(axes['mono'][0], axes['mono'][1], t), 2)
		casl = round(interpolate(axes['casl'][0], axes['casl'][1], t), 2)
		wght = round(interpolate(axes['wght'][0], axes['wght'][1], t), 2)
		slnt = round(interpolate(axes['slnt'][0], axes['slnt'][1], t), 2)
		ital = 0.5

		pageNum = str(split + 1).rjust(2, '0')
		monoVal = "{:.2f}".format(mono).rjust(7, ' ')
		caslVal = "{:.2f}".format(casl).rjust(7, ' ')
		wghtVal = "{:.2f}".format(wght).rjust(7, ' ')
		slntVal = "{:.2f}".format(slnt).rjust(7, ' ')
		italVal = "{:.2f}".format(ital).rjust(7, ' ')

		output = f"page {pageNum} | MONO: {monoVal}, CASL: {caslVal}, wght: {wghtVal}, slnt: {slntVal}, ital: {italVal}"
		print("\n", output)
		report += output + "\n"

		# actually create the instance
		if run:

			instance = instancer.instantiateVariableFont(
				varfont, {"wght": wght, "CASL": casl, "MONO": mono, "slnt": slnt}
			)

			# give instance page-based style name
			setFontNameID(instance, 1, f"Recursive {splits}p")
			setFontNameID(instance, 3, f"1.031;ARRW;RecVarSplit-split{pageNum}")
			setFontNameID(instance, 4, f"Recursive {splits}p")
			setFontNameID(instance, 6, f"RecVarSplit-split{pageNum}")
			setFontNameID(instance, 16, f"Recursive {splits}p")
			setFontNameID(instance, 17, f"Split_{pageNum}")

			# save custom instance
			instance.save(f"{outputDirectoryyyy}/recursive-split--page_{pageNum}--MONO{mono}_CASL{casl}_wght{wght}_slnt{slnt}.ttf")

	if run:
		with open(f"{outputDirectoryyyy}/font-split-report.txt", "w") as file:  
			file.write(report)

	if not run:
		print("\n\tINFO: This was a dry run to preview output. To generate fonts, please add argument --run or -r\n\n")

# also make text file with outputs?

if __name__ == '__main__':
	fire.Fire(splitFont)
