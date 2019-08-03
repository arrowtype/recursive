from distutils import text_file

f = open('/Users/stephennixon/type/01-casual_mono-project/glyph-recipes/diacritic-recipes-for-underware_latin_plus-comb_names.txt', "r")

recipes = f.read()

print(recipes)

lines = recipes.split("\n")

sortedLines = sorted(lines)

print(sorted(lines))

f2 = open('sorted-recipes.txt', "w")

for line in sortedLines:
    if line != "" and line[0] != "#":
        f2.write(line + "\n")

f.close()
f2.close()