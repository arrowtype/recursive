# Variable font axis splitting notes

Generally, a variable font's filesize is about:

```
(the size of a single font) × (number of masters required)
```

In Recursive, each static instance woff2 is around 40kb.

| File                                            | Description                          | Masters | Size     |
| ----------------------------------------------- | ------------------------------------ | ------- | -------: |
| recursive--MONO_0_1.woff2                       | Just the Monospace axis              | 2       |  `62 KB` |
| recursive--CASL_0_1.woff2                       | Just the Casual axis                 | 2       |  `88 KB` |
| recursive--slnt_0_15.woff2                      | Slant 0 to -15 (mono 0)              | 2       |  `83 KB` |
| recursive--slnt_0_15-mono_1.woff2               | Slant 0 to -15 (mono 1)              | 2       |  `82 KB` |
| recursive--wght_300_800.woff2                   | Weight 300–800                       | 2       |  `80 KB` |
| recursive--wght_300_1000.woff2                  | Weight 300–1000                      | 3       | `112 KB` |
| recursive--wght_300_800-mono_0_1.woff2          | Weight 300–800, plus Monospace axis  | 4       | `164 KB` |
| recursive--wght_300_1000-mono_0_1.woff2         | Weight 300–1000, plus Monospace axis | 4       | `239 KB` |
| recursive--wght_300_800-slnt0_15.woff2          | Weight 300–800, Slant, Ital 0.5      | 4       | `135 KB` |
| recursive--wght_300_800-slnt0_15-ital_0.woff2   | Weight 300–800, Slant, Ital 0        | 4       | `135 KB` |
| recursive--wght_300_1000-slnt0_15.woff2         | Weight 300–1000, Slant, Ital 0.5     | 6       | `194 KB` |

Note: subsetting `ital` makes no filesize difference – all these alternate glyphs must be remaining in the partial font.

## Process

I'm using this script to run `fontTools.instancer`: 

https://github.com/arrowtype/recursive/blob/dfe7a4569cdf0b599f5bfb1ac79d973cd2c7fdcf/src/build-scripts/instancing/partial-instance-tests.py