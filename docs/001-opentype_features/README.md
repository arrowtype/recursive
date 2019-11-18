# OpenType Features in Recursive

Tracking issue: https://github.com/arrowtype/recursive/issues/92

Helpful reference: [IBM Plex Mono features](https://github.com/IBM/plex/blob/f51d07200ae54caed11da4de140142ed61af1be3/IBM-Plex-Mono/sources/masters/IBM%20Plex%20Mono-Thin.ufo/features.fea)

Features spec https://docs.microsoft.com/en-us/typography/opentype/spec/featuretags

Feature language spec: http://adobe-type-tools.github.io/afdko/OpenTypeFeatureFileSpecification.html

## Ordering

From http://opentypecookbook.com/putting-it-together.html:

- script language specific forms (locl)
- fractions (frac, numr, dnom)
- superscript and subscript (sups, subs)
- figures (lnum, onum, pnum, tnum)
- ordinals (ordn)
- small caps (smcp, c2sc)
- all caps (case)
- various alternates (cswh, titl, salt, ss01, ss02, ss...)
- ligatures (liga, dlig)
- manual alternate access (aalt)
- capital spacing (cpsp)

## Initially-planned features:

### Done or mostly-done (even if still being refined)
- [x] rvrn (variation-contextual GSUB for .italic and .mono alternates)
- [x] kern
- [x] mark
- [x] dlig (arrow substitution, code ligatures)
- [x] liga (and rlig as appropriate)
- [x] subs, sinf, dnom, numr, sups, (subscript, superscript, etc, for figures)
- [x] ordn (ordinals – ª and º)
- [x] pnum (proportional figures – figures are tabular, by default – makes a proportional `1`)
- [x] titl (titling caps – no A–Z below the baseline, for tighter-fitting all-caps headlines)
- [x] frac (precomposed fractions only)
- [x] ss01 (disambiguated forms for `6` and `9`)
- [x] ss03 (slashed zero in sans – default is open)
- [x] zero (slashed zero for sans, where default is open)
- [x] case (case-sensitive punctuation)
- [x] ss04 (alternate /at symbol)

### To be done
- [ ] mkmk
  - [ ] probably needs `top` AND `_top` anchor in each accent
  - [ ] test that arbitrary stacking works
- [ ] aalt 
  - [ ] make script to compile this from all suffixed glyphs, making list for each base glyph
- [ ] locl (for languages)
  - [ ] dutch ij
  - [ ] turkish dotlessi

- [ ] cv01–cv09+ (control of individual roman/italic alternates) or should this just be stylistic sets? YES, because char variants seemingly cannot be named.
  - [x] a
  - [x] g
  - [ ] i
  - l
  - f
  - r

- [ ] ss02 (dotted zero – default is slashed)

### Maybe

- [ ] ? arbitrary frac (arbitrary fractions)


### Invalid
- [x] ~ss01 (all-roman forms across slnt axis)~ Implemented as `ital` axis.
- [x] ~ss02 (all-italic across slnt axis)~ Implemented as `ital` axis.
- cpsc (added spacing for all-caps text – sans only)
  - Reasion: not sure this is a good idea for a UI font. It only has partial support, and may cause confusing problems between design & development

### Not sure
- [ ] ccmp
  - not sure if this is being used [OT spec definition](https://docs.microsoft.com/en-us/typography/opentype/spec/features_ae#ccmp)
