import os
from build_files import buildFiles, getFolders
from build_variable import build_variable
from build_static import build_static
from utils import getFiles, makeWOFF

if __name__ == "__main__":
    import argparse
    description = """Font builder for Recursive"""
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("-v", "--version",
                        help="Version for the fonts")
    parser.add_argument("-o", "--out",
                        help="Directory for final fonts")
    parser.add_argument("-a", "--all", action="store_true",
                        help="Build all (source files, variable, static fonts, & WOFF")
    parser.add_argument("-f", "--files", action="store_true",
                        help="Build source files for mastering")
    parser.add_argument("-v", "--variable", action="store_true",
                        help="Build variable font")
    parser.add_argument("-s", "--static", action="store_true",
                        help="Build static fonts")
    parser.add_argument("-w", "--woff", action="store_true",
                        help="Make WOFF & WOFF2 of generated fonts")

    args = parser.parse_args()

    if args.version:
        version = args.version
    else:
        version = "0.000"

    if args.out:
        out = args.out
    else:
        out = os.path.join("..", os.getcwd(), f"fonts_{version}")

    if args.all:
        files = buildFiles(version=version)

        var_out = os.path.join(out, "Variable_TTF")
        build_variable(designspacePath=files["designspace"]
                       stylespacePath=files["stylespace"],
                       out=out)
        build_static(files["cff"], files["ttf"], out)

        ttf = getFiles(out, "ttf")
        otfs = getFiles(out, "otf")
        fonts = ttfs + otfs
        makeWOFF(fonts, os.path.join(out, "WOFFS"))

    else:
        if args.files:
            files = buildFiles(version=version)
        else:
            files = getFolders()

        if args.variable:
            var_out = os.path.join(out, "Variable_TTF")
            build_variable(designspacePath=files["designspace"]
                           stylespacePath=files["stylespace"],
                           out=out)

        if args.static:
            build_static(files["cff"], files["ttf"], out)

        if args.woff:
            ttf = getFiles(out, "ttf")
            otfs = getFiles(out, "otf")
            fonts = ttfs + otfs
            makeWOFF(fonts, os.path.join(out, "WOFFS"))
