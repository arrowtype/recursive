'''
    Usage:

    python "<path>/copy-kerning-without-metrics_machine.py" "<path>/Recursive Sans-Casual B.ufo" <dir/to/copy/to>

    Required argument: UFO path to copy kerning & features from

    Optional argument: Dir path of UFOs to copy to, if separate

    Assumptions: 
        - You have a single group of UFOs
        - The UFO path you feed in contains both features.plist and kerning.plist
        - You wish to exactly copy features.plist from the UFO path to all other UFOs in the same directory
        - You wish to exactly copy kerning.plist from the UFO path to all other UFOs in the same directory with 'Sans' in their filepath
'''

import sys
import os
import shutil 

try:
    feaToCopy = sys.argv[1]
except IndexError:
    print("At least one arg required: path of UFO to copy from")

try:
    if sys.argv[2]:
        print("Copying from UFO to UFOs in another Directory")
        dirToCopyTo = sys.argv[2]
        ufosToCopyTo = next(os.walk(dirToCopyTo))[1]

        head = dirToCopyTo
except IndexError:
    print("Oops")

for ufo in sorted(ufosToCopyTo):
    ufoPath = f"{head}/{ufo}"

    print(ufoPath)
    featuresDest = f"{ufoPath}/features.fea"
    # copy feature file and overwrite
    shutil.copyfile(feaToCopy, featuresDest)
