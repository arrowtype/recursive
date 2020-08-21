"""
    Set global guides, to help with alignment of superior/inferior figures.
"""

from mojo.UI import setDefault


f = CurrentFont()

def clearGuides(g):
    for guide in g.guidelines:
        g.removeGuideline(guide)

# if the glyph already has a bunch of guides clear them and set default guides to be unlocked; otherwise, add them
def clearExistingGuides(glyphName):
    g = f[glyphName]
    if len(g.guidelines) > 5:
        clearGuides(g)
        # set to False to unlock guidelines
        setDefault("glyphViewLockGuides", False)

    else:
        clearGuides(g)
        setDefault("glyphViewLockGuides", True)


def addHorizontalGuidelines(glyphName, *args):
    clearExistingGuides(glyphName)

    for yPos in args:
        print(yPos)
        f[glyphName].appendGuideline((0, yPos), 0)

    print(f"added guidelines to {glyphName} at Y values:")
    print(f"\t {args}")


def setTinyFigGuides(roundFig="eightsuperior"):

    try:
        suffix = roundFig.split(".")[1]
    except IndexError:
        suffix = ""

    tinyFigs = "onesuperior twosuperior threesuperior zerosuperior foursuperior \
        fivesuperior sixsuperior sevensuperior eightsuperior ninesuperior \
        zeroinferior oneinferior twoinferior threeinferior fourinferior \
        fiveinferior sixinferior seveninferior eightinferior nineinferior".split()

    altTinyFigs = "sixsuperior.ss01 ninesuperior.ss01 sixinferior.ss01 nineinferior.ss01 \
        zerosuperior.slash zeroinferior.slash zerosuperior.dotted zeroinferior.dotted \
        zerosuperior.sans zeroinferior.sans".split()

    # get round figure maxY, minY
    minY = f[roundFig].bounds[1]
    maxY = f[roundFig].bounds[3]
    minYflat = minY + 10
    maxYflat = maxY - 10

    # reflect along middle of cap-height
    lowMinY = 0 - (maxY - f.info.capHeight)
    lowMaxY = f.info.capHeight - minY
    lowMinYflat = lowMinY + 10
    lowMaxYflat = lowMaxY - 10

    for name in tinyFigs:
        if suffix == "":
            addHorizontalGuidelines(name, minY, maxY, minYflat, maxYflat, lowMinY, lowMaxY, lowMinYflat, lowMaxYflat)
        if suffix == "afrc":
            name = name + "." + suffix
            addHorizontalGuidelines(name, minY, maxY, minYflat, maxYflat, lowMinY, lowMaxY, lowMinYflat, lowMaxYflat)
        else:
            try:
                name = name + suffix
                addHorizontalGuidelines(name, minY, maxY, minYflat, maxYflat, lowMinY, lowMaxY, lowMinYflat, lowMaxYflat)
            except KeyError:
                print(f"{name + suffix} not in font")

    for name in altTinyFigs:
        # if eightsuperior
        if suffix == "":
            addHorizontalGuidelines(name, minY, maxY, minYflat, maxYflat, lowMinY, lowMaxY, lowMinYflat, lowMaxYflat)
        # if eightsuperior.afrc and alt is sixsuperior.ss01
        else:
            print(suffix)
            name = name.replace(".","") + "." + suffix
            addHorizontalGuidelines(name, minY, maxY, minYflat, maxYflat, lowMinY, lowMaxY, lowMinYflat, lowMaxYflat)


setTinyFigGuides("eightsuperior")
setTinyFigGuides("eightsuperior.afrc")
