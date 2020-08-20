"""
    Check for glyphs with zero-char glyph name lengths.

    https://github.com/arrowtype/recursive/issues/388
"""

from vanilla.dialogs import *
from mojo.UI import OutputWindow

## use if you want to select different files
files = getFile("Select file to check", allowsMultipleSelection=True, fileTypes=["ufo"])

## uncomment if you wish to see output window
OutputWindow().show()
OutputWindow().clear()

for fontPath in files:

    f = OpenFont(fontPath, showInterface=False)

    for g in f:
        if len(g.name) < 1:
            print(f.info.styleName)
            print(g)
            print()

    f.close()
