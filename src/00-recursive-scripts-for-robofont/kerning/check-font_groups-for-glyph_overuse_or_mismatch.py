import sys
import plistlib
from fontParts.world import OpenFont, RFont, RGlyph
import os

groupsPath = sys.argv[1]
# ufoPath = sys.argv[2]

# glyphsInGroups = {}
# glyphsInUFOforeground = []

# with open(groupsPath, 'r') as file:
#     for line in file:
#         if 'string' in line:
#             line = line.replace('\t','').replace('\n','').replace('<string>','').replace('</string>','')
#             if line not in glyphsInGroups.keys():
#                 glyphsInGroups[line] = 1
#             else:
#                 glyphsInGroups[line] += 1

# font = OpenFont(ufoPath, showInterface=False)

# for glyphName in glyphsInGroups.keys():
#     if glyphName not in font.layers[0].keys():
#         print(glyphName)

# print(font.layers[0].keys())

# ## check quantities
# for key, value in glyphsInGroups.items():
#     if value > 2:
#         print(key, value)

## check keys in plist

glyphsInGroups = []

groupsDict = plistlib.readPlist(os.getcwd() + '/' + groupsPath)
for key in groupsDict.keys():
    print(key)
    for val in groupsDict[key]:
        glyphsInGroups.append(val)

for glyphName in set(glyphsInGroups):
    if glyphsInGroups.count(glyphName) > 1:
        print(glyphName, glyphsInGroups.count(glyphName))