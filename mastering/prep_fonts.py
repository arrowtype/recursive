import os
import shutil
import datetime
from fontParts.fontshell import RFont as Font
from fontTools import agl
from designspaceProblems import DesignSpaceChecker
from fontTools.designspaceLib import DesignSpaceDocument

# A re-write of Varfont Prep (https://github.com/arrowtype/varfont-prep)
# for the commandline. This just does what is needed to get the Recursive
# Sources in line for making variable fonts.


report = {}


def removeGlyphs(font, names):
    """
    Removes the glyphs in the list of *names* from the supplied *font*.
    This checks all layers for the glyph, removes the glyph from any
    composite glyphs that use it, removes the glyph from the `glyphOrder`,
    and removes the glyph from the kerning.

    *font* is a font object (Defcon or FontParts)
    *names* is a `list` of glyph names
    """

    for name in names:
        for layer in font.layers:
            if name in layer.keys():
                layer.removeGlyph(name)

    for glyph in font:
        if glyph.components:
            for component in glyph.components:
                if component.baseGlyph in names:
                    glyph.removeComponent(component)

    glyphOrder = font.glyphOrder
    for name in glyphOrder:
        if name in names:
            glyphOrder.remove(name)
    font.glyphOrder = glyphOrder

    for left, right in font.kerning.keys():
        if left in names or right in names:
            del font.kerning[(left, right)]


def copyFiles(designspacePath, outRoot):
    """
    Copies the supplied designspace and all of it's sources to *outRoot*

    This updates the source paths in the the designspace file.

    *designspacePath* is a `string` of the path to a designspace file
    *outRoot* is a `string` of the root directory to copy files to
    """

    ignore = shutil.ignore_patterns(".git", ".git*")

    if os.path.exists(outRoot):
        print("🛑 new folder path exists, stopping")
        raise ValueError
    os.mkdir(outRoot)

    newDesignspacePath = os.path.join(outRoot,
                                      os.path.split(designspacePath)[1])

    shutil.copy(designspacePath, newDesignspacePath)

    ds = DesignSpaceDocument.fromfile(designspacePath)
    sources = [source.path for source in ds.sources]
    paths = {}
    for fontPath in sources:
        f = os.path.split(fontPath)[1]
        newPath = os.path.join(outRoot, f)
        paths[f] = newPath
        shutil.copytree(fontPath, newPath, ignore=ignore)

    ds = DesignSpaceDocument.fromfile(newDesignspacePath)
    for source in ds.sources:
        source.path = paths[os.path.split(source.path)[1]]
    ds.write(newDesignspacePath)

    return newDesignspacePath


def writeReport(path):
    """
    Writes out the report text file from the report dictionary to
    the given *path*.

    *path* is a `string` of the path to write to
    """

    seperator = "\n_________________________"

    final_report = [seperator, "Cleared guidelines in:"]
    if report["Clear Guidelines"]:
        for font, glyphs in report["Clear Guidelines"]:
            final_report.append(f"\t{font}")
            if glyphs:
                final_report.append(f"\t\tAnd these glyphs: {' '.join(glyphs)}")
    else:
        final_report.append("None! No guidelines to remove")

    final_report.append(seperator)
    final_report.append("Decomposed and removed these non-exporting glyphs:")
    if report["Non-exporting glyphs"]:
        for font, glyphs in report["Non-exporting glyphs"]:
            final_report.append(f"\t{font}")
            final_report.append(f"\t\t{', '.join(glyphs)}")
    else:
        final_report.append("None! No glyphs to remove")

    final_report.append(seperator)
    final_report.append("Removed these glyphs that were not common to all sources:")
    if report["Removed Glyphs"]:
        for font, glyphs in report["Removed Glyphs"]:
            final_report.append(f"\t{font}")
            final_report.append(f"\t\t{', '.join(glyphs)}")
    else:
        final_report.append("None! No glyphs to remove")

    final_report.append(seperator)
    final_report.append("Removed these non-compatible glyphs:")
    if report["Removed non-compatible glyphs"]:
        for glyph, reason in report["Removed non-compatible glyphs"]:
            final_report.append(f"\t{glyph} because:")
            final_report.append(f"\t\t{reason}")
    else:
        final_report.append("None! No glyphs to remove")

    final_report.append(seperator)
    final_report.append("Added blank kerning to these fonts:")
    if report["Added blank kerning"]:
        for font in report["Added blank kerning"]:
            final_report.append(f"\t{font}")
    else:
        final_report.append("None! All fonts had kerning.")

    final_report.append(seperator)
    final_report.append("Reported designspace problems from DesignspaceProblems:")
    if report["Designspace check"]:
        for problem in report["Designspace check"]:
            final_report.append(str(problem))
    else:
        final_report.append("No reported problems!")

    with open(path, "w") as writer:
        writer.write("\n".join(final_report))


