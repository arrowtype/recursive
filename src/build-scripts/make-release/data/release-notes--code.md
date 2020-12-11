# Rec Mono for Code

This folder includes four pre-customized packages specifically made for code editors, each featuring:
- Regular, Italic, Bold, & Bold Italic static fonts
- An abbreviated family name to enable italic themes on macOS
- Reduced-slant italics for easier readability in code (normal Recursive Italics have slnt=-15, which is pretty intense)
- Frozen-in Code Ligatures
- Frozen-in OpenType features to enhance legibility for code (e.g. making 1 and l instantly recognizable)
  - `ss03` # simplified f
  - `ss05` # simplified l
  - `ss07` # serifless L and Z
  - `ss09` # simplified 6 and 9

NOTE: If you would rather customize your own version of Rec Mono for Code (for instance, without Code Ligatures or with different stylistic sets frozen-in), check out https://github.com/arrowtype/recursive-code-config.


## Packages

Download the zip in this folder for an easy way to download these fonts. Then, install the fonts then call them from your favorite code editor with their relevant family name, e.g. `Rec Mono Duotone`.

**`Rec Mono Duotone`**
- A personal favorite – this uses Linear styles for upright text and Casual styles for italic text. In many themes that use italic styles, this will give most code a utilitarian look, but set comments and some keywords in a more-handwritten style.

**`Rec Mono Linear`**
- Everyday workhorse for code. Simplified shapes meant to help enhance focus in complex code.

**`Rec Mono Casual`**
- A party in a font. Fun & wacky shapes, simplified enough for small sizes but curvy enough to have plenty of character. Best in casual coding & non-primary terminals.

**`Rec Mono SemiCasual`**
- Sets the CASL axis at `0.5` for font that is serious but softened a little bit. This isn't the best choice for text at large sizes (like headlines on a website), but can be a really nice balance in code.

## Code Ligatures

By popular demand, these fonts shift the code ligature feature from their usual OpenType feature of `dlig` to the feature `calt`, to act more like preexisting code-ligature fonts such as Fira Code & Hasklig.

In the Desktop & Web fonts, code ligatures are still controlled by the `dlig` feature, so that they are *not* on by default for contexts in which they may not be well-understood by many users.

## And again...

If you would rather customize your own version of Rec Mono for Code, use the scripts at https://github.com/arrowtype/recursive-code-config. 

Happy coding!
