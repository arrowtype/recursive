'''
    Usage:

    python "<path>/copy-kerning-without-metrics_machine.py" "<path>/Recursive Sans-Casual B.ufo" <dir/to/copy/to>

    Required argument: Feature file to copy

    Optional argument: Dir path of UFOs to copy to, if separate

    Assumptions: 
        - You have a single group of UFOs
        - You wish to exactly copy the features.fea from the features path to all other UFOs in the specified directory
'''

import sys
import os
import shutil 

try:
    feaToCopy = sys.argv[1]
    print(feaToCopy)
except IndexError:
    print("At least one arg required: path of feature file to copy")

try:
    if sys.argv[2]:
        dirToCopyTo = sys.argv[2]
        print(f"Copying feature file to UFOs in {dirToCopyTo}")
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
