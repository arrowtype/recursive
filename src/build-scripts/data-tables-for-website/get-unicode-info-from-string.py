import unicodedata

u = 'AÀÁÂÃÄÅĀĂĄǺẠBCÇĆĈĊČDĎEÈÉÊËĒĔĖĘĚẸẼFGĜĞĠĢǦHĤIÌÍÎÏĨĪĬĮİỊJĴKĶLĹĻĽMNÑŃŅŇOÒÓÔÕÖŌŎŐǪỌPQRŔŖŘSŚŜŞŠȘTŢŤȚUÙÚÛÜŨŪŬŮŰŲỤVWŴẀẂẄXYÝŶŸȲỲỸZŹŻŽÆǼÐØǾÞĐĦĲŁŊŦƏƝẞΩaàáâãäåāăąǻạbcçćĉċčdeèéêëēĕėěẹẽfgĝğġģǧhĥiìíîïĩīĭįịjĵkķlĺļmnñńņňoòóôõöōŏőǫọpqrŕŗřsśŝşšștţťțuùúûüũūŭůűųụvwŵẁẃẅxyýÿŷȳỳỹzźżžßæǽøǿıłŉȷπªº̧̨̣̦̀́̂̃̄̆̇̈̊̋̌̒̕0123456789¹²³¼½¾⁰⁴⁵⁶⁷⁸⁹₀₁₂₃₄₅₆₇₈₉⅓⅔⅛⅜⅝⅞_-–—()[]\{\}#%‰\'"‘’“”‚„‹›«»*†.,:;…!¡?¿//\\⁄|¦@&¶ℓ·•‾+−±÷×=<>≤≥≈≠¬←↑→↓∂∆∏∕√∞∫≡$¢£¤¥฿₡₦₨₩₪₫€ƒ₭₱₲₴₵₸₼₽₿^~´`˝ˆˇ˘˜¯¨˙˚¸˛©®™°℮◊'

yamlInfo = ''

for i, c in enumerate(u):

    charInfo = f'''
- character: {c}
  unicode: u+{'%04x' % ord(c)}
  name: {unicodedata.name(c).lower()}
  complete: true
    '''

    yamlInfo = yamlInfo + charInfo

print(yamlInfo)

path = 'font-betas/recursive-prop_xprn_weight_slnt_ital--2019_08_26.glyphs.yml'

with open(path, 'w') as file:
    file.write(yamlInfo)