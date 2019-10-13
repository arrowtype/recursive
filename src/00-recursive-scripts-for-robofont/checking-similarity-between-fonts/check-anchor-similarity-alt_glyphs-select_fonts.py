from vanilla.dialogs import *
from mojo.UI import AskString
from mojo.UI import OutputWindow
import pprint

relevantSuffixes = "italic mono sans".split()

files = getFile("Select files to check for anchor similarity in default and alt glyphs", allowsMultipleSelection=True, fileTypes=["ufo"])


# fonts = []


OutputWindow().show()
OutputWindow().clear()

def Diff(li1, li2): 
    return (list(set(li1) - set(li2))) 


for file in files:
    font = OpenFont(file, showInterface=False)

    fontName = font.info.familyName + " " + font.info.styleName

    # fonts.append(fontName)
    print('\n\n-------------------------------------------------\n')
    print(fontName, '\n')

    anchors = {}

    for glyph in font:

        # set up base glyph dict entry
        if '.' in glyph.name and \
            glyph.name.split('.')[1] in relevantSuffixes and \
            glyph.name.split('.')[0] not in anchors.keys():
            anchors[glyph.name.split('.')[0]] = {
                'anchorsInBase': [],
                'anchorsInAlts': {}
            }

        # go through alts in font
        if '.' in glyph.name and \
            glyph.name.split('.')[1] in relevantSuffixes:

            # add anchor list to base glyph
            for anchor in font[glyph.name.split('.')[0]].anchors:
                if anchor.name not in anchors[glyph.name.split('.')[0]]['anchorsInBase']:
                    anchors[glyph.name.split('.')[0]]['anchorsInBase'].append(anchor.name)

            # add alt to entry
            if glyph.name not in anchors[glyph.name.split('.')[0]]['anchorsInAlts']:
                anchors[glyph.name.split('.')[0]]['anchorsInAlts'][glyph.name] = []

            # add anchor list to alt
            for anchor in glyph.anchors:
                if anchor.name not in anchors[glyph.name.split('.')[0]]['anchorsInAlts'][glyph.name]:
                    anchors[glyph.name.split('.')[0]]['anchorsInAlts'][glyph.name].append(anchor.name)

        # find if anchorsInAlts don't match anchors in base. If not, print about it

    for baseGlyph in anchors:
        for altGlyph in anchors[baseGlyph]['anchorsInAlts']:
            if len(Diff(anchors[baseGlyph]['anchorsInBase'], anchors[baseGlyph]['anchorsInAlts'][altGlyph])) >= 1:
                print(baseGlyph.ljust(20), sorted(anchors[baseGlyph]['anchorsInBase']))
                print(altGlyph.ljust(20), sorted(anchors[baseGlyph]['anchorsInAlts'][altGlyph]))
                # print(Diff(anchors[baseGlyph]['anchorsInBase'], anchors[baseGlyph]['anchorsInAlts'][altGlyph]))
                print("")

                # TODO: list things not to make alt diacritics of
                    # ydot italic (wouldn't fit)
                    # g.mono top accents (best with flat-top, "sans" form)
                    # should /g vs /g.mono be treated specially (because /g.mono already has an "accent" with its ear)?

    

    # pp = pprint.PrettyPrinter(indent=2, width=200,compact=False)
    # pp.pprint(anchors)

    font.close()

# TODO: should this instead print each glyph, then which fonts have which anchors missing?
