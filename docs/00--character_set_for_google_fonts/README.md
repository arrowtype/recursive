# Character Set for Google Fonts

Recursive will support the following [Google Fonts Glyph Sets](https://github.com/googlefonts/gftools/tree/ead41409bfe154e170dcde47626ce2d66a59878e/Lib/gftools/encodings/GF%20Glyph%20Sets#gf-latin-expert-271-for-984-total), with modifications as specified below:
- Core
- Plus
- Pro
- Expert

## Where Recursive exceeds standard Google Fonts Latin character setssd

- [Code ligatures](./code-ligatures--planning)
- Additional currencies for many countries which use the Latin script ([more details](https://github.com/googlefonts/gftools/pull/145)) `฿ ₨ ₪ ₴ ₸ ₿`
- Additional arrows `↔ ↕ ↖ ↗ ↘ ↙`
- A few additional language-specific glyphs, such as Dutch ij and ijacute ligatures
- A variable .notdef glyph (because it's cool)
- Case-specific forms (need to specify an exact set)
- check, checkbox, checkedbox

## Glyphs excluded despite being in existing Google Fonts Latin character sets, and why

Some glyphs will not be supported by Recursive because they are not useful in a font for code & UI. 

- Small caps
  - Reason: small caps are very seldom used on the web, and never used in code (that I am aware of)

- Peseta, Lira, Franc
  - Reason: these currencies are outdated

- Lining figures (`.lf` in Plus)
  - Reason: All figures are lining, which are far more typical (and recognizable) in web & code

- Traditional discretionary ligatures: `T_h c_h c_t s_t`
  - Reasion: More useful as a decorative element in print
  - Reasion: may confuse users compared to the actual code ligatures in Recursive, which will be established under the `dlig` feature

- Carriage Return
  - Reason: [unecessary](https://github.com/googlefonts/fontbakery/issues/2677)

## Potential glyphs to consider adding in the future

- ℗, soundcopyright
- ℠, servicemark
