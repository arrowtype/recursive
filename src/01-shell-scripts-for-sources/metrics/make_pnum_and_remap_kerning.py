"""
    Goals:
    - Make set of .pnum figures
    - Map kerning currently used for default figures to the pnum
    - Remove kerning from default figures

    Approach:
    1. Duplicate the figures as component glyphs with .pnum suffix (skip /one, because /one.sans exists)
    2. Update all references in kerning, adding .pnum suffix to any number names
    3. Remove kerning references to /one (there are several)

    # TODO? : deal with glyph names that get two periods, e.g. zero.sans.pnum

    # TODO: also make one.sans_tnum, with:
    https://github.com/arrowtype/recursive/blob/e84c1bcd9cd077e724b33f70d8215d8314a5c038/src/01-shell-scripts-for-sources/glyphs/decompose-and-copy-one_sans_tnum.py
"""

import os
from fontParts.world import OpenFont

monoDir = "src/ufo/mono"
sansDir = "src/ufo/sans"

# /one is intentionally excluded (one.sans already exists)
numbers = "zero two three four five six seven eight nine six.ss01 nine.ss01 zero.slash zero.dotted zero.sans".split(" ")

# get source UFO paths
ufoPaths = [os.path.join(monoDir, path) for path in os.listdir(monoDir) if ".ufo" in path] + [os.path.join(sansDir, path) for path in os.listdir(sansDir) if ".ufo" in path]

for fontPath in ufoPaths:
    print(fontPath)
    f = OpenFont(fontPath, showInterface=False)

    for number in numbers:
        newName = number + ".pnum"

        if newName not in f.keys():
            f.newGlyph(newName)

            glyphToCopyTo = f[newName].getLayer("foreground")

            # get the point pen of the layer glyph
            penForNewGlyph = glyphToCopyTo.getPointPen()
            # draw the points of the imported glyph into the layered glyph
            f[number].drawPoints(penForNewGlyph)

            glyphToCopyTo.markColor = (1, 1, 0, 0.5)

            # make width
            glyphToCopyTo.width = f[number].width

            f.save()

        # update glyph names in groups
        for groupName, members in f.groups.items():

            # if a default number is a group
            if number in members:
                # get members, remove the default number and add the pnum
                groupMembers = [member for member in members]
                groupMembers.remove(number)

                newGroupMembers = groupMembers + [f'{number}.pnum']

                # delete the group
                del f.groups[groupName]

                print(newGroupMembers)

                # make new group with adjusted members
                f.groups[groupName] = newGroupMembers

        # update glyph names in kerns
        for kern in f.kerning.items():
            # if default number is on either side
            if number in kern[0]:
                # make a temp kern data, updating number names
                newKern = ((kern[0][0].replace(number,f'{number}.pnum'),kern[0][1].replace(number,f'{number}.pnum')),kern[1])

                # delete old kern
                del f.kerning[kern[0]]

                # add in new kern data
                f.kerning[newKern[0]] = newKern[1]
    
    f.save()
