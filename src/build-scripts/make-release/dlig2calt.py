"""
	A script to change dlig features to calt features, 
	to make code ligatures on by default in Rec Mono for Code.
"""

from fontTools import ttLib
import fire

def dlig2calt(fontPath, inplace=False):
	font = ttLib.TTFont(fontPath)

	featureRecords = font['GSUB'].table.FeatureList.FeatureRecord

	for fea in featureRecords:
		if fea.FeatureTag == 'dlig':
			fea.FeatureTag = 'calt'
			print('Updated feature "dlig" to be "calt".')

	if inplace:
		font.save(fontPath)
		print("Saved font inplace with feature 'dlig' changed to 'calt'.")
	else:
		newPath = fontPath.replace('.ttf','.calt_ligs.ttf')
		font.save(newPath)
		print("Saved font with feature 'dlig' changed to 'calt' at ", newPath)


if __name__ == '__main__':
	fire.Fire(dlig2calt)