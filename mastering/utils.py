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
        elif parts[1] == path:  # sentinel for relative paths
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

    print("🏗  Making WOFF2")
    printProgressBar(0, len(files), prefix='  ', suffix='Complete', length=50)
    for i, file in enumerate(files):
        outfilename = makeOutputFileName(file,
                                         outputDir=destination,
                                         extension='.woff2')
        if os.path.exists(outfilename):
            os.remove(outfilename)

        woff2.compress(file, outfilename)
        printProgressBar(i + 1, len(files), prefix='  ',
                         suffix='Complete', length=50)


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


def make_mark_mkmk_gdef_feature(font):
    from collections import defaultdict
    """
    Takes in a font and builds the mark, mkmk,
    and gdef table in Adobe Feature File syntax.

    *font* is a Defcon like font object.
    """

    # Gather all the data we need
    ligCarets = defaultdict(list)
    mark = defaultdict(list)
    base = defaultdict(list)

    for glyph in font:

        # note, we're rounding (by int()) the anchor positions

        if len(glyph.anchors) > 0:
            # there can be more than one ligCaret in a ligature
            # so need to store them before writing them out
            carets = []

            for a in glyph.anchors:
                # Lig caret marks are named starting
                # caret, so we look for those. Only
                # need the x position for the feature
                if a.name.startswith('caret'):
                    carets.append(int(a.x))

                # if a anchor name starts with a
                # underscore, it's a mark
                elif a.name.startswith("_"):
                    mark[(int(a.x), int(a.y))].append((a.name, glyph.name))

                # if it's not a ligature caret or a mark, it's base
                else:
                    base[(int(a.x), int(a.y))].append((a.name, glyph.name))

            # make a dict of all the same caret positions
            # with the glyph names as values. Streamines
            # the GDEF table
            if carets != []:
                ligCarets[tuple(carets)].append(glyph.name)

    # Now process the data

    # Mark name list
    kinds = list(base.keys())

    # Get a list of all the ligs in the font for GDEF
    ligatures = []
    for names in ligCarets.values():
        ligatures += names
    ligatures.sort()

    #  Sort out the marks
    uc_marks = defaultdict(list)
    lc_marks = defaultdict(list)
    common_marks = defaultdict(list)
    mark_names = []
    mark_glyph_names = []
    uc_marks_names = []

    for pos, data in mark.items():
        _lc_marks = defaultdict(list)
        _uc_marks = defaultdict(list)
        for markName, glyphName in data:
            markName = markName[1:]
            if markName not in mark_names:
                mark_names.append(markName)
            if glyphName not in mark_glyph_names:
                mark_glyph_names.append(glyphName)
            if glyphName.endswith(".case"):
                _uc_marks[markName].append(glyphName)
                uc_marks_names.append(glyphName)
            else:
                _lc_marks[markName].append(glyphName)
        for markName, glyphs in _uc_marks.items():
            uc_marks[markName].append((pos, glyphs))
        for markName, glyphs in _lc_marks.items():
            lc_marks[markName].append((pos, glyphs))

    for markName, data in lc_marks.items():
        newData = []
        for pos, glyphNames in data:
            common = []
            for n in glyphNames:
                if (n + ".case") not in uc_marks_names:
                    common.append(n)
            for i in common:
                glyphNames.remove(i)
            if common != []:
                common_marks[markName].append((pos, common))
            if glyphNames != []:
                newData.append((pos, glyphNames))
        lc_marks[markName] = newData

    mark_names.sort()
    mark_glyph_names.sort()
    uc_marks_names.sort()

    # Collect base info

    # This is a hardcoded list, if marks are added to another UC glyph, this
    # list needs extending. One could do this by looking at all glyphs with
    # anchors anddoing a check of unicode category, but then you have to check
    # for non-encodedglyphs also.
    uc_base_names = ['A', 'AE', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                     'K', 'L', 'L.sans', 'M', 'N', 'O', 'Oslash', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Z.sans']
    uc_bases = defaultdict(list)
    bases = defaultdict(list)
    mkmk_bases = defaultdict(list)
    mkmk_uc_bases = defaultdict(list)
    base_names = []

    for pos, data in base.items():
        _bases = defaultdict(list)
        _uc_bases = defaultdict(list)
        _mkmk_bases = defaultdict(list)
        _mkmk_uc_bases = defaultdict(list)
        for markName, glyphName in data:
            if glyphName not in base_names:
                base_names.append(glyphName)

            if glyphName in uc_base_names and markName in uc_marks.keys():
                _uc_bases[markName].append(glyphName)
            elif glyphName in mark_glyph_names and glyphName.endswith(".case"):
                _mkmk_uc_bases[markName].append(glyphName)
                base_names.remove(glyphName)
            elif glyphName in mark_glyph_names:
                _mkmk_bases[markName].append(glyphName)
                base_names.remove(glyphName)
            else:
                _bases[markName].append(glyphName)

        for markName, glyphs in _uc_bases.items():
            uc_bases[markName].append((pos, glyphs))
        for markName, glyphs in _bases.items():
            bases[markName].append((pos, glyphs))
        for markName, glyphs in _mkmk_bases.items():
            mkmk_bases[markName].append((pos, glyphs))
        for markName, glyphs in _mkmk_uc_bases.items():
            mkmk_uc_bases[markName].append((pos, glyphs))

    base_names.sort()

    # Make features

    classes = ""
    mark_feature = "feature mark {\n"
    mkmk_feature = "feature mkmk {\n"

    for n in mark_names:
        if n in uc_marks.keys():
            for a in uc_marks[n]:
                pos = a[0]
                names = a[1]
                classes += f"markClass [{' '.join(names)}] <anchor {str(pos[0])} {str(pos[1])}> @mark_uc_{n};\n"
            if n in uc_bases:
                mark_feature += f"    lookup mark_uc_{n} {{\n"
                for base in uc_bases[n]:
                    pos = base[0]
                    names = base[1]
                    mark_feature += f"        pos base [{' '.join(names)}] <anchor {str(pos[0])} {str(pos[1])}> mark @mark_uc_{n};\n"
                mark_feature += f"    }} mark_uc_{n};\n"
            if n in mkmk_uc_bases:
                mkmk_feature += f"    lookup mkmk_uc_{n} {{\n"
                for base in mkmk_uc_bases[n]:
                    pos = base[0]
                    names = base[1]
                    mkmk_feature += f"        pos mark [{' '.join(names)}] <anchor {str(pos[0])} {str(pos[1])}> mark @mark_uc_{n};\n"
                mkmk_feature += f"    }} mkmk_uc_{n};\n"
        if n in lc_marks.keys():
            for a in lc_marks[n]:
                pos = a[0]
                names = a[1]
                classes += f"markClass [{' '.join(names)}] <anchor {str(pos[0])} {str(pos[1])}> @mark_lc_{n};\n"
            if n in bases:
                mark_feature += f"    lookup mark_lc_{n} {{\n"
                for base in bases[n]:
                    pos = base[0]
                    names = base[1]
                    mark_feature += f"        pos base [{' '.join(names)}] <anchor {str(pos[0])} {str(pos[1])}> mark @mark_lc_{n};\n"
                mark_feature += f"    }} mark_lc_{n};\n"
            if n in mkmk_bases:
                mkmk_feature += f"    lookup mkmk_lc_{n} {{\n"
                for base in mkmk_bases[n]:
                    pos = base[0]
                    names = base[1]
                    mkmk_feature += f"        pos mark [{' '.join(names)}] <anchor {str(pos[0])} {str(pos[1])}> mark @mark_lc_{n};\n"
                mkmk_feature += f"    }} mkmk_lc_{n};\n"
        if n in common_marks.keys():
            for a in common_marks[n]:
                pos = a[0]
                names = a[1]
                classes += f"markClass [{' '.join(names)}] <anchor {str(pos[0])} {str(pos[1])}> @mark_common_{n};\n"

            # build our common bases for this mark
            common_bases = []
            if n in bases:
                common_bases.append(bases[n])
            if n in uc_bases:
                common_bases.append(uc_bases[n])

            common_mkmk_bases = []
            if n in mkmk_bases:
                if mkmk_bases[n][0][1] != []:
                    common_mkmk_bases.append(mkmk_bases[n])
            if n in mkmk_uc_bases:
                if mkmk_uc_bases[n][0][1] != []:
                    common_mkmk_bases.append(mkmk_uc_bases[n])

            if common_bases != []:
                mark_feature += f"    lookup mark_common_{n} {{\n"
                for c in common_bases:
                    for pos, names in c:
                        mark_feature += f"        pos base [{' '.join(names)}] <anchor {str(pos[0])} {str(pos[1])}> mark @mark_common_{n};\n"
                mark_feature += f"    }} mark_common_{n};\n"

            if common_mkmk_bases != []:
                mkmk_feature += f"    lookup mkmk_common_{n} {{\n"
                for c in common_mkmk_bases:
                    for pos, names in c:
                        mkmk_feature += f"        pos mark [{' '.join(names)}] <anchor {str(pos[0])} {str(pos[1])}> mark @mark_common_{n};\n"
                mkmk_feature += f"    }} mkmk_common_{n};\n"

    mark_feature += "} mark;"
    mkmk_feature += "} mkmk;"

    gdef = f"@BASE  = [{' '.join(base_names)}];\n@MARKS = [{' '.join(mark_glyph_names)}];\n@LIGATURES = [{' '.join(ligatures)}];\n\ntable GDEF {{\n    GlyphClassDef @BASE, @LIGATURES, @MARKS,;\n"

    for k, v in ligCarets.items():
        if len(v) > 1:
            gdef += f"    LigatureCaretByPos [{' '.join(v)}] {' '.join(str(i) for i in k)};\n"
        else:
            gdef += f"    LigatureCaretByPos {' '.join(v)} {' '.join(str(i) for i in k)};\n"
    gdef += "} GDEF;"

    return f'{classes}\n{mark_feature}\n{mkmk_feature}\n{gdef}'


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
