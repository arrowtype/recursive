# /Users/stephennixon/type-repos/recursive/venv/bin/python
# coding=utf8
        

import unicodedata

# this string was pulled from RoboFont Space Center, then edited by hand

u = 'AÀÁÂÃÄÅĀĂĄǺȀȂẠẢẤẦẨẪẬẮẰẲẴẶBCÇĆĈĊČḈDĎḌḎEÈÉÊËĒĔĖĘĚȄȆḔḖḜẸẺẼẾỀỂỄỆFGĜĞĠĢǦḠHĤḤḪIÌÍÎÏĨĪĬĮİȈȊḮỈỊJĴKĶLĹĻĽḶḺMṂNÑŃŅŇṄṆṈOÒÓÔÕÖŌŎŐƠǪȌȎȪȬȰṌṎṐṒỌỎỐỒỔỖỘỚỜỞỠỢPQRŔŖŘȐȒṚṞSŚŜŞŠȘṠṢṤṦṨTŢŤȚṬṮUÙÚÛÜŨŪŬŮŰŲƯȔȖṸṺỤỦỨỪỬỮỰVWŴẀẂẄXYÝŶŸȲẎỲỴỶỸZŹŻŽẒÆǼÐØǾÞĐĦĲĿŁŊŒŦƏƝǄǇǊẞΩaàáâãäåāăąǻȁȃạảấầẩẫậắằẳẵặbcçćĉċčḉdďḍḏeèéêëēĕėęěȅȇḕḗḝẹẻẽếềểễệfgĝğġģǧḡhĥḥḫiìíîïĩīĭįȉȋḯỉịjĵkķlĺļľḷḻmṃnñńņňṅṇṉoòóôõöōŏőơǫȍȏȫȭȱṍṏṑṓọỏốồổỗộớờởỡợpqrŕŗřȑȓṛṟsśŝşšșṡṣṥṧṩtţťțṭṯẗuùúûüũūŭůűųưȕȗṹṻụủứừửữựvwŵẁẃẅxyýÿŷȳẏỳỵỷỹzźżžẓßæǽðøǿþđħıĳĸŀłŉŋœŧǆǉǌȷəɲπǅǈǋﬀﬁﬂﬃﬄʹʺʻʾʿˈˉˊ\ˋˌªº0123456789¹²³¼½¾⁰⁴⁵⁶⁷⁸⁹₀₁₂₃₄₅₆₇₈₉⅓⅔⅛⅜⅝⅞_-‐‒–—―()[]{}⟨⟩#%‰\'\"‘’“”‚„‹›«»*†‡·•….,:;!¡?¿/\⁄|¦&§¶ℓ№′″‾+−±÷×=<>≤≥≈≠¬⁒∂∅∆∏∑∕∙√∞◊∫≡▷◁$¢£¤¥฿₡₦₨₩₪₫€ƒ₭₱₲₴₵₸₹₺₼₽₿^~´`˝ˆˇ˘˜¯¨˙˚¸˛©®™°℮←↑→↓↔↕↖↗↘↙■□▲△▶▼▽◀◆◇♡♥'

path = '/Users/stephennixon/Desktop/recursive-MONO_CASL_wght_slnt_ital--glyph_grid.txt'

def getUnicodeName(c):
    try:
        return unicodedata.name(c).lower()
    except ValueError:
        if c == "":
            return "latin capital ligature ij with acute"
        elif c == "":
            return "latin small ligature ij with acute"
        else:
            return ""

charsetString = ""

for i, c in enumerate(u):
    charsetString += f"{c} "

charsetString += f" @ "



with open(path, 'w') as file:
    file.write(charsetString)
    print('saved to ', str(path)) 