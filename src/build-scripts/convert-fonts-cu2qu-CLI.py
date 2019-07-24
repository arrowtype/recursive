'''
 First, install dependencies in requirements.txt.
 
 Then, use this script like this:
 python src/build-scripts/convert-fonts-cu2qu-CLI.py <directory path>
'''

import sys
import glob
from defcon import Font
from cu2qu.ufo import fonts_to_quadratic

directory = sys.argv[1]

print(directory)

fonts = []

for filepath in glob.iglob(f'{directory}/*.ufo'):
    print(filepath)
    fonts.append(Font(str(filepath)))

print(fonts)

stats = {}
print(fonts_to_quadratic(fonts, stats=stats, dump_stats=True))
