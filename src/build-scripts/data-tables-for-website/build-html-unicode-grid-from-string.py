# /Users/stephennixon/type-repos/recursive/venv/bin/python
# coding=utf8

html ="""\
<div class="module container-fluid">
    <div class="languages-list">
        Abenaki, Afaan Oromo, Afar, Afrikaans, Albanian, Alsatian, Amis, Anuta, Aragonese, Aranese, Aromanian, Arrernte, Arvanitic (Latin), Asturian, Atayal, Aymara, Azerbaijani, Bashkir (Latin), Basque, Belarusian (Latin), Bemba, Bikol, Bislama, Bosnian, Breton, Cape Verdean Creole, Catalan, Cebuano, Chamorro, Chavacano, Chichewa, Chickasaw, Cimbrian, Cofán, Cornish, Corsican, Creek, Crimean Tatar (Latin), Croatian, Czech, Danish, Dawan, Delaware, Dholuo, Drehu, Dutch, English, Esperanto, Estonian, Faroese, Fijian, Filipino, Finnish, Folkspraak, French, Frisian, Friulian, Gagauz (Latin), Galician, Ganda, Genoese, German, Gikuyu, Gooniyandi, Greenlandic (Kalaallisut), Guadeloupean Creole, Gwich’in, Haitian Creole, Hän, Hawaiian, Hiligaynon, Hopi, Hotcąk (Latin), Hungarian, Icelandic, Ido, Igbo, Ilocano, Indonesian, Interglossa, Interlingua, Irish, Istro-Romanian, Italian, Jamaican, Javanese (Latin), Jèrriais, Kaingang, Kala Lagaw Ya, Kapampangan (Latin), Kaqchikel, Karakalpak (Latin), Karelian (Latin), Kashubian, Kikongo, Kinyarwanda, Kiribati, Kirundi, Klingon, Kurdish (Latin), Ladin, Latin, Latino sine Flexione, Latvian, Lithuanian, Lojban, Lombard, Low Saxon, Luxembourgish, Maasai, Makhuwa, Malay, Maltese, Manx, Māori, Marquesan, Megleno-Romanian, Meriam Mir, Mirandese, Mohawk, Moldovan, Montagnais, Montenegrin, Murrinh-Patha, Nagamese Creole, Nahuatl, Ndebele, Neapolitan, Ngiyambaa, Niuean, Noongar, Norwegian, Novial, Occidental, Occitan, Old Icelandic, Old Norse, Onĕipŏt, Oshiwambo, Ossetian (Latin), Palauan, Papiamento, Piedmontese, Polish, Portuguese, Potawatomi, Q’eqchi’, Quechua, Rarotongan, Romanian, Romansh, Rotokas, Sami (Inari Sami), Sami (Lule Sami), Sami (Northern Sami), Sami (Southern Sami), Samoan, Sango, Saramaccan, Sardinian, Scottish Gaelic, Serbian (Latin), Seri, Seychellois Creole, Shawnee, Shona, Sicilian, Silesian, Slovak, Slovenian, Slovio (Latin), Somali, Sorbian (Lower Sorbian), Sorbian (Upper Sorbian), Sotho (Northern), Sotho (Southern), Spanish, Sranan, Sundanese (Latin), Swahili, Swazi, Swedish, Tagalog, Tahitian, Tetum, Tok Pisin, Tokelauan, Tongan, Tshiluba, Tsonga, Tswana, Tumbuka, Turkish, Turkmen (Latin), Tuvaluan, Tzotzil, Uzbek (Latin), Venetian, Vepsian, Vietnamese, Volapük, Võro, Wallisian, Walloon, Waray-Waray, Warlpiri, Wayuu, Welsh, Wik-Mungkan, Wiradjuri, Wolof, Xavante, Xhosa, Yapese, Yindjibarndi, Zapotec, Zarma, Zazaki, Zulu, Zuni
    </div>
    
    <div class="grid clearfix" id="grid">
"""
        

import unicodedata

# this string was pulled from RoboFont Space Center

