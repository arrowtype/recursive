import os


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


def splitall(path):
    """
    Splits a path into all it's parts, returns a list.
    """
    allparts = []
    while 1:
        parts = os.path.split(path)
        if parts[0] == path:  # sentinel for absolute paths
            allparts.insert(0, parts[0])
            break
        elif parts[1] == path: # sentinel for relative paths
            allparts.insert(0, parts[1])
            break
        else:
            path = parts[0]
            allparts.insert(0, parts[1])
    return allparts


def printProgressBar(iteration, total, prefix='', suffix='',
                     decimals=1, length=100, fill='█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)

    Nabbed, of course, from Stack Overflow
    (https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console)
    """
    percent = ("{0:."+str(decimals)+"f}").format(100*(iteration/float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end='\r')
    # Print New Line on Complete
    if iteration == total:
        print()


def makeWOFF(files, destination):
    """
    Makes WOFF and WOFF2 files from list of paths.
    This uses the highest compression for making WOFF files. It is slow.

    *files* is a `list` of file paths as `string`
    *destination* is a `string` of the destination to save the WOFF files.
    """
    from fontTools.ttLib import TTFont, sfnt
    from fontTools.ttLib.sfnt import WOFFFlavorData
    from fontTools.ttx import makeOutputFileName

    sfnt.USE_ZOPFLI = True
    sfnt.ZLIB_COMPRESSION_LEVEL = 9

    print("🏗  Making WOFF & WOFF2")
    printProgressBar(0, len(files), prefix='  ', suffix='Complete', length=50)
    for i, file in enumerate(files):
        font = TTFont(file, recalcBBoxes=False, recalcTimestamp=False)

        font.flavor = "woff"
        data = WOFFFlavorData()
        data.majorVersion = 1
        data.minorVersion = 0
        font.flavorData = data

        outfilename = makeOutputFileName(file,
                                         outputDir=destination,
                                         extension='.woff')
        font.save(outfilename)

        outfilename = makeOutputFileName(source,
                                         outputDir=destination,
                                         extension='.woff2')
        font.flavor = "woff2"
        font.save(outfilename, reorderTables=False)

        printProgressBar(i + 1, length, prefix='  ',
                         suffix='Complete', length=50)


def batchCheckOutlines(root):
    from afdko.checkoutlinesufo import run as checkoutlinesufo
    from contextlib import redirect_stdout, redirect_stderr
    import re

    regex = re.compile(r'[\.]{2,}')

    files = getFiles(root, "ufo")
    for file in files:
        pass
