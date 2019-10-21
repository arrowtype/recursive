# Character Set for Google Fonts 

## Glyphs added that are not required

- code ligatures
- diagonal arrows
- more prebuilt fractions

## Not doing

Some glyphs will not be supported by Recursive, because they are not particularly useful in a font for code & UI. 

- Small caps

- Peseta, Lira, Franc
  - outdated

- Lining figures (`.lf` in Plus)
  - All figures are lining

- Traditional "discretionary ligatures"
  - `T_h c_h c_t s_t`
  - More useful as a decorative element in print
  - May confuse users compared to the actual code ligatures in Recursive


## Need to add, as of Oct 21, 2019

This would be more useful as a script ... it should be able to generate an on-the-fly report of selected fonts vs the character set we need.

- case-specific forms (need to specify an exact set)

- **Digraphs**
  - 0x01C4 Ǆ LATIN CAPITAL LETTER DZ WITH CARON
  - 0x01C5 ǅ LATIN CAPITAL LETTER D WITH SMALL LETTER Z WITH CARON
  - 0x01C6 ǆ LATIN SMALL LETTER DZ WITH CARON
  - 0x01C7 Ǉ LATIN CAPITAL LETTER LJ
  - 0x01C8 ǈ LATIN CAPITAL LETTER L WITH SMALL LETTER J
  - 0x01C9 ǉ LATIN SMALL LETTER LJ
  - 0x01CA Ǌ LATIN CAPITAL LETTER NJ
  - 0x01CB ǋ LATIN CAPITAL LETTER N WITH SMALL LETTER J
  - 0x01CC ǌ LATIN SMALL LETTER NJ

- **Basic Latin Ligatures**
  - 0xFB01 ﬁ LATIN SMALL LIGATURE FI
  - 0xFB02 ﬂ LATIN SMALL LIGATURE FL
  - f_f
  - f_f_i
  - f_f_l

- **Modifiers**
  - 0x02B9 ʹ MODIFIER LETTER PRIME
  - 0x02BA ʺ MODIFIER LETTER DOUBLE PRIME
  - 0x02BB ʻ MODIFIER LETTER TURNED COMMA
  - 0x02BE ʾ MODIFIER LETTER RIGHT HALF RING
  - 0x02BF ʿ MODIFIER LETTER LEFT HALF RING
  - 0x02C8 ˈ MODIFIER LETTER VERTICAL LINE
  - 0x02C9 ˉ MODIFIER LETTER MACRON
  - 0x02CA ˊ MODIFIER LETTER ACUTE ACCENT
  - 0x02CB ˋ MODIFIER LETTER GRAVE ACCENT
  - 0x02CC ˌ MODIFIER LETTER LOW VERTICAL LINE

- **Spacing glyphs**
  - 0x2007   FIGURE SPACE
  - 0x2008   PUNCTUATION SPACE
  - 0x2009   THIN SPACE
  - 0x200A   HAIR SPACE
  - 0x200B ​ ZERO WIDTH SPACE

- **Accents below**
  - 0x032E ̮ COMBINING BREVE BELOW
  - 0x0331 ̱ COMBINING MACRON BELOW

- **Math / Misc Marks**
  - 0x27E8 ⟨ MATHEMATICAL LEFT ANGLE BRACKET
  - 0x27E9 ⟩ MATHEMATICAL RIGHT ANGLE BRACKET
  - 0x2032 ′ PRIME
  - 0x2033 ″ DOUBLE PRIME
  - 0x2030 ‰ PER MILLE SIGN
  - 0x2116 № NUMERO SIGN
  - soundcopyright

- Top anchors to combining accents


## Potential glyphs to consider adding

- check
- checkbox
- checkedbox
- ℗, soundcopyright
- ℠, servicemark