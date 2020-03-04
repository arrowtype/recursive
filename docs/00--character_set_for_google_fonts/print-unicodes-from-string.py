"""
	Prints unicodes values from a string, to make it easy to add those glyphs to a UFO in RoboFont or GlyphsApp.

	USAGE:

	Update "string" variable. Then run in RoboFont or on the command line:

	python3 <put_filepath_here>/print-unicodes-from-string.py
"""

import unicodedata

string = 'ƆƎƐƔƖƘƛƩƬƭƲƳƴƷƸƹǝǤǥȠȢȣɁɂɊɋɑɓɔɛɣɩɪɬʃʈʊ'

unicodes = [f"uni{'%04x' % ord(c)}" for c in string]

print(" ".join(set(unicodes)))
