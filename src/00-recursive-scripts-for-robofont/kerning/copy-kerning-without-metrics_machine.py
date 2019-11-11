'''
    Usage:

    python "<path>/copy-kerning-without-metrics_machine.py" "<path>/Recursive Sans-Casual B.ufo"

    Required argument: UFO path to copy kerning & groups from

    Assumptions: 
        - You have a single group of UFOs
        - The UFO path you feed in contains both groups.plist and kerning.plist
        - You wish to exactly copy groups.plist from the UFO path to all other UFOs in the same directory
        - You wish to exactly copy kerning.plist from the UFO path to all other UFOs in the same directory with 'Sans' in their filepath
'''

import sys
import os
import shutil 

try:
    ufoToCopyFrom = sys.argv[1]
except IndexError:
    print("At least one arg required: path of UFO to copy from")



try:
    if sys.argv[2]:
        print("Copying from UFO to UFOs in another Directory")
        dirToCopyTo = sys.argv[2]
        ufosToCopyTo = next(os.walk(dirToCopyTo))[1]
except IndexError:
    print("Copying from UFO to UFOs in the same Directory")
    head, tail = os.path.split(ufoToCopyFrom)

ufosToCopyTo = next(os.walk(head))[1]

groupsPath = f"{ufoToCopyFrom}/groups.plist"
kerningPath = f"{ufoToCopyFrom}/kerning.plist"

for ufo in sorted(ufosToCopyTo):
    ufoPath = f"{head}/{ufo}"

    if ufoPath != ufoToCopyFrom:
        print(ufoPath)
        groupsDest = f"{ufoPath}/groups.plist"
        # good if mono or sans
        shutil.copyfile(groupsPath, groupsDest)
        # only copy kerning file for sans UFOs
        if 'Sans' in ufo:
            kerningDest = f"{ufoPath}/kerning.plist"
            shutil.copyfile(kerningPath, kerningDest)
