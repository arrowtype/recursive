# /Users/stephennixon/type-repos/recursive/venv/bin/python
# coding=utf8

import unicodedata
from datetime import datetime

timestamp = datetime.now().strftime("%Y-%m-%d")

# this string was pulled from RoboFont Space Center, then edited by hand

u = 'AÀÁÂÃÄÅĀĂĄǺẠẢẤẦẨẪẬẮẰẲẴẶBCÇĆĈĊČDĎEÈÉÊËĒĔĖĘĚẸẺẼẾỀỂỄỆFGĜĞĠĢǦHĤIÌÍÎÏĨĪĬĮİỈỊJĴKĶLĹĻĽMNÑŃŅŇOÒÓÔÕÖŌŎŐƠǪỌỎỐỒỔỖỘỚỜỞỠỢPQRŔŖŘSŚŜŞŠȘTŢŤȚUÙÚÛÜŨŪŬŮŰŲƯỤỦỨỪỬỮỰVWŴẀẂẄXYÝŶŸȲỲỴỸZŹŻŽÆǼÐØǾÞĐĦĲĿŁŊŒŦƏƝƳǄǇǊẞΩaàáâãäåāăąǻạảấầẩẫậắằẳẵặbcçćĉċčdďeèéêëēĕėęěẹẻẽếềểễệfgĝğġģǧhĥiìíîïĩīĭįỉịjĵkķlĺļľmnñńņňoòóôõöōŏőơǫọỏốồổỗộớờởỡợpqrŕŗřsśŝşšștţťțuùúûüũūŭůűųưụủứừửữựvwŵẁẃẅxyýÿŷȳỳỵỹzźżžßæǽðøǿþđħıĳĸŀłŉŋœŧƴǆǉǌȷəπǅǈǋﬀﬁﬂﬃﬄªº0123456789⁰¹²³⁴⁵⁶⁷⁸⁹₀₁₂₃₄₅₆₇₈₉¼½¾⅓⅔⅛⅜⅝⅞_-–—()[]{}⟨⟩#%‰\'\"‘’“”‚„ˌ‹›«»*†‡.,:;…!¡?¿//\⁄|¦&§¶ℓ№·•′″‾+−±÷×=<>≤≥≈≠¬∂∆∏∑∕√∞∫◊≡$¢£¤¥฿₡₦₨₩₪₫€ƒ₭₱₲₴₵₸₼₽₿^~´`˝ˆˇ˘˜¯¨˙˚¸˛ʹʺʻʾʿˈˉˊˋ©®™°℮■□▲△▶▷▼▽◀◁◆◇♥♡←↑→↓↖↗↘↙↕↔'

path = 'docs/00--character_set_for_google_fonts/web-test/index.html'

html = f"""\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Recursive CharSet</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

        <h1>Recursive Character Set</h1>
        <p>As of {timestamp}</p>
        <ul class="grid">
"""

for i, c in enumerate(u):
    print(c)
    html += f"""\
        <li>
            {c}
        </li>
"""

html += """\
        <li>
            
        </li>
        <li>
            @
        </li>
    </ul>
</body>
</html>
"""



with open(path, 'w') as file:
    file.write(html)
    print('saved to ', str(path)) 