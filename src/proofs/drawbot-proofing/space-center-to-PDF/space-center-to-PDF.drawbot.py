'''SpaceCenter to multipage PDF

With help from @gferreira:
https://forum.robofont.com/topic/658/is-it-possible-to-export-to-from-space-center-to-a-multi-page-or-tall-page-pdf/6
'''

from mojo.UI import CurrentSpaceCenter

# --------
# settings
# --------

pageSize = 'LetterLandscape'
margin = 40

# ------------
# calculations
# ------------

f = CurrentFont()
spaceCenter = CurrentSpaceCenter()

help(spaceCenter)

print(spaceCenter.getPosSize())

size(pageSize)

s = spaceCenter.getPointSize() / f.info.unitsPerEm # scale factor
L = (f.info.unitsPerEm + f.info.descender) * s # first line shift

w = width()  - margin * 2
h = height() - margin * 2
x = margin
y = height() - margin - L

# ----------
# make pages
# ----------

translate(x, y)
scale(s)
X, Y = 0, 0 

for gr in spaceCenter.glyphRecords:

    # linebreak
    if (X + gr.glyph.width) * s > w:
        X = 0
        Y -= f.info.unitsPerEm * (1 + spaceCenter.getLineHeight() / 800)

    # pagebreak
    if (abs(Y * s) + L) > h:
        newPage(pageSize)
        translate(x, y)
        scale(s)
        X, Y = 0, 0 

    with savedState():
        translate(X, Y)
        drawGlyph(gr.glyph)

    X += gr.glyph.width