"""
	Some code ligatures have been made, but either have temporary problems or probably shouldn't be built into final fonts.

	This script appends an underscore (_) to the start of glyphs names in selected fonts, which will make them get removed in the mastering prep scripts.
"""

nonExportingGlyphs = """
_arrowhead
parenleft_parenleft.code
bracketleft_bracketleft.code
bracketleft_parenleft.code
braceleft_bracketleft.code
braceleft_parenleft.code
parenright_braceright.code
parenright_bracketright.code
parenright_parenright.code
bracketright_braceright.code
bracketright_bracketright.code
percent_c.code
percent_d.code
percent_g.code
percent_percent.code
percent_r.code
percent_s.code
f_quotesingle.code
""".split()

for name in nonExportingGlyphs:
	print(name)

from vanilla.dialogs import *

inputFonts = getFile("select masters to add non-exporting glyphs to", allowsMultipleSelection=True, fileTypes=["ufo"])
		
for fontPath in inputFonts:
	f = OpenFont(fontPath, showInterface=False)

	f.lib["public.skipExportGlyphs"] = nonExportingGlyphs

	f.save()
	f.close()