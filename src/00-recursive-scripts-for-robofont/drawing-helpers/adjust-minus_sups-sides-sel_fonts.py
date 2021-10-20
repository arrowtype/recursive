"""
    Quick way to adjust the right side or left side of the minus.superior glyph for mono sources
"""

from mojo.UI import GetFile

# get files
files = GetFile("Select files to modify", allowsMultipleSelection=True, fileTypes=["ufo"])

for filpath in files:
    f = OpenFont(filpath, showInterface=False)

    g = f["minus.superior"]
    g.width = 400
    
    for c in g:
        for s in c:
            for p in s:
                if p.x > 250:
                    p.x -= 200
                # if p.x > 300:
                #     p.x -= 60

    g.update()

    f.save()

