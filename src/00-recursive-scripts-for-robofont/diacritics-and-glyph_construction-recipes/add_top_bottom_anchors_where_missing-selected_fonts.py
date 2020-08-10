"""
    A script to quickly add top & bottom anchors to basic Latin alphabet, if not already present.

    Made to run on Recursive as of commit 7dfdca77 (with basically a full character set).

    TODO:
    - caps: attach anchor `top` in x=center, at y=711
    - caps: attach anchor `bottom` in x=center, at y=0

    - lowercase: attach anchor `top` in x=center, at y=xheight+11
    - ascenders: attach anchor `top` in x=center, at y=ascender-20 # and just fix manually? :(
    - lowercase: attach anchor `bottom` in x=center, at y=-1
    - descenders: attach anchor `bottom` in x=center, at y=descender (?)

    questions:
    - will this work for slanted masters?

    to fix manually:
    - [ ] F, bottom
    - [ ] b, d, f
    - [ ] j, q
    - [x] (add ringbelow)
"""

from vanilla.dialogs import *
from mojo.UI import OutputWindow

uppercase = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z L.sans Z.sans".split()

# also check for .italic, .sans, .mono alternates...

lowercaseXheight = [char for char in "acemnorsuvwxz"] +"a.italic c.italic e.italic m.italic n.italic r.italic s.italic u.italic v.italic w.italic x.italic z.italic r.mono".split()

# add to ... highest/lowest points in glyphs?
ascenders = "b d f h l b.italic d.italic f.italic h.italic k.italic l.italic f.mono l.mono l.sans".split()
descenders = "g p q y f.italic g.italic y.italic g.mono".split()

ij = "i j i.italic j.italic i.mono".split()



OutputWindow().show()
OutputWindow().clear()
files = getFile("Select files to build glyphs in", allowsMultipleSelection=True, fileTypes=["ufo"])

def addMissingAnchors(font):
    print("\n\n-----------------------------------------------")
    print(font.info.styleName)

    for char in uppercase:
        g = font[char]
        if 'top' not in [a.name for a in g.anchors]:
            print("\n")
            print(g, g.anchors)

            # stupid way to align top anchor with bottom
            if char is "K":
                xPos = [anchor.x for anchor in font["K"].anchors if anchor.name == "bottom"][0]
                g.appendAnchor("top", (xPos, font.info.capHeight + 11))

            else:
                g.appendAnchor("top", (g.width/2, font.info.capHeight + 11))


            print("- Anchor 'top' added")

        if 'bottom' not in [a.name for a in g.anchors]:
            print("\n")
            print(g, g.anchors)
            g.appendAnchor("bottom", (g.width/2, 0))
            print("- Anchor 'bottom' added")

    # add top to lowercase at x-height
    for char in lowercaseXheight+descenders:
        g = font[char]
        if 'top' not in [a.name for a in g.anchors]:
            print("\n")
            print(g, g.anchors)
            g.appendAnchor("top", (g.width/2, font.info.xHeight + 11))
            print("- Anchor 'top' added")

    # add top to ascenders
    for char in ascenders:
        g = font[char]
        if 'top' not in [a.name for a in g.anchors]:
            print("\n")
            print(g, g.anchors)
            g.appendAnchor("top", (g.width/2, font.info.ascender - 20))
            print("- Anchor 'top' added")

    # add bottom to lowercase at baseline
    for char in lowercaseXheight+ascenders:
        g = font[char]
        if 'bottom' not in [a.name for a in g.anchors]:
            print("\n")
            print(g, g.anchors)

            if char is "f.italic":
                g.appendAnchor("bottom", (g.width/2, g.bounds[1] - 1))
            else:
                g.appendAnchor("bottom", (g.width/2, -1))

            print("- Anchor 'bottom' added")


    # add bottom to descenders
    for char in descenders:
        g = font[char]
        if 'bottom' not in [a.name for a in g.anchors]:
            print("\n")
            print(g, g.anchors)
            g.appendAnchor("bottom", (g.width/2, g.bounds[1] - 1)) # at min Y of glyph
            print("- Anchor 'bottom' added")

    # add bottom to ij
    for char in ij:
        g = font[char]
        if 'bottom' not in [a.name for a in g.anchors]:
            print("\n")
            print(g, g.anchors)
            g.appendAnchor("bottom", (g.width/2, g.bounds[1] - 1)) # at min Y of glyph
            print("- Anchor 'bottom' added")


# find suffixes needed for recipeGlyphs
for file in files:
    font = OpenFont(file, showInterface=False)

    addMissingAnchors(font)

    font.save()

    font.close()