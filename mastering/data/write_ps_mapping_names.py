# Read designspace file, write ps and style map names
import csv
from fontTools.designspaceLib import DesignSpaceDocument

names = {}
with open('instance_names.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        names[(row["Family Name"], row["Style Name"])] = (row["postscript"], row["familymap"], row["stylemap"])

doc = DesignSpaceDocument()
doc.read("../../src/masters/recursive-prop_xprn_weight_slnt_ital.designspace")
for i in doc.instances:
    k = (i.familyName, i.styleName)
    ps, styleFamily, styleStyle = names[k]
    i.postScriptFontName = ps
    i.styleMapFamilyName = styleFamily
    i.styleMapStyleName = styleStyle


doc.write("recursive-prop_xprn_weight_slnt_ital.designspace")