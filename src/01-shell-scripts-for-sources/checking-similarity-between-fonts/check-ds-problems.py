'''
    Check for DesignSpaceProblems:
    python <path>/check-ds-problems.py <designspacePath>

    Requires DesignspaceProblems library:
    pip install git+https://github.com/LettError/DesignspaceProblems.git
'''

import sys
from pprint import pprint
from designspaceProblems import DesignSpaceChecker

designspacePath = sys.argv[1]

dc = DesignSpaceChecker(designspacePath)
dc.checkEverything()

# now all problems are stored in dc.problems
pprint(dc.problems)
