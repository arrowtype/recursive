# Sets a all open fonts to the Google standard for vertical metrics
# See https://github.com/googlefonts/gf-docs/tree/master/VerticalMetrics
# for the specification.
#
# To be run inside of RoboFont.


def find_min_max(fonts):
    """
    Iterates through all glyphs of the given fonts and finds the max and min
    bounding boxes for the set of fonts. Returns the min and max values.
    """
    min = 0
    max = 0

    for font in fonts:
        for glyph in font:
            if glyph.bounds is not None:
                if glyph.bounds[1] < min:
                    min = glyph.bounds[1]
                if glyph.bounds[3] > max:
                    max = glyph.bounds[3]

    return min, max


def find_typo_values(fonts):
    """
    Looks at all standard single accented captial letters (see list) to find
    the tallest value for the hheaAscender and typoAscender values. Likewise,
    looks at all lowercase letters that descend (see list) to find the value
    for hheaDescender and typoDescender. Returns the descender and ascender
    values.
    """

    ascender = ['Agrave', 'Aacute', 'Acircumflex', 'Atilde', 'Adieresis',
                'Aring', 'Amacron', 'Abreve', 'Cacute', 'Ccircumflex',
                'Cdotaccent', 'Ccaron', 'Dcaron', 'Egrave', 'Eacute',
                'Ecircumflex', 'Edieresis', 'Emacron', 'Ebreve', 'Edotaccent',
                'Eogonek', 'Ecaron', 'Etilde', 'Gcircumflex', 'Gbreve',
                'Gdotaccent', 'Gcaron', 'Hcircumflex', 'Igrave', 'Iacute',
                'Icircumflex', 'Idieresis', 'Itilde', 'Imacron', 'Ibreve',
                'Idotaccent', 'Jcircumflex', 'Lacute', 'Ntilde', 'Nacute',
                'Ncaron', 'Ograve', 'Oacute', 'Ocircumflex', 'Otilde',
                'Odieresis', 'Omacron', 'Obreve', 'Ohungarumlaut', 'Racute',
                'Rcaron', 'Sacute', 'Scircumflex', 'Scaron', 'Tcaron',
                'Ugrave', 'Uacute', 'Ucircumflex', 'Udieresis', 'Utilde',
                'Umacron', 'Ubreve', 'Uring', 'Uhungarumlaut', 'Wcircumflex',
                'Wgrave', 'Wacute', 'Wdieresis', 'Yacute', 'Ycircumflex',
                'Ydieresis', 'Ymacron', 'Ygrave', 'Ytilde', 'Zacute',
                'Zdotaccent', 'Zcaron', 'AEacute']
    descender = ['g', 'q', 'p', 'y', 'j']
    asc = 0
    dsc = 0
    for font in fonts:
        for name in ascender:
            if name in font.keys():
                glyph = font[name]
                if glyph.bounds[3] > asc:
                    asc = glyph.bounds[3]
        for name in descender:
            if name in font.keys():
                glyph = font[name]
                if glyph.bounds[1] < dsc:
                    dsc = glyph.bounds[1]
    return dsc, asc


def set_vertical_metrics(fonts, max, min, asc, dsc):
    """
    Sets the vertical metrics and the USE_TYPO_VALUES bit in all the
    open fonts.

    Saves and closes each font when it is finished.
    """

    print('Setting fonts to:')
    print('winAscent: ' + str(max))
    print('winDescent: ' + str(abs(min)))
    print('typoAscender & hheaAscender: ' + str(asc))
    print('typoDescender & hheaDescender: ' + str(dsc))
    print('typoLineGap & hheaLineGap: 0')
    for font in fonts:
        font.info.openTypeHheaAscender = asc
        font.info.openTypeHheaDescender = dsc
        font.info.openTypeHheaLineGap = 0
        font.info.openTypeOS2TypoAscender = asc
        font.info.openTypeOS2TypoDescender = dsc
        font.info.openTypeOS2TypoLineGap = 0
        font.info.openTypeOS2WinAscent = max
        font.info.openTypeOS2WinDescent = abs(min)
        if font.info.openTypeOS2Selection is None or 7 not in font.info.openTypeOS2Selection:
            if font.info.openTypeOS2Selection is None:
                font.info.openTypeOS2Selection = [7]
            else:
                font.info.openTypeOS2Selection.append(7)
        font.save()
        font.close()


fonts = AllFonts()
min, max = find_min_max(fonts)
dsc, asc = find_typo_values(fonts)
set_vertical_metrics(fonts, max, min, asc, dsc)
