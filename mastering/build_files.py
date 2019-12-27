import os
import shutil
from fontTools.designspaceLib import DesignSpaceDocument
from prep_fonts import prep, copyFiles
from build_variable import makeSTAT
from build_static import buildFolders, buildNameMap, buildFontMenuDB, buildInstances


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


def makeSources(ds, src, designspacePath):
    # Copy files from src/masters, as we need to edit them
    ignore = shutil.ignore_patterns(".git",
                                    ".git*",
                                    )
    print("🏗  Copying files")

    dsPath = os.path.join("../src/masters", ds)
    copyFiles(dsPath, src)

    # Copy features
    shutil.copytree("../src/features/features", os.path.join(src, "features"),
                    ignore=ignore)
    shutil.copy("../src/features/features.fea",
                os.path.join(src, 'features.fea'))

    prep(designspacePath)


def buildFeatures(src):
    ufos = getFiles(src, "ufo")
    feature = os.path.join(src, "features.fea")
    for ufo in ufos:
        shutil.copy(feature, ufo)
    print("🏗  Moved features into UFOs")


def buildFiles(sources=False,
               static=True,
               variable=False,
               ds="recursive-MONO_CASL_wght_slnt_ital--full_gsub.designspace"):

    print("🚚  Building files for mastering")

    root = os.path.join(os.getcwd(), "build")
    static_root = os.path.join(root, "static")
    var_root = os.path.join(root, "var")
    src = os.path.join(root, "src")
    designspacePath = os.path.join(src, ds)

    if sources:
        print("\n🚚  Generating sources")
        if os.path.exists(root):
            shutil.rmtree(root)

        os.mkdir(root)
        os.mkdir(static_root)
        os.mkdir(var_root)

        makeSources(ds, src, designspacePath)

    ds = DesignSpaceDocument.fromfile(designspacePath)

    if static:
        print("\n🚚  Making files for static font mastering")

        name_map = buildNameMap()
        buildFolders(ds, static_root, name_map)
        buildFontMenuDB(ds, static_root, name_map)
        buildInstances(designspacePath, static_root, name_map)

    if variable:
        print("\n🚚  Making files for varible font mastering")
        # Make STAT table source
        makeSTAT(var_root, ds)
        buildFeatures(src)



if __name__ == "__main__":
    buildFiles()
