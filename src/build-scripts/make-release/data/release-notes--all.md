# Recursive Mono & Sans, by Arrow Type

Recursive is a typographic palette for code & UI. It includes sans-serif & mono fonts designed specifically for use in interactive applications and code editors. See https://recursive.design for more information.

Recursive is an open-source project. Follow along and contribute at https://github.com/arrowtype/recursive. It is licensed under the OFL, so (in summary) you are free to make derivative versions, but these must also adopt the same OFL license (e.g. you cannot sell proprietary licenses for derivative fonts). See `LICENSE.txt` for full details.

Do you have a question or have you found a bug? Please file an issue at https://github.com/arrowtype/recursive/issues. Thanks!

## Recommendations

For design & usage recommendations, please see the project README at https://github.com/arrowtype/recursive.

Fonts in `Recursive_Desktop` and `Recursive_Code` are made so that it is possible to install all of these without experiencing conflicts in font menus. However, you may want to pick-and-choose which font files you wish to install, based on your needs.

### General Desktop use (Word, PowerPoint, Keynote, InDesign, Illustrator, PhotoShop, Figma, etc)

- On Windows, install `Recursive_Desktop/recursive-statics.ttc` (This is a collection of all 64 static instances in TTF format)
- On Mac, install `Recursive_Desktop/recursive-statics.otc` (This is a collection of all 64 static instances in OTF format)

### Desktop web design (Sketch) & experimental use in Adobe apps

- Install `Recursive_Desktop/Recursive_VF_1.0XX.ttf` (this is the full Recursive variable font)
- It may also be beneficial to install static fonts, as OS & app support of variable fonts is still growing

### Code (code editors such as VS Code, Atom, Sublime, etc etc)

- Install fonts in `Recursive_Code` (These are specifically simplified families for use in code editors. See README in that directory for further advice)

### Web

- Use the woff2 font files in `Recursive_Web`. This includes a few useful subsets for variable fonts, along with some starter `@font-face` CSS for the `woff2_variable_subsets`.
- If you only need a style or two on a site, it may be practical to just use static instances, but you may want to figure out subsetting with `pyftsubset` to make those even smaller.