def checkFamilyName(fonts):
    """
    Checks that all the sources for a designspace have the same family name.

    Returns `True` if so, prints an error and returns `False` if not.

    *fonts* is a `list` of font objects (Defcon or FontParts).
    """

    familyName = []
    for font in fonts:
        if font.info.familyName not in familyName:
            familyName.append(font.info.familyName)

    if len(familyName) != 1:
        print("🛑 source UFOs have different family names, stopping")
        print(f"{', '.join(familyName)}")
        return False
    else:
        return True


def clearGuides(font):
    """
    Clears both font level and glyph level guides in a font.

    *font* is a font object (Defcon or FontParts)
    """

    local_report = report.get("Clear Guidelines", [])
    font.clearGuidelines()
    clearedGlyphs = []

    for glyph in font:
        if glyph.guidelines:
            glyph.clearGuidelines()
            clearedGlyphs.append(glyph.name)

    local_report.append((font.info.familyName + " " + font.info.styleName,
                         clearedGlyphs))
    report["Clear Guidelines"] = local_report


def makeSourceFontsGlyphCompatible(fonts):
    """
    Compares the glyphs of all *fonts* and removes glyphs that are not
    common to all the provided *fonts*.

    *fonts* is a `list` of font objects (Defcon or FontParts).
    """

    local_report = report.get("Removed Glyphs", [])

    # Get a list of all glyphs in each font
    glyphSets = [font.keys() for font in fonts]

    # Use set intersection to get all common glyph from each list
    commonGlyphs = set.intersection(*map(set, glyphSets))

    for font in fonts:
        removed = []
        for name in font.keys():
            if name not in commonGlyphs:
                removed.append(name)
        if len(removed) != 0:
            removeGlyphs(font, removed)
            local_report.append((font.info.familyName + " " + font.info.styleName,
                                 removed))
    report["Removed Glyphs"] = local_report


def decomposeNonExportingGlyphs(fonts):
    """
    Looks for any glyph that has a name starting with '_' (underscore) that
    is used as a component. Decomposes these components, then removes the
    glyph(s) from the font.

    *fonts* is a `list` of font objects (Defcon or FontParts).
    """

    local_report = report.get("Non-exporting glyphs", [])
    for font in fonts:
        non_exporting = []
        for glyph in font:
            if glyph.components:
                for component in glyph.components:
                    if component.baseGlyph in non_exporting:
                        component.decompose()
                    elif component.baseGlyph[0] == "_":
                        non_exporting.append(component.baseGlyph)
                        component.decompose()
        removeGlyphs(font, non_exporting)
        local_report.append((font.info.familyName + " " + font.info.styleName, non_exporting))
    report["Non-exporting glyphs"] = local_report


def sortGlyphOrder(fonts):
    """
    Sorts all fonts in the list of *fonts* to have a common sort order.

    *fonts* is a `list` of font objects (Defcon or FontParts).
    """
    for font in fonts:
        newGlyphOrder = font.naked().unicodeData.sortGlyphNames(font.glyphOrder, sortDescriptors=[dict(type="cannedDesign", ascending=True, allowPseudoUnicode=True)])

        # Trick here to put the .notdef first, as the cannedDesign sort puts it
        # last, and it must be the first glyph in a font.
        newGlyphOrder.insert(0, newGlyphOrder.pop())
        font.glyphOrder = newGlyphOrder


def checkName(name, mapping):
    """
    Helper function that takes in a glyph name and a mapping of glyph
    names to final (production) names and returns a production name for
    the provided glyph name.

    For example, given the mapping:
    {'florin': 'uni0192', }

    florin.tl will be transformed to uni0192.tl
    florin.simple.tl will be transformed to uni0192.simple_tl
    florin will be transformed to uni0192
    a will be returned as a

    *name* is a `string` of the glyph name
    *mapping* is a `dictionary` of glyph name to final names, both `string`s
    """

    if len(name.split('.')) == 2:
        n, ext = name.split('.')
        if n in mapping.keys():
            return f"{mapping[n]}.{ext}"
        else:
            return name
    elif len(name.split('.')) > 2:
        r = name.split('.')
        n = check_name(r[0], mapping)
        return f"{n}.{'_'.join(r[1:])}"
    else:
        if name in mapping.keys():
            return mapping[name]
        else:
            return name


def setVersion(fonts, version):
    """
    Sets the `versionMajor` and `versionMinor` for a `list` of fonts.

    *fonts* is a `list` of font objects (Defcon or FontParts).
    *version* is a `string` of the version number for the fonts
    """

    if len(version.split(".")) > 2:
        raise ValueError

    version = version.split(".")
    versionMajor = int(version[0])
    try:
        versionMinor = int(version[1])
    except IndexError:
        versionMinor = 0

    for font in fonts:
        font.info.versionMajor = versionMajor
        font.info.versionMinor = versionMinor


def setProductionNames(fonts):
    """
    Sets the `public.postscriptNames` for a `list` of fonts.

    *fonts* is a `list` of font objects (Defcon or FontParts).
    """

    mapping = {
               'florin': 'uni0192',
               'f_f': 'f_f',
               'f_f_i': 'f_f_i',
               'f_f_l': 'f_f_l',
               }
    names = []

    for font in fonts:
        for glyph in font:
            added = False
            if glyph.name not in mapping.keys():
                if len(glyph.unicodes) == 1:
                    if glyph.name not in agl.AGL2UV.keys():
                        mapping[glyph.name] = f"uni{glyph.unicode:04X}"
                        added = True
            if not added and glyph.name not in names:
                names.append(glyph.name)

    for name in names:
        if name in agl.AGL2UV.keys():
            mapping[name] = name
        else:
            prod_name = checkName(name, mapping)
            mapping[name] = prod_name

    for font in fonts:
        font.lib["public.postscriptNames"] = mapping


def kerningCompatibility(fonts):
    """
    Adds dummy kerning to a font that has no kerning.

    *fonts* is a `list` of font objects (Defcon or FontParts).
    """

    local_report = report.get("Added blank kerning", [])

    for font in fonts:
        if len(font.kerning) == 0:
            font.kerning[("A", "A")] = 0
            local_report.append(font.info.familyName + " " + font.info.styleName)
    report["Added blank kerning"] = local_report


def makeCompatible(fonts):
    """
    Checks all glyphs in *fonts* for compatibility. Removes any glyphs that
    aren't compatible from all of the fonts.

    *fonts* is a `list` of font objects (Defcon or FontParts).
    """

    local_report = report.get("Removed non-compatible glyphs", [])
    nonCompatible = []

    for glyph in fonts[0]:
        for font in fonts[1:]:
            if glyph.name in font.keys():
                compatibility = glyph.isCompatible(font[glyph.name])
                if not compatibility[0]:
                    nonCompatible.append((glyph.name, str(compatibility)))
            else:
                nonCompatible.append((glyph.name, "Missing in font"))

    for font in fonts:
        removeGlyphs(font, [name for name, _ in nonCompatible])

    if nonCompatible != []:
        local_report.append(nonCompatible)
    report["Removed non-compatible glyphs"] = local_report


def prep(designspacePath, version):
    """
    Runs all of the checks and corrections and generates the report.

    Uses https://github.com/LettError/DesignspaceProblems to check and
    report on issues with the design space.

    *designspacePath* is a `string` of the path to the designspace file
    *version* is a `string` that is the version to set the font to
    """

    # Checking to see if there are any large issues with the designspace
    # file before doing anything
    dsc = DesignSpaceChecker(designspacePath)
    assert not dsc.hasStructuralProblems()

    ds = DesignSpaceDocument.fromfile(designspacePath)
    sources = [source.path for source in ds.sources]

    print("🏗  Opening sources")
    fonts = [Font(path) for path in sources]

    print("🏗  Checking family name")
    assert checkFamilyName(fonts)

    print("🏗  Removing non-exporting glyphs")
    decomposeNonExportingGlyphs(fonts)

    print("🏗  Clearing guides")
    for font in fonts:
        clearGuides(font)

    print("🏗  Removing glyphs that aren't in every font")
    makeSourceFontsGlyphCompatible(fonts)

    print("🏗  Removing non-compatible glyphs")
    makeCompatible(fonts)

    print("🏗  Making kerning compatible")
    kerningCompatibility(fonts)

    print("🏗  Sorting glyph order to be common")
    sortGlyphOrder(fonts)

    print("🏗  Setting production names")
    setProductionNames(fonts)

    if version:
        print("🏗  Setting version")
        setVersion(fonts, version)

    print("🏗  Closing and saving sources")
    for font in fonts:
        font.close(save=True)

    print("🏗  Checking full design space")
    dsc.checkEverything()
    report["Designspace check"] = dsc.problems

    print("🏗  Writing report")
    report_path = os.path.join(os.path.split(designspacePath)[0],
                               "varfontprep-report.txt")
    writeReport(report_path)

    print("✅ Done preparing sources")


if __name__ == "__main__":

    import argparse
    description = """
    Prepares the sources of a designspace for building a variable font.

    By default it makes a copy of the designspace and sources, so your
    working files are never overwritten. This may be overridden.
    """
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("designspacePath",
                        help="The path to a designspace file")
    parser.add_argument("-o", "--overwrite", action="store_true",
                        help="Overwrite source files in place.")
    parser.add_argument("-v", "--version",
                        help="Version to set in files")
    args = parser.parse_args()
    designspacePath = args.designspacePath

    if not args.overwrite:
        print("🏗  Copying files")

        ds = DesignSpaceDocument.fromfile(designspacePath)
        font = Font(ds.sources[0].path)
        fn = font.info.familyName.replace(" ", "_").lower()
        font.close()

        now = datetime.datetime.now()
        fn += "-varfontprep-" + now.strftime("%Y_%m_%d-%H_%M_%S")

        directory, file = os.path.split(designspacePath)
        root = os.path.join(directory, fn)

        designspacePath = copyFiles(designspacePath, root)

    prep(designspacePath, args.version)
