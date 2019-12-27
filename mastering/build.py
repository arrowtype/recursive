import os
from build_files import buildFiles


if __name__ == "__main__":
    import argparse
    description = """
    Font builder for Recursive
    """
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("-ds", "--designspacePath",
                        help="The path to the src designspace file")
    parser.add_argument("-f", "--files", action="store_true",
                        help="Build source files for mastering")
    parser.add_argument("-v", "--variable", action="store_true",
                        help="Build variable font")
    parser.add_argument("-s", "--static", action="store_true",
                        help="Build static fonts")
    parser.add_argument("-a", "--all", action="store_true",
                        help="Build all (source files, variable, & static fonts")
    args = parser.parse_args()

    if args.designspacePath:
        src = args.designspacePath
        if not os.path.exists(src):

        else:
            print("🛑  designspacePath isn't valid")
    else:

