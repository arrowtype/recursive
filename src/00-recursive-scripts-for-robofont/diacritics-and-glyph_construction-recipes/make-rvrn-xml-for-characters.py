unicodesToFind = "ȁ ḍ ḏ ṡ ṣ ṥ ṧ ṩ ṹ ṻ ṟ ȑ ȓ ṛ ḯ ḝ ḉ ȅ ȇ ȉ ȋ ȕ ȗ ẏ ẓ ṃ ṅ ṇ ṉ ḡ ḥ".split()

unicodesOrdsToFind = []

for uni in unicodesToFind:
    unicodesOrdsToFind.append(ord(uni))

f = CurrentFont()

glyphUnicodes = {}

for g in f:
    try:
        glyphUnicodes[g.unicodes[0]] = g.name
    except:
        pass

for ordNum in unicodesOrdsToFind:
    if ordNum in glyphUnicodes.keys():
        print(f'<sub name="{glyphUnicodes[ordNum]}" with="{glyphUnicodes[ordNum]}.italic"/>')