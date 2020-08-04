# Rec Mono for Code

Custom 4-style packages specifically made for code editors, each featuring:
- Regular, Italic, Bold, & Bold Italic static fonts
- An abbreviated family name to enable italic themes on macOS
- Reduced-slant italics for easier readability in code (normal Recursive Italics have slnt=-15, which is pretty intense)
- Stylistic sets pre-applied for clear, unambiguous code: a simplified `L`, `Z`, `l`, & `f` and a more-open `6` and `9`


## Packages

Download the zip in this folder for an easy way to download these fonts. Then, install the fonts then call them from your favorite code editor with their relevant family name, e.g. `Rec Mono Duotone`.

**`Rec Mono Linear`**
- Everyday workhorse for code. Simplified shapes meant to help enhance focus in complex code.

**`Rec Mono Casual`**
- A party in a font. Fun & wacky shapes, simplified enough for small sizes but curvy enough to have plenty of character. Best in casual coding & non-primary terminals.

**`Rec Mono SemiCasual`**
- Sets the CASL axis at `0.5` for font that is serious but softened a little bit. This isn't the best choice for text at large sizes (like headlines on a website), but can be a really nice balance in code.

**`Rec Mono Duotone`**
- A personal favorite – this uses Linear styles for upright text and Casual styles for italic text. In many themes that use italic styles, this will give most code a utilitarian look, but set comments and some keywords in a more-handwritten style.


## Code Ligatures

By popular demand, these fonts shift the code ligature feature from their usual OpenType feature of `dlig` to the feature `calt`, to act more like preexisting code-ligature fonts such as Fira Code & Hasklig.

These are therefore activated (or deactivated) by default in general text settings, and activatable in many code editors under typical "Code Ligatures" setting.

In the Desktop & Web fonts, code ligatures are still controlled by the `dlig` feature, so that they are *not* on by default for contexts in which they may not be well-understood by many users.
