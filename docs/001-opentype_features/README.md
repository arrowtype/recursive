# OpenType Features in Recursive

Tracking issue: https://github.com/arrowtype/recursive/issues/92

## Initially-planned features:

### Done or mostly-done (even if still being refined)
- [x] rvrn (variation-contextual GSUB for .italic and .mono alternates)
- [x] kern
- [x] mark
- [x] mkmk
  - [ ] test that arbitrary stacking works
- [x] dlig (arrow substitution, code ligatures)

### To be done
- [ ] aalt 
- [ ] case (case-sensitive punctuation)
- [ ] liga (and rlig as appropriate)
- [ ] subs, sinf, dnom, numr, sups, (subscript, superscript, etc, for figures)
- [ ] titl (titling caps – no A–Z below the baseline, for tighter-fitting all-caps headlines)
- [ ] locl (for languages)
  - [ ] dutch ij
  - [ ] turkish dotlessi
- [ ] cpsc (added spacing for all-caps text – sans only)
  - [ ] Test: is this a good idea? it only has partial support, and may cause confusing problems between design & development
- [ ] cv01–cv09+ (control of individual roman/italic alternates)
- [ ] ss01 (dotted zero – default is slashed)
- [-] ss02 (disambiguated forms for `6` and `9`)
  - [x] draw glyphs
  - [ ] implement
- [ ] pnum (proportional figures – figures are tabular, by default – makes a proportional `1`)
- [ ] frac (arbitrary fractions)
- [ ] ordn (ordinals – ª and º)
- [ ] zero (slashed zero for sans, where default is open)
  - [ ] figure out how to coordinate this with the GSUB/rvrn taking place

### Invalid
- [x] ~ss01 (all-roman forms across slnt axis)~ Implemented as `ital` axis.
- [x] ~ss02 (all-italic across slnt axis)~ Implemented as `ital` axis.

### Not sure
- [ ] ccmp
  - not sure if this is being used [OT spec definition](https://docs.microsoft.com/en-us/typography/opentype/spec/features_ae#ccmp)
