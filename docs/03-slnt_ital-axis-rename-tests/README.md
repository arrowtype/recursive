# Testing different axis naming for Slant & Italic axes

## The problem(s)

1. There is a lack of clarity as to how CSS should treat variable fonts that contain *both* Slant and Italic axes. The main question is: what should `font-style: italic` do with these axes? There is a good chance that this property & value will *either* set Slant to max or set Italic to `1`, but may not do both.
2. It is hard for users to understand the different and interaction between Recursive's `slnt` and `ital` axes.
3. It is hard for users to predict that *negative* Slant slants letters "forward" (clockwise)

## Current state

In Recursive, the `slnt` axis controls clockwise slant, and true-italic letterforms sub in automatically above 50% slant (less than `-7.5`). These "true italic" letterforms mimic cursive handwriing, and include single-story "a" and "g" plus exit-strokes on most lowercase letters, producing a style that is a disconnected script/cursive.

The `ital` axis allows users to have more control over the true-italic substitution behavior.
- `0` turns off substitution, allowing for slanted-Roman styles
- `0.5` (the default) allows for automatic true-italic substitution when slnt is above 50%
- `1` turns on true-italic forms at any slant, allowing for upright italics

## Possible ways forward

1. Keep `slnt` and `ital` as-is
2. Keep `slnt` as is, control true-italic substitution with "Cursive" (`CRSV`)
3. Change Slant `slnt` axis to Italic `ital` axis, control true-italic substitution with "Cursive" (`CRSV`)
4. Something else?? E.g. Keep existing behavior mostly, but connect `ital=1` to full slant

### Option 1: Pros and Cons

> Keep `slnt` and `ital` as-is

**Pros**
- No need to change print specimen design/content at this late stage (as of Friday, we thought we had "frozen" content & design)
- No need to change setup for users that may be used to the current implementation
- If we think CSS `font-style: italic` *should* control Slant + Italic, this would possibly help influence that

**Cons**
- (see "Problems" section, above)

### Option 2: Pros and Cons

> Keep `slnt` as is, control true-italic substitution with "Cursive" (`CRSV`)

**Pros**
- We only have to partially change user expectations
- `slnt` having a range of values from `0` to `-15` indicates users something about what to expect from `slnt=-15`, and also suggests that other slants are possible, e.g. `slnt=-9`, etc. This can vary from font to font, just as actually degree of slant can.
- Mapping true-italic behavior to an unfamiliar term `CRSV` cues users that the behavior is something unfamiliar

**Cons**
- Most users don't expect clockwise slant to be negative, and this doesn't deal with that
- The print specimen has already taken more time than the designers expected they had signed up for, so it would seem unethical to change something now, unless we can pay them for the extra time it will take to update
- `sltn` cannot be mathematically exact between min and max values, and is only really a general amount of lean, becuase various letterforms in Italic styles generally break the general italic angle. (E.g. *f* often has less slant in the middle than *H*.)
- `slnt` may not be the best axis to activate a true-italic style (See *What are Italics?* section below.)

### Option 3: Pros and Cons

> Change Slant `slnt` axis to Italic `ital` axis, control true-italic substitution with "Cursive" (`CRSV`)

**Pros**
- Recursive Italic styles are not merely slanted, but truly Italic. (See *What are Italics?* section below.)
- `ital` is simpler to understand than `slnt` – `0` is obviously not Italic and `1` is obviously Italic
- Mapping true-italic behavior to an unfamiliar term `CRSV` cues users that the behavior is something unfamiliar

**Cons**
- Shifts user understanding in two axes, rather than just one
- The print specimen has already taken more time than the designers expected they had signed up for, so it would seem unethical to change something now, unless we can pay them for the extra time it will take to update

## What *are* Italics? What is Slant?

Arguably, there is a typographic difference between concepts of *Slant* & *Italic*. Generally speaking, *Italics* are used for hierarchy within text (somewhat similar to *Weight*), while *Slant* is a visual attribute that can be used in layout (more similar to *Width*). Put another way, *Italics* are about semantic meaning, while *Slant* is more about visual presentation.

### Italics are emphasis, and often immitate handwriting

The word "Italic" indicates something about typographic hierarchy, rather than just simple slanting or even a purely aesthetic change. 

Italics, in a formal typographic sense, are a secondary style of text which can be used to indicate a small amount of emphasis. For instance, they may call attention to certain terms, denote foreign words, indicate block quotes, be used to reference the name of a cited news article, etc.

Additionally, "Italic" characters may have different amounts of slant within the same type family. Even within a single script, such as Latin italic, characters must often have different amounts of slant. A long italic *f* usually needs to be more upright, overall, than the strokes of an italic *H*, or the *f* will appear to lean forward *too much*.

Within different scripts in the same type family, general levels of slant may also be different. The notion of "Italics" comes from Latin text, but has been applied to other scripts. For example, Hebrew is read right-to-left, so Hebrew italics would have to lean counter-clockwise to have a "forward" slant. In Greta Text, by Typotheque, the Hebrew Italics have about half the amount of slant as the Latin Italics. Additionally, these Hebrew Italics have varying levels of slant, because they are showing a "handwriting" origin much more than they are showing a certain "slant."

![Greta Text Italics, Latin vs Hebrew](assets/2020-03-02-12-00-19.png)

 I don't know of an "italic" Arabic, but presumably, it would be possible for a single Arabic typeface to have a standard style, plus a secondary style that might have more-handwritten letterforms.

 Even though "Italics" in some typefaces (such as Arial) are simply slanted versions of the general style, this is more of an exception than a rule – and these "Italics" are still used to provide emphasis in text in a similar manner to other type systems.

### Slant is a visual attribute

Just as *Width* changes the overall shaping of letters as a visual change that can help in certain layouts, *Slant* may be best treated as a visual change that affects the overall lean of letters, more as a visual change for certain aesthetics than as a device for typographic semantics.

## Tests

(Work in progress)
