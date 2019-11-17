from defcon import Font
from cu2qu.ufo import fonts_to_quadratic

casual_a = Font('src/masters--quadratic_production/experiments--curvier-casual/Recursive Mono-Casual A.ufo')
casual_a_ital = Font('src/masters--quadratic_production/experiments--curvier-casual/Recursive Mono-Casual A Italic - gradually fixed.ufo')
casual_b = Font('src/masters--quadratic_production/experiments--curvier-casual/Recursive Mono-Casual B.ufo')
casual_b_ital = Font('src/masters--quadratic_production/experiments--curvier-casual/Recursive Mono-Casual B Italic - gradually fixed.ufo')

# fonts_to_quadratic([casual_a, casual_a_ital, casual_b, casual_b_ital])

for font in [casual_a, casual_a_ital, casual_b, casual_b_ital]:
    fonts_to_quadratic([font])