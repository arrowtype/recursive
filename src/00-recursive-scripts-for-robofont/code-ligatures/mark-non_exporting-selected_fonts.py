"""
	This is a way to quickly set glyphs to not export, without deleting them outright. (In case someone else in the future really wants them.)

	Reasons for glyphs to be here:
	- Some code ligatures have been made, but either have temporary problems or probably shouldn't be built into final fonts.
	- More ligatures were made initially than are actually a good idea in practice. So, fi and ffi are being used in Sans Italic styles, but 
	  ff, fl, and ffl are not.

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
f_f
fl
f_f_l
f_f.italic
f_f_i.italic
f_f_l.italic
fi.italic
fl.italic
f_f.mono
f_f_i.mono
f_f_l.mono
fi.mono
fl.mono
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