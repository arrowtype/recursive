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
    stylespacePath = os.path.join(var_root, "Recursive.stylespace")

    paths = {"root": root,
             "static:": static_root,
             "cff": cff_root,
             "ttf": ttf_root,
             "var": var_root,
             "src": src,
             "designspace": designspacePath,
             "stylespace": stylespacePath
             }

    return paths


def makeSources(ds, src, designspacePath, version):
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

    prep(designspacePath, version)
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

        makeSources(ds, paths["src"], paths["designspace"], version)

    ds = DesignSpaceDocument.fromfile(paths["designspace"])

    if static:
        print("\n🚚 Making files for static font mastering")

        name_map = buildNameMap()
        print(name_map)
        buildFolders(ds, paths["CFF"], name_map)
        buildFontMenuDB(ds, paths["CFF"], name_map)
        buildGlyphOrderAndAlias(ds.sources[0].path, paths["CFF"])
        buildFamilyFeatures(paths["CFF"],
                            os.path.join(paths["src"], 'features.fea'),
                            version)
        buildInstances(paths["designspace"], paths["CFF"], name_map)

    if variable:
        print("\n🚚 Making files for varible font mastering")
        # Make STAT table source
        makeSTAT(paths["stylespace"], ds)

    return paths


if __name__ == "__main__":
    buildFiles()
