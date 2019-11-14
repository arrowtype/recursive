# OpenType Features

Features are primarily written in individual files, then included in `features.fea`.

Current process: I'm just copying the `features` folder into varfont-prepped directories, then using `src/00-recursive-scripts-for-robofont/clean-up/add-feature-code-to-selected_fonts.py` to add in this main `features.fea` file.