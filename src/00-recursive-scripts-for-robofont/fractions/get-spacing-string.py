"""
    Script to make a well-organized spacing string to deal with sups/infs in Recursive.

    There is certainly a faster way to sort this list, but I just need the list now.
"""

# all glyphs with "superior" or "inferior" in their name
l = ['zeroinferiordotted.afrc', 'sixsuperior.ss01', 'foursuperior', 'ninesuperior.ss01', 'zeroinferiorsans.afrc', 'fourinferior', 'nineinferior.ss01', 'foursuperior.afrc', 'zeroinferior.afrc', 'sevensuperior.afrc', 'eightsuperior', 'onesuperior.afrc', 'nineinferior.afrc', 'fivesuperior', 'eightinferior.afrc', 'twosuperior', 'zeroinferiorslash.afrc', 'twoinferior.afrc', 'onesuperior', 'sixsuperior', 'sixinferiorss01.afrc', 'zerosuperior.dotted', 'zeroinferior.dotted', 'zerosuperiorsans.afrc', 'sixinferior.afrc', 'zerosuperior.sans', 'fourinferior.afrc', 'oneinferior.afrc', 'seveninferior.afrc', 'threesuperior', 'sixinferior', 'sixinferior.ss01', 'zeroinferior.sans', 'zerosuperiorslash.afrc', 'oneinferior', 'sixsuperiorss01.afrc', 'eightsuperior.afrc', 'twosuperior.afrc', 'ninesuperior', 'sixsuperior.afrc', 'ninesuperiorss01.afrc', 'fiveinferior', 'zerosuperior.slash', 'zerosuperior', 'fivesuperior.afrc', 'eightinferior', 'ninesuperior.afrc', 'nineinferiorss01.afrc', 'zeroinferior.slash', 'threeinferior.afrc', 'twoinferior', 'zerosuperiordotted.afrc', 'zerosuperior.afrc', 'seveninferior', 'threeinferior', 'nineinferior', 'threesuperior.afrc', 'zeroinferior', 'fiveinferior.afrc', 'sevensuperior']

# sort list
sortedList = []

sups = [] 

for name in l:
    if "superior" in name:
        sups.append(name)

for name in sups:
    if "afrc" not in name and "ss01" not in name:
        sortedList.append(name)
        # sortedString += f"{name} "

for name in sups:
    if "afrc" not in name and "ss01" in name:
        sortedList.append(name)

for name in sups:
    if "afrc" in name and "ss01" not in name:
        sortedList.append(name)

for name in sups:
    if "afrc" in name and "ss01" in name:
        sortedList.append(name)

infs = []

for name in l:
    if "superior" not in name:
        infs.append(name)

for name in infs:
    if "afrc" not in name and "ss01" not in name:
        sortedList.append(name)
        # sortedString += f"{name} "

for name in infs:
    if "afrc" not in name and "ss01" in name:
        sortedList.append(name)

for name in infs:
    if "afrc" in name and "ss01" not in name:
        sortedList.append(name)

for name in infs:
    if "afrc" in name and "ss01" in name:
        sortedList.append(name)


# print(sortedList)

# make spacing string

s = ""

for i, n in enumerate(sortedList):
    if i % 6 == 0 and i != 0:
        s += "\\n"
    s += f"/{n} "

print(s)