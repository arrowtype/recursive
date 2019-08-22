import os
from ufoProcessor import build as upBuild

# Helper functions
def getFiles(path, extension):
    """
    Walks down all directories starting at *path* looking for files
    ending with *extension*. Knows that UFOs are directories and stops
    the walk for any found UFO.
    """
    if not extension.startswith('.'):
        extension = '.' + extension
    if extension == '.ufo':
        return [dir for (dir, dirs, files) in os.walk(path)
                if dir[-len(extension):] == extension]
    else:
        return [os.sep.join((dir, file)) for (dir, dirs, files)
                in os.walk(path) for file in files if
                file[-len(extension):] == extension]

