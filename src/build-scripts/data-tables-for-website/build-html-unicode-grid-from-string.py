

html ="""\
<div class="module container-fluid">
    <div class="grid clearfix" id="grid">
        <ul>
"""
        

import unicodedata

u = 'AÀÁÂÃÄÅĀĂĄǺẠBCÇĆĈĊČDĎEÈÉÊËĒĔĖĘĚẸẼFGĜĞĠĢǦHĤIÌÍÎÏĨĪĬĮİỊJĴKĶLĹĻĽMNÑŃŅŇOÒÓÔÕÖŌŎŐǪỌPQRŔŖŘSŚŜŞŠȘTŢŤȚUÙÚÛÜŨŪŬŮŰŲỤVWŴẀẂẄXYÝŶŸȲỲỸZŹŻŽÆǼÐØǾÞĐĦĲŁŊŦƏƝẞΩaàáâãäåāăąǻạbcçćĉċčdeèéêëēĕėěẹẽfgĝğġģǧhĥiìíîïĩīĭįịjĵkķlĺļmnñńņňoòóôõöōŏőǫọpqrŕŗřsśŝşšștţťțuùúûüũūŭůűųụvwŵẁẃẅxyýÿŷȳỳỹzźżžßæǽøǿıłŉȷπªº̧̨̣̦̀́̂̃̄̆̇̈̊̋̌̒̕0123456789¹²³¼½¾⁰⁴⁵⁶⁷⁸⁹₀₁₂₃₄₅₆₇₈₉⅓⅔⅛⅜⅝⅞_-–—()[]\{\}#%‰\'"‘’“”‚„‹›«»*†.,:;…!¡?¿//\\⁄|¦@&¶ℓ·•‾+−±÷×=<>≤≥≈≠¬←↑→↓∂∆∏∕√∞∫≡$¢£¤¥฿₡₦₨₩₪₫€ƒ₭₱₲₴₵₸₼₽₿^~´`˝ˆˇ˘˜¯¨˙˚¸˛©®™°℮◊'

yamlInfo = ''

for i, c in enumerate(u):

    html += f"""\
        <li class="complete">
            <span>{c}</span>
            <div class="detail">
                <div class="detail-top-content">
                    <svg width="23" height="23" viewBox="0 0 23 23" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M23 0H0V23L23 0Z" fill="white"/>
                    </svg>
                    <small>{unicodedata.name(c).lower()} (u+{'%04x' % ord(c)})</small>
                </div>
                <span class="letter-lg">
                    {c}          
                </span>
            </div>
        </li>
    """

html += """\
        </ul>
    </div>
</div>
"""

path = 'font-betas/recursive-prop_xprn_weight_slnt_ital--2019_08_26.glyphs.html'

with open(path, 'w') as file:
    file.write(html)
    print('saved to ', str(path))