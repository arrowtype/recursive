"""
	Script to find issues of anchors missing names, which have somehow made it into the project. :|
"""



import sys
import os
from fontParts.world import *

try:
	if sys.argv[1]:
		dirToUpdate = sys.argv[1]
		subDirs = next(os.walk(dirToUpdate))[1]
		ufosToCheck = [ path for path in subDirs if path.endswith(".ufo")]
		head = dirToUpdate

except IndexError:
	print("Please include arg: <directory containing UFOs>")

for ufo in sorted(ufosToCheck):
	ufoPath = f"{head}/{ufo}"

	f = OpenFont(ufoPath, showInterface=False)

	for g in f:
		for anchor in g.anchors:
			if anchor.name == None:
				print(f"{(f.info.styleName).ljust(30, ' ')} \t {(g.name).ljust(9, ' ')} \t {anchor}")
				try:
					if sys.argv[2] == "-r" or sys.argv[2] == "--remove" :
						print(f"{anchor} removed!")
						g.removeAnchor(anchor)
						f.save()
				except IndexError:
					pass
	
	f.close()