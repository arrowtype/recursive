import sys
from fontParts.world import OpenFont, RFont, RGlyph

groupsPath = sys.argv[1]
ufoPath = sys.argv[2]

glyphsInGroups = {}
glyphsInUFOforeground = []

with open(groupsPath, 'r') as file:
    for line in file:
        if 'string' in line:
            line = line.replace('\t','').replace('\n','').replace('<string>','').replace('</string>','')
            if line not in glyphsInGroups.keys():
                glyphsInGroups[line] = 1
            else:
                glyphsInGroups[line] += 1

font = OpenFont(ufoPath, showInterface=False)

for glyphName in glyphsInGroups.keys():
    if glyphName not in font.layers[0].keys():
        print(glyphName)

print(font.layers[0].keys())

## check quantities
for key, value in glyphsInGroups.items():
    if value > 2:
        print(key, value)
