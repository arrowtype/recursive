import os
import shutil
from fontTools.designspaceLib import DesignSpaceDocument
from prep_fonts import prep, copyFiles
from build_variable import makeSTAT
from build_static import (buildFolders,
                          buildNameMap,
                          buildFontMenuDB,
                          buildInstances,
                          buildGlyphOrderAndAlias,
                          buildFamilyFeatures)
from utils import getFiles


def buildFeatures(src):
    ufos = getFiles(src, "ufo")
    feature = os.path.join(src, "features.fea")
    for ufo in ufos:
        shutil.copy(feature, ufo)
    print("🏗  Moved features into UFOs")


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
    buildFeatures(src)


def buildFiles(sources=False,
               static=False,
               variable=True,
               ds="recursive-MONO_CASL_wght_slnt_ital--full_gsub.designspace",
               version=1.001):

    print("🚚 Building files for mastering")

    root = os.path.join(os.getcwd(), "build")
    static_root = os.path.join(root, "static")
    var_root = os.path.join(root, "var")
    src = os.path.join(root, "src")
    designspacePath = os.path.join(src, ds)

    paths = {"root": root,
             "static:": static_root,
             "var": var_root,
             "src": src,
             "designspace": designspacePath,
             }

    if sources:
        print("\n🚚 Generating sources")
        if os.path.exists(root):
            shutil.rmtree(root)

        os.mkdir(root)
        os.mkdir(static_root)
        os.mkdir(var_root)

        makeSources(ds, src, designspacePath)

    ds = DesignSpaceDocument.fromfile(designspacePath)

    if static:
        print("\n🚚 Making files for static font mastering")

        name_map = buildNameMap()
        buildFolders(ds, static_root, name_map)
        buildFontMenuDB(ds, static_root, name_map)
        buildGlyphOrderAndAlias(ds.sources[0].path, static_root)
        buildFamilyFeatures(static_root,
                            os.path.join(src, 'features.fea'),
                            version)
        buildInstances(designspacePath, static_root, name_map)

    if variable:
        print("\n🚚 Making files for varible font mastering")
        # Make STAT table source
        paths["stylespace"] = makeSTAT(var_root, ds)

    return paths


if __name__ == "__main__":
    buildFiles()
