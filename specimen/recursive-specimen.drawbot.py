file_object = open("./drawbot-drawing-tools.txt", 'r')

codeExample = file_object.read()

# print(codeExample)

import random

newPage('A4')
# rect(1,1,593,840)
W,H = 595,842


glyphsToRemove = '" ( ) { } [ ] _ . ; = > < ? : , / - ` \' '

glyphsToRemoveList = glyphsToRemove.split(' ')

cleanedCodeExample = ''

for letter in codeExample:
    if letter in glyphsToRemoveList:
        cleanedCodeExample += ' '
    else:
        cleanedCodeExample += letter

codeWords = set(cleanedCodeExample.replace('\n', ' ').split(' '))

# print(codeWords)

wordsToRemove = ['', 'aabcde1234567890', 'A4Landscape']

for word in wordsToRemove:
    if word in codeWords:
        codeWords.remove(word)

minWordLength = 3
maxWordLength = 14

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

# print(sortedByLengthSorted)

textBoxes = len(sortedByLengthSorted.keys())

# print(textBoxes)
boxHeight = H / textBoxes * 1.25

# print(boxHeight)

def chooseRandomWord(list):
    listLength = len(list)
    item = random.randint(0, listLength-1)
    return list[item]



minFontSize = 21.32
maxFontSize = 92

def currentFontSize(minSize,maxSize,t):
    totalRange = maxSize - minSize
    currentSize = maxSize - (totalRange * t)
    return currentSize
    
counter = 0
for num in range(minWordLength,maxWordLength):
    # print(num)
    if num in sortedByLengthSorted.keys():
        t = (num - minWordLength) / (maxWordLength - minWordLength)
        # print(t)
        currentSize= currentFontSize(minFontSize,maxFontSize,t)
        print(currentSize)
        fontSize(currentSize)
        font("RecursiveMono-CasualMedium")
        # choose a random word from list
        wordToDraw = chooseRandomWord(sortedByLengthSorted[num])
        print(wordToDraw)
        textBox(wordToDraw,(0,H-boxHeight*counter,W,boxHeight))  
        counter += 1
        
    # textBox(sortedByLength[num],(0,H-boxHeight*index,W,boxHeight))

# textBox(words, (100,500,1200,1000))






file_object.close()