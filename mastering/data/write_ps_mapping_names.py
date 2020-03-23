# Read designspace file, write ps and style map names
# Instance names come from this spreadsheet:
# https://docs.google.com/spreadsheets/d/1vo9R9Xjt_FmNEE7VHzuvkhQ1KHRR9s-0drIZcmhW7ew
# Exported as CSV
import csv
from fontTools.designspaceLib import DesignSpaceDocument

names = {}
with open('instance_names.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        names[(row["Var Instance Family Name"],
               row["Var Instance Style Name"])] = (row["Var postscript"],
                                                   row["Var familymap"],
                                                   row["stylemap"])

doc = DesignSpaceDocument()
doc.read("../../src/masters/recursive-MONO_CASL_wght_ital_CRSV--full_gsub.designspace")
for i in doc.instances:
    k = (i.familyName, i.styleName)
    ps, fm, sm = names[k]
    i.postScriptFontName = ps
    i.styleMapFamilyName = fm
    i.styleMapStyleName = sm

# Because re-writing the designspace removes all the comments, we save
# a new one out to the data folder, then copy/paste into the working
# designSpace file. Yes, this is dumb, but is the better solution to
# save all the comments and formatting (for better git diffs) in the
# working designSpace file.
doc.write("../../src/masters/recursive-MONO_CASL_wght_ital_CRSV--full_gsub_ps_names.designspace")