# u = 'AÀÁÂÃÄÅĀĂĄǺẠBCÇĆĈĊČDĎEÈÉÊËĒĔĖĘĚẸẼFGĜĞĠĢǦHĤIÌÍÎÏĨĪĬĮİỊJĴKĶLĹĻĽMNÑŃŅŇOÒÓÔÕÖŌŎŐǪỌPQRŔŖŘSŚŜŞŠȘTŢŤȚUÙÚÛÜŨŪŬŮŰŲỤVWŴẀẂẄXYÝŶŸȲỲỸZŹŻŽÆǼÐØǾÞĐĦĲŁŊŦƏƝẞΩaàáâãäåāăąǻạbcçćĉċčdeèéêëēĕėěẹẽfgĝğġģǧhĥiìíîïĩīĭįịjĵkķlĺļmnñńņňoòóôõöōŏőǫọpqrŕŗřsśŝşšștţťțuùúûüũūŭůűųụvwŵẁẃẅxyýÿŷȳỳỹzźżžßæǽøǿıłŉȷπªº̧̨̣̦̀́̂̃̄̆̇̈̊̋̌̒̕0123456789¹²³¼½¾⁰⁴⁵⁶⁷⁸⁹₀₁₂₃₄₅₆₇₈₉⅓⅔⅛⅜⅝⅞_-–—()[]\{\}#%‰\'"‘’“”‚„‹›«»*†.,:;…!¡?¿//\\⁄|¦@&¶ℓ·•‾+−±÷×=<>≤≥≈≠¬←↑→↓∂∆∏∕√∞∫≡$¢£¤¥฿₡₦₨₩₪₫€ƒ₭₱₲₴₵₸₼₽₿^~´`˝ˆˇ˘˜¯¨˙˚¸˛©®™°℮◊'
u = 'AÀÁÂÃÄÅĀĂĄǺẠẢẤẦẨẪẬẮẰẲẴẶBCÇĆĈĊČDĎEÈÉÊËĒĔĖĘĚẸẺẼẾỀỂỄỆFGĜĞĠĢǦHĤIÌÍÎÏĨĪĬĮİỈỊJĴKĶLĹĻĽMNÑŃŅŇOÒÓÔÕÖŌŎŐƠǪỌỎỐỒỔỖỘỚỜỞỠỢPQRŔŖŘSŚŜŞŠȘTŢŤȚUÙÚÛÜŨŪŬŮŰŲƯỤỦỨỪỬỮỰVWŴẀẂẄXYÝŶŸȲỲỴỸZŹŻŽÆǼÐØǾÞĐĦĲĿŁŊŒŦƏƝƳǇǊẞΩaàáâãäåāăąǻạảấầẩẫậắằẳẵặbcçćĉċčdeèéêëēĕėęěẹẻẽếềểễệfgĝğġģǧhĥiìíîïĩīĭįỉịjĵkķlĺļľmnñńņňoòóôõöōŏőơǫọỏốồổỗộớởỡợpqrŕŗřsśŝşšștţťțuùúûüũūŭůűųưụủứừửữựvwŵẁẃẅxyýÿŷȳỳỵỹzźżžßæǽðøǿþđħıŀłŉŋœŧƴǆȷəπǋʹʺʻʾʿˈˉˊˋˌ˝ˆˇ˘˜¯¨˙˚¸˛ªº0123456789¹²³⁰⁴⁵⁶⁷⁸⁹₀₁₂₃₄₅₆₇₈₉¼½¾⅓⅔⅛⅜⅝⅞&§¶¥฿₡₦₨₩₪₫€ƒ₭₱₲₴₵₸₼₽₿_-–—()[]\{\}⟨⟩#%‰\'\"‘’“”‚„‹›«»*†‡.,:;…!¡?¿//\⁄|¦ℓ·•′″‾+−±÷×=<>≤≥≈≠¬∂∆∏∑∕√∞∫◊≡$¢£¤^~´`©®™°℮▷◁■□▲△▶▼▽◀◆◇♡♥←↑→↓↖↗↘↙↕'

path = 'font_betas/recursive-MONO_CASL_wght_slnt_ital--2019_10_31-18_00.glyphs.html'

yamlInfo = ''

for i, c in enumerate(u):
    html += f"""\
        <span class="complete">
            {c}
            <div class="detail">
                <div class="letter-lg">
                    {c}          
                </div>
                <div class="detail-top-content">
                    <svg width="23" height="23" viewBox="0 0 23 23" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M23 0H0V23L23 0Z" fill="white"/>
                    </svg>
                    <small>{unicodedata.name(c).lower()} (u+{'%04x' % ord(c)})</small>
                </div>
            </div>
        </span>
    """

html += """\
        <span class="complete">
            
            <div class="detail">
                <div class="letter-lg">
                              
                </div>
                <div class="detail-top-content">
                    <svg width="23" height="23" viewBox="0 0 23 23" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M23 0H0V23L23 0Z" fill="white"/>
                    </svg>
                    <small>.notdef</small>
                </div>
            </div>
        </span>
        <span class="complete">
            @
            <div class="detail">
                <div class="letter-lg">
                    @          
                </div>
                <div class="detail-top-content">
                    <svg width="23" height="23" viewBox="0 0 23 23" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M23 0H0V23L23 0Z" fill="white"/>
                    </svg>
                    <small>commercial at (u+0040)</small>
                </div>
            </div>
        </span>
        </ul>
    </div>
</div>
"""



with open(path, 'w') as file:
    file.write(html)
    print('saved to ', str(path)) 