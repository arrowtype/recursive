# ------------------------------------------------------------------------------
# set up variables -------------------------------------------------------------

folderToGet = '../../../../Users/stephennixon/Environments/gfonts3/lib/python3.6'
fileToSave = 'specimen/pythonCodeExamples.py'

minWordLength = 2
maxWordLength = 45

# ------------------------------------------------------------------------------
# set up basics ----------------------------------------------------------------

from pathlib import Path

f= open(fileToSave,"w+")

codeExample= ""

# ------------------------------------------------------------------------------
# get text and add to string ---------------------------------------------------

pathlist = Path(folderToGet).glob('**/*.py')

for path in pathlist:
    # because path is object not string
    path_in_str = str(path)
    # print(path_in_str)

    file_object = open(path_in_str, 'r', encoding='utf-8')
    codeExample += file_object.read()

# ------------------------------------------------------------------------------
# clean up string --------------------------------------------------------------

glyphsToRemove = '" ( ) { } [ ] _ . ; = > < ? : , / - ` \ \' ^ @ 1 2 3 4 5 6 7 8 9 0'

glyphsToRemoveList = glyphsToRemove.split(' ')

cleanedCodeExample = ''


for letter in codeExample:
    if letter in glyphsToRemoveList:
        cleanedCodeExample += ' '
    else:
        cleanedCodeExample += letter

codeWords = set(cleanedCodeExample.replace('\n', ' ').replace('\t','').split(' '))

# print(codeWords)

wordsToRemove = ['',' ', '  ', '   ', '\t', 'aabcde1234567890', 'A4Landscape', 'molestie', 'vvvvvvvvvvvvvvvvvvvv', 'eEfFgGdiouxXcrs%',  'математика', 'numOps','bFamilyType','cmapLoading', 'ranges','bestDefault','compressedData']

for word in wordsToRemove:
    if word in codeWords:
        codeWords.remove(word)


sortedByLength = {}

for index, word in enumerate(codeWords):
    # print(word)
    if len(word) >= minWordLength and len(word) <= maxWordLength:
        if len(word) not in sortedByLength.keys():
            sortedByLength[len(word)] = []
        if len(word) in sortedByLength.keys():
            sortedByLength[len(word)].append(word)
            
sortedByLengthSorted = {}

for i in range(minWordLength,maxWordLength+1):
    if i in sortedByLength.keys() and i % 1 == 0:
        sortedByLengthSorted[i] = sortedByLength[i]

# ------------------------------------------------------------------------------
# write to file ----------------------------------------------------------------

f.write('sortedByLengthSorted = ' + str(sortedByLengthSorted))

f.close()
