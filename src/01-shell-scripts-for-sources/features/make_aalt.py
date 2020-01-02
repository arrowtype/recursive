import os
from fontParts.fontshell import RFont as Font


def rotate(l, n):
    """
    Helper method to rotate a list by a certain number of places

    *l* is the `list`
    *n* is the number or rotations
    """
    return l[-n:] + l[:-n]


def build_aalt(font, outPath):
    """
    Builds a aalt feature from a font.
    This relies on standard glyph naming for alts to us the form of:
    <base name>.<alt name>.

    *font* is a font object (Defcon or FontParts)
    *outPath* is the path to save the feature to as a `string`
    """

    alts = {}
    aalt = ['feature aalt {', ]

    for glyph in font:
        if "." in glyph.name:
            split = glyph.name.split(".")[0]
            if split != "":
                if split not in alts:
                    alts[split] = [split, glyph.name]
                else:
                    alt_list = alts[split]
                    if glyph.name not in alt_list:
                        alt_list.append(glyph.name)
                        alts[split] = alt_list

    keys = list(alts.keys())
    keys.sort()

    for name in keys:
        alternates = alts[name]
        glyphs = []
        for name in alternates:
            if name in font.keys():
                glyphs.append(name)
        if len(glyphs) > 1:
            for count, _ in enumerate(glyphs):
                line = rotate(glyphs, count)
                sub = f"    sub {line[0]} from [{' '.join(line)}];"
                aalt.append(sub)

    aalt.append("} aalt;")

    with open(outPath, "w") as f:
        f.write("\n".join(aalt))


if __name__ == "__main__":
    import argparse
    description = "Make a aalt feature from a UFO"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("fontPath",
                        help="The path to a designspace file")
    parser.add_argument("-o", "--out",
                        help="Output path")
    args = parser.parse_args()
    font = Font(args.fontPath)
    outPath = args.out

    if not outPath:
        outPath = os.path.split(args.fontPath)[0] + "aalt.fea"

    build_aalt(font, outPath)
