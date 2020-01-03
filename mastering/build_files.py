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
                          buildFamilyFeatures,
                          buildTTFfiles)


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


def buildFiles(sources=False,
               static=True,
               variable=True,
               ds="recursive-MONO_CASL_wght_slnt_ital--full_gsub.designspace",
               version="1.001"):

    print("🚚 Building files for mastering")

    root = os.path.join(os.getcwd(), "build")
    static_root = os.path.join(root, "static")
    cff_root = os.path.join(static_root, "CFF")
    ttf_root = os.path.join(static_root, "TTF")
    var_root = os.path.join(root, "var")
    src = os.path.join(root, "src")
    designspacePath = os.path.join(src, ds)

    paths = {"root": root,
             "static:": static_root,
             "cff": cff_root,
             "ttf": ttf_root,
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

        makeSources(ds, src, designspacePath, version)

    ds = DesignSpaceDocument.fromfile(designspacePath)

    if static:
        print("\n🚚 Making files for static font mastering")

        name_map = buildNameMap()
        buildFolders(ds, cff_root, name_map)
        buildFontMenuDB(ds, cff_root, name_map)
        buildGlyphOrderAndAlias(ds.sources[0].path, cff_root)
        buildFamilyFeatures(cff_root,
                            os.path.join(src, 'features.fea'),
                            version)
        buildInstances(designspacePath, cff_root, name_map)
        buildTTFfiles(cff_root, ttf_root)

    if variable:
        print("\n🚚 Making files for varible font mastering")
        # Make STAT table source
        paths["stylespace"] = makeSTAT(var_root, ds)

    return paths


if __name__ == "__main__":
    buildFiles()
