import os
import shutil
from fontTools.designspaceLib import DesignSpaceDocument
from prep_fonts import prep, copyFiles
from build_variable import makeSTAT, buildFeatures
from build_static import (buildFolders,
                          buildNameMap,
                          buildFontMenuDB,
                          buildInstances,
                          buildGlyphOrderAndAlias,
                          buildFamilyFeatures)


def getFolders(ds):
    """
    Makes path strings for all the paths needed.

    Returns a dictionary of paths.

    *ds* is the designspace file.
    """

    root = os.path.join(os.getcwd(), "build")
    static_root = os.path.join(root, "static")
    cff_root = os.path.join(static_root, "CFF")
    ttf_root = os.path.join(static_root, "TTF")
    var_root = os.path.join(root, "var")
    src = os.path.join(root, "src")
    designspacePath = os.path.join(src, ds)

    paths = {"root": root,
             "static": static_root,
             "cff": cff_root,
             "ttf": ttf_root,
             "var": var_root,
             "src": src,
             "designspace": designspacePath,
             }

    return paths


def makeSources(ds, src, version):
    """
    Generates the source files from the working src files

    We don't want to use the working files as this will prep the files
    for making all the fonts, so it has to subset and change things that one
    wants to keep in the design files.

    *ds* file name of the working source designspace file
    *src* is path to the mastering source directory
    *version* is the version number to set the fonts to
    """
    # Copy files from src/ufo, as we need to edit them
    ignore = shutil.ignore_patterns(".git",
                                    ".git*",
                                    )
    print("🏗  Copying files")

    dsPath = os.path.join("../src/ufo", ds)
    copyFiles(dsPath, src)

    # Copy features
    shutil.copytree("../src/features/features", os.path.join(src, "features"),
                    ignore=ignore)
    shutil.copy("../src/features/features.fea",
                os.path.join(src, 'features.fea'))

    prep(os.path.join(src, ds), version)
    buildFeatures(src)


def buildFiles(sources=True,
               static=True,
               variable=True,
               ds="recursive-MONO_CASL_wght_slnt_ital--full_gsub.designspace",
               version="0.000"):

    print("🚚 Building files for mastering")

    paths = getFolders(ds)

    if sources:
        print("\n🚚 Generating sources")
        if os.path.exists(paths["root"]):
            shutil.rmtree(paths["root"])

        os.mkdir(paths["root"])
        os.mkdir(paths["static"])
        os.mkdir(paths["var"])

        makeSources(ds, paths["src"], version)

    ds = DesignSpaceDocument.fromfile(paths["designspace"])

    if static:
        print("\n🚚 Making files for static font mastering")

        name_map = buildNameMap()
        buildFolders(ds, paths["cff"], name_map)
        buildFontMenuDB(ds, paths["cff"], name_map)
        buildGlyphOrderAndAlias(ds.sources[0].path, paths["cff"])
        buildFamilyFeatures(paths["cff"],
                            os.path.join(paths["src"], 'features.fea'),
                            version)
        buildInstances(paths["designspace"], paths["cff"], name_map)

    return paths


if __name__ == "__main__":
    buildFiles()
