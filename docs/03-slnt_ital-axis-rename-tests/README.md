# Testing different axis naming for Slant & Italic axes

*Note: Much of the following was greatly assisted through conversation with David Jonathan Ross (DJR), though also through experimentation and experience in the Recursive project.*

## The problem(s)

1. There is a lack of clarity as to how CSS should treat variable fonts that contain *both* Slant and Italic axes. The main question is: what should `font-style: italic` do with these axes? There is a good chance that this property & value will *either* set Slant to max or set Italic to `1`, but may not do both.
2. It is hard for users to understand the different and interaction between Recursive's `slnt` and `ital` axes.
3. It is hard for users to predict that *negative* Slant slants letters "forward" (clockwise)

## How Recursive currently works (as of March 2, 2020)

In Recursive, the `slnt` axis controls clockwise slant, and true-italic letterforms sub in automatically above 50% slant (less than `-7.5`). These "true italic" letterforms mimic cursive handwriing, and include single-story "a" and "g" plus exit-strokes on most lowercase letters, producing a style that is a disconnected script/cursive.

The `ital` axis allows users to have more control over the true-italic substitution behavior.
- `0` turns off substitution, allowing for slanted-Roman styles
- `0.5` (the default) allows for automatic true-italic substitution when slnt is above 50%
- `1` turns on true-italic forms at any slant, allowing for upright italics

![Interaction of slnt & ital axes in Recursive](assets/recursive-slnt_ital-2020_03_02.gif)

## What does the CSS spec say?

The CSS Spec is somewhat ambiguous/confusing on [font-style](https://drafts.csswg.org/css-fonts-4/#font-style-prop), but it could be interpreted as saying that `font-style:italic` should have a browser request ital:1, and if that's not available, should request the max slnt. This would probably match behavior for `<em>` and `<i>` tags.

> italic: Matches against a font that is labeled as an italic face, or an oblique face if one does not exist. ... For TrueType / OpenType fonts that use variations, the slnt variation is used to implement oblique values, and the ital variation with a value of 1 is used to implement the italic values.
 
But this is (maybe?) complicated by a later statement:

> For the purposes of font matching, User Agents may treat italic as a synonym for oblique. For User Agents that treat these values distinctly, synthesis must not be performed for italic.

This means, as far as I can tell, that `font-style:italic` should call a font if that font is established in `@font-face` rules to have `font-style:oblique`. However, the concept might logically be extended as saying that `font-style:italic` should "implement oblique values" with the slnt variation, as stated above.

However, because there are different legitimate uses for slant vs italic styles, it may not be a bad thing for `<em>`, `<i>`, and `font-style:italic` to only call the ital axis.

## What *are* Italics? What is Slant?

Arguably, there is a typographic difference between concepts of *Slant* & *Italic*. Generally speaking, *Italics* are used for hierarchy within text (somewhat similar to *Weight*), while *Slant* is a visual attribute that can be used in layout (more similar to *Width*). Put another way, *Italics* are about semantic meaning, while *Slant* is more about visual presentation.

### Italics are for secondary emphasis, and often immitate handwriting

The word "Italic" indicates something about typographic hierarchy, rather than just simple slanting or even a purely aesthetic change. 

Italics, in a formal typographic sense, are a secondary style of text which can be used to indicate a small amount of emphasis. For instance, they may call attention to certain terms, denote foreign words, indicate block quotes, be used to reference the name of a cited news article, etc.

Additionally, "Italic" characters may have different amounts of slant within the same type family. Even within a single script, such as Latin italic, characters must often have different amounts of slant. A long italic *f* usually needs to be more upright, overall, than the strokes of an italic *H*, or the *f* will appear to lean forward *too much*.

Within different scripts in the same type family, general levels of slant may also be different. The notion of "Italics" comes from Latin text, but has been applied to other scripts. For example, Hebrew is read right-to-left, so Hebrew italics would have to lean counter-clockwise to have a "forward" slant. In Greta Text, by Typotheque, the Hebrew Italics have about half the amount of slant as the Latin Italics. Additionally, these Hebrew Italics have varying levels of slant, because they are showing a "handwriting" origin much more than they are showing a certain "slant."

![Greta Text Italics, Latin vs Hebrew](assets/2020-03-02-12-00-19.png)

 I don't know of an "italic" Arabic, but presumably, it would be possible for a single Arabic typeface to have a standard style, plus a secondary style that might have more-handwritten letterforms.

 Even though "Italics" in some typefaces (such as Arial) are simply slanted versions of the general style, this is more of an exception than a rule. These styles are often called "Obliques" by typographers, but are still used to provide emphasis in text in a similar manner to other type systems.

### Slant is a visual/"mechanical" attribute

Just as *Width* changes the overall shaping of letters as a visual change that can help in certain layouts, *Slant* may be best treated as a visual change that affects the overall lean of letters, more as a visual change for certain aesthetics than as a device for typographic semantics. Slant without glyph substitution allows for things like animated interactions (e.g. links that slant when hovered, letters that stay "upright" despite a device's gyroscopic tilt), interesting display typography (e.g. posters with sloped typography, signage on staircases), and more.

### Should the OpenType/Google Fonts specs deprecate Slant or Italic? No.

There is overlap and ambiguity between Slant and Italic axes, and this has led to confusion and slow movement in browsers supporting this axes, as well as in average font designers in following the spec properly.

As outlined above, *Italic* and *Slant* both serve a unique purpose, and there are contexts in which a user would want one or the other separately, and probably also contexts in which a user might want some separately-controllable combination of the two (e.g. animated UI text that includes a secondary level of emphasis).

The specs shouldn't eliminate one or the other; they should provide more clarity and guidance around the purpose and implemenation of each.

In general, "Italic" instances should be activated via the `ital` axis, while "Oblique" instances are activated via the `slnt` axis.

## Potential alternative ways to implement Recursive

**Simple options**
1. Keep `slnt` and `ital` as-is
2. Keep `slnt` as is, control true-italic substitution with "Cursive" (`CRSV`)
3. Change Slant `slnt` axis to Italic `ital` axis, control true-italic substitution with "Cursive" (`CRSV`)

**Additional possibilities**
4. Just `ital` or just `slnt`, then split out `CRSV` and `ROMN` into two separate binary axes
5. `slnt` and `CRSV` could be like "parametric axes," while `ital` is the combination of these. Italic text is Slanted *and* Cursive.
6. Keep existing behavior for `slnt` and `ital` up to 0.9, but make `ital=1` activate full slant (first attempt at this not successful)

### Option 1: Keep `slnt` and `ital` as-is

**Pros**
- No need to change print specimen design/content at this late stage (as of Friday, we thought we had "frozen" content & design)
- No need to change setup for users that may be used to the current implementation
- If we think CSS `font-style: italic` *should* control Slant + Italic, this would possibly help influence that

**Cons**
- (see "Problems" section, above)

### Option 2: Keep `slnt` as is, control true-italic substitution with "Cursive" (`CRSV`)

**Pros**
- We only have to partially change user expectations
- `slnt` having a range of values from `0` to `-15` indicates users something about what to expect from `slnt=-15`, and also suggests that other slants are possible, e.g. `slnt=-9`, etc. This can vary from font to font, just as actually degree of slant can.
- Mapping true-italic behavior to an unfamiliar term `CRSV` cues users that the behavior is something unfamiliar

**Cons**
- Most users don't expect clockwise slant to be negative, and this doesn't deal with that
- The print specimen has already taken more time than the designers expected they had signed up for, so it would seem unethical to change something now, unless we can pay them for the extra time it will take to update
- `sltn` cannot be mathematically exact between min and max values, and is only really a general amount of lean, becuase various letterforms in Italic styles generally break the general italic angle. (E.g. *f* often has less slant in the middle than *H*.)
- `slnt` may not be the best axis to activate a true-italic style (See *What are Italics?* section below.)

### Option 3: Change Slant `slnt` axis to Italic `ital` axis, control true-italic substitution with "Cursive" (`CRSV`)

**Pros**
- Recursive Italic styles are not merely slanted, but truly Italic. (See *What are Italics?* section below.)
- `ital` is simpler to understand than `slnt` – `0` is obviously not Italic and `1` is obviously Italic
- Mapping true-italic behavior to an unfamiliar term `CRSV` cues users that the behavior is something unfamiliar

**Cons**
- Shifts user understanding in two axes, rather than just one
- The print specimen has already taken more time than the designers expected they had signed up for, so it would seem unethical to change something now, unless we can pay them for the extra time it will take to update

### Option 4: Just `ital` or just `slnt`, then split out `CRSV` and `ROMN` into two separate binary axes

This would be similar to the previous two options, but instead of `CRSV` having options `0`, `0.5`, and `1` (off, auto, on), it would have Roman (`ROMN`) with options `0` and `1` (auto, on) and Cursive, (auto, on).

**Pros**
- DJR: "a good axis does one simple thing, and does it well"
- 

**Cons**
- Would be less clear why these aren't just Stylistic Sets (and this isn't a stylistic set because those are often hard to find, and customize behavior of just one character, while control cursive alts is a near-global change convering most of the lowercase)
- Not easy to guess what happens when `ROMN=1` *and* `CRSV=1`. Probably, one would override the other? Or possibly, it would flip the behavior of cursive alts (e.g. upright is cursive while sloped is roman).
- Might suggest that Fraunces `WONK` should also be split into two axes such as `WONK` and `NORM`

### Option 5: `slnt` and `CRSV` could be like "parametric axes," while `ital` is the combination of these.

**Pros**
- Each axis has its role, and each does its thing
- DJR: "I think it's worth the risk to have them both in [`slnt` and `CRSV` making up the blended `ital`], because it's not easy to get to a "bad" solution. That would only ever happen for users seeing the axis sliders in a pro design tool." (Counterpoint: users will likely see these sliders on the minisite, on specimens, and possibly on Google Fonts.)
- Might allow two in-spec CSS ways to access italic *or* oblique

`font-style: italic;` gives proper italic
`font-style: oblique;` gives sloped roman

**Cons**
- Might introduce "doubling" possibility / unsafe areas of designspace
- Currently unclear how to implement (though DJR is confident it could be done, possibly via duplicate sources)
- Would add additional axis, possibly making the font more rather than less confusing
- Might feel a bit like "amstelvar," which is easy for newcomers to perceive as broken/confusing. Amstelvar is very cool, but the goal of Recursive is to be nerdy but approacheable.

### Option 6: Keep existing behavior for `slnt` and `ital` up to 0.9, but make `ital=1` activate full slant (first attempt at this not successful)

**Pros**
- Listed axes don't change
- `ital=1` would activate expected style, as would `slnt=-15`
- ital 0–0.9 could still have off/auto/on interaction

**Cons**
- Currently unclear how to implement. My first attempt resulted in slanted italics *only* being available when *both* `slnt` & `ital` were at maximum values
- The `ital`/`CRSV` axis is already hard to understand as `off/auto/on`, and making it `off/auto/on/full` becomes a mixed set of effects, and probably much harder to explain

## What's the best option?

Without much testing, I personally feel that Option 3 (`ital` controls slope & alts, `CRSV` controls alts) is best.

It is the option which makes things most clear, without adding additional complexity to the system. It still allows for the entire designspace to be accessible, without creating unsafe or newly confusing areas.

## Test fonts

> (⚠️ Work in progress – test fonts not yet made ⚠️)
> 1. Prep variable font build as usual `cd mastering && python build.py --varfiles`
> 2. Copy the test designspace into the generated `mastering/build/src` folder
> 3. Run `fontmake -m <test_designspace> -o variable`

## Relevant links

- [CSS Spec, font-style](https://drafts.csswg.org/css-fonts-4/#font-style-prop)
- [OpenType Spec, ital axis](https://docs.microsoft.com/en-us/typography/opentype/spec/dvaraxistag_ital)
- [OpenType Spec, ital axis](https://docs.microsoft.com/en-us/typography/opentype/spec/dvaraxistag_slnt)