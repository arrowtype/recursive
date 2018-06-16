
glyphsToRename = {
    "uni0300":          "gravecomb",
    "uni0301":          "acutecomb",
    "uni0302":          "circumflexcomb",
    "uni0303":          "tildecomb",
    "uni0304":          "macroncomb",
    "uni0306":          "brevecomb",
    "uni0307":          "dotaccentcomb",
    "uni0308":          "dieresiscomb",
    "uni030A":          "ringcomb",
    "uni030B":          "hungarumlautcomb",
    "uni030C":          "caroncomb",
    "uni0312":          "commaturnedabovecomb",
    "uni0315":          "commaaboverightcomb",
    "uni0323":          "dotbelowcomb",
    "uni0326":          "commaaccentcomb",
    "uni0327":          "cedillacomb",
    "uni0328":          "ogonekcomb",
    "uni0300.case":     "gravecomb.case",
    "uni0301.case":     "acutecomb.case",
    "uni0302.case":     "circumflexcomb.case",
    "uni0303.case":     "tildecomb.case",
    "uni0304.case":     "macroncomb.case",
    "uni0306.case":     "brevecomb.case",
    "uni0307.case":     "dotaccentcomb.case",
    "uni0308.case":     "dieresiscomb.case",
    "uni030A.case":     "ringcomb.case",
    "uni030B.case":     "hungarumlautcomb.case",
    "uni030C.case":     "caroncomb.case",
    "uni0312.case":     "commaturnedabovecomb.case",
    "uni0315.case":     "commaaboverightcomb.case",
    "uni0323.case":     "dotbelowcomb.case",
    "uni0326.case":     "commaaccentcomb.case",
    "uni0327.case":     "cedillacomb.case",
    "uni0328.case":     "ogonekcomb.case"
}

af = AllFonts()
cf = CurrentFont()

for f in af:
    for g in f:
        if g.name in glyphsToRename:
            g.name = glyphsToRename.get(g.name)