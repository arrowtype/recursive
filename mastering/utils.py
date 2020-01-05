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

    *path* is the path to split
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
    Makes WOFF2 files from list of paths.

    *files* is a `list` of file paths as `string`
    *destination* is a `string` of the destination to save the WOFF files.
    """
    from fontTools.ttLib import woff2
    from fontTools.ttx import makeOutputFileName

    if not os.path.exists(destination):
        os.mkdir(destination)

    print("🏗  Making WOFF & WOFF2")
    for i, file in enumerate(files):
        outfilename = makeOutputFileName(file,
                                         outputDir=destination,
                                         extension='.woff2')
        if os.path.exists(outfilename):
            os.remove(outfilename)

        woff2.compress(file, outfilename)


def batchCheckOutlines(root):
    from afdko.checkoutlinesufo import run as checkoutlinesufo
    from contextlib import redirect_stdout, redirect_stderr
    import re

    files = getFiles(root, "ufo")

    skips = ["uni000D has no contours\n",
             "uniE0A0 has no contours\n", ]

    outputFile = os.path.join(root, "checkoutlines.txt")
    if os.path.exists(outputFile):
        os.remove(outputFile)

    print("🏗  Running checkoutlinesUFO on files")
    printProgressBar(0, len(files), prefix='  ', suffix='Complete', length=50)
    for i, file in enumerate(files):
        with open(outputFile, "a") as f:
            with redirect_stdout(f), redirect_stderr(f):
                print(f"Checking {file}")
                checkoutlinesufo([file, "--all"])
                print("\n\n")
        printProgressBar(i + 1, len(files), prefix='  ',
                         suffix='Complete', length=50)

    log = []
    with open(outputFile, "r") as f:
        for line in f:
            if not line.startswith("Checking"):
                pass1 = re.sub(r'[\.]{2,}', '', line)
                pass2 = re.sub(r' Flat curve at \([0-9,\.]+, [0-9,\.]+\)\.',
                               '', pass1)
                if len(pass2.split()) > 1:
                    if pass2 not in skips:
                        log.append(pass2)
            elif line.startswith("Checking"):
                log.append("\n\n" + line)

    with open(outputFile, "w") as f:
        f.write("".join(log))


if __name__ == "__main__":

    import argparse
    description = "Two helper tools"
    parser = argparse.ArgumentParser(description=description)
    group = parser.add_mutually_exclusive_group()
    parser.add_argument("directory", help="Directory of files to work on")
    group.add_argument("-w", "--woff", action="store_true",
                       help="Make WOFF & WOFF2 files from fonts in directory")
    group.add_argument("-c", "--checkoutlines", action="store_true",
                       help="Run checkoutlines on all UFOs in directory")

    args = parser.parse_args()

    if args.woff:
        out = os.path.join(args.directory, "WOFF")
        ttfs = getFiles(args.directory, 'ttf')
        otfs = getFiles(args.directory, 'otf')
        fonts = ttfs + otfs
        print(fonts)
        if len(fonts) != 0:
            makeWOFF(fonts, out)
        else:
            print("No otfs or ttfs to make WOFFs from")

    if args.checkoutlines:
        batchCheckOutlines(args.directory)
