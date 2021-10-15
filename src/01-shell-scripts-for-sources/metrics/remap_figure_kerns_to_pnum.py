"""
    Goals:
    - Make set of .pnum figures
    - Map kerning currently used for default figures to the pnum
    - Remove kerning from default figures

    Maybe....?
    1. Change names of default figures (add .pnum suffixes in a way that updates groups & kerning)
    2. Duplicate new pnum figures as default figures
    3. Restore unicodes to default figures

    No, that’s too complicated in practice. Instead:
    1. Duplicate the figures as component glyphs with .pnum suffix (skip /one, because /one.sans exists)
    2. Update all references in kerning, adding .pnum suffix to any number names
    3. Remove kerning references to /one (there are several)
"""


inputFonts = getFile("select masters to add feature code to", allowsMultipleSelection=True, fileTypes=["ufo"])

# /one is intentionally excluded (one.sans already exists)
numbers = "zero two three four five six seven eight nine".split(" ")

for fontPath in inputFonts:
    f = OpenFont(fontPath, showInterface=False)

    for name in numbers:
        # use robofont’s renameGlyph function, because it’s easy
        f.renameGlyph(oldName=name, newName=f'{name}.sans', renameComponents=True, renameGroups=True, renameKerning=True, renameGlyphOrder=True)

        # maybe clear the new glyphs, then make them using components?
        # we need some way to 