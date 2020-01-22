from pythonCodeExamplesList import sortedByLengthSorted
import os

path = "/Users/stephennixon/type-repos/recursive/src/proofs/drawbot-specimens-and-diagrams/drawbot-specimen--monospace_columns/python-sorted-string.txt"

# words = " ".join(sortedByLengthSorted)
words = ""

for word, i in enumerate(sortedByLengthSorted):
	words += f"{sortedByLengthSorted[i]}" 

with open(path, 'w') as file:
    file.write(words)
    print('saved to ', str(path)) 