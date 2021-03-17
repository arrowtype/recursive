"""
    The FontTools Subsetter expects unicode ranges for *inclusion*, but 
    often you just know which ranges you want to *exclude* from a font subset.

    So, this script will accept a font, then report what Unicode values 
    it includes *beyond* given Unicode ranges.

    USAGE:

    python compute-remaining-unicodes-in-font.py <font> --unicodes <unicode-ranges>

    Or see usage information at:

    python compute-remaining-unicodes-in-font.py --help
"""

from fontTools.ttLib import TTFont


def listUnicodeRanges(unicodeRanges):
    # remove "U+"" from ranges
    unicodeRanges = unicodeRanges.replace("U+", "").replace(" ", "")

    # create set
    unicodesIncluded = set()

    # split up separate ranges by commas
    for unicodeChunk in unicodeRanges.split(","):
        # if it's a range...
        if "-" in unicodeChunk:
            # get start and end of range
            start, end = unicodeChunk.split("-")
            # go through range and add each value to the set
            for unicodeInteger in range(int(start, 16), int(end, 16) + 1):
                unicodesIncluded.add(unicodeInteger)
        # if it's a single unicode...
        else:
            unicodesIncluded.add(int(unicodeChunk, 16))

    return unicodesIncluded


def main():
    # get arguments from argparse
    args = parser.parse_args()

    # open font at TTFont object
    ttfont = TTFont(str(args.fontPath[0]))

    # get set of unicode ints in font
    rangeInFont = {x for x in ttfont["cmap"].getBestCmap()}

    # get unicode values for ranges given in arg
    unicodesGiven = listUnicodeRanges(args.unicodes)

    # Find unicodes in the font which aren’t listed, but are in the font
    unicodesRemaining = {intUnicode for intUnicode in rangeInFont if intUnicode not in unicodesGiven}

    # convert to hex, then join in comma-separated string
    unicodesRemaining = [hex(n) for n in unicodesRemaining]
    unicodesRemaining = [str(hex).replace("0x", "U+").upper() for hex in unicodesRemaining]
    unicodesRemaining = ",".join(unicodesRemaining)

    print(unicodesRemaining)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Report what Unicode values a font includes *beyond* given Unicode ranges.')
    parser.add_argument('fontPath', 
                        help='Path to a font file',
                        nargs="+")
    parser.add_argument("-u", "--unicodes",
                        default="U+0020-0039, U+003A-005A, U+0061-007A, U+2018-201D, U+005B, U+005D",
                        help='String of unicodes or unicode ranges, comma-separated. Example – a basic Latin set would be "U+0020-0039, U+003A-005A, U+0061-007A, U+2018-201D, U+005B, U+005D"')

    main()