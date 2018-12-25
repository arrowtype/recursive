file_object = open("./drawbot-drawing-tools.txt", 'r')
codeExample = file_object.read()

file_object_2 = open("./drawbot-misc.txt")
codeExample += file_object_2.read()

# print(codeExample)

import random
import math

# A4 page size is 595, 842
# rect(1,1,593,840)
W,H = 595,842

glyphsToRemove = '" ( ) { } [ ] _ . ; = > < ? : , / - ` \' 1 2 3 4 5 6 7 8 9 0'

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
        
padding = 60

minWordLength = 8
maxWordLength = 20
textColumnWidth = W-padding*2

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

def currentFontSize(minSize,maxSize,t):
    totalRange = maxSize - minSize
    currentSize = (maxSize - (totalRange * t)) #/ 1.36 * math.tan(1+t)
    return currentSize
    

# width = 0.6 * currentSize * numOfLetters    
## set font size to whatever is needed to match width of first thing

# width = 500 = 0.6 * currentSize * 3
# currentSize = 0.6/500 * 3/500



def calcFontSize(currentLetters, t):
    currentSize = textColumnWidth / currentLetters / 0.6      
    return currentSize
    
font("RecursiveMonoVar-StrictLight")

for axis, data in listFontVariations().items():
    print((axis, data))

pages = 5

minWght = 300
maxWght = 1100

weightSteps = int((maxWght - minWght)/100)

currentWght = 300
currentXprn = 0.99

for page in range(0,weightSteps):
    newPage(W,H)
    counter = 0
    currentHeight = 0
    
    
    
    for num in range(minWordLength,maxWordLength):
        # print(num)
        if num in sortedByLengthSorted.keys():
            t = (num - minWordLength) / (maxWordLength - minWordLength)
            # print(t)
            # currentSize= currentFontSize(minFontSize,maxFontSize,t)
            currentLetters = num
            currentSize = calcFontSize(currentLetters, t)
            # print(currentSize)
            fontSize(currentSize)
            lineHeight(currentSize)
            
            font("RecursiveMonoVar-StrictLight")
            fontVariations(wght=currentWght, XPRN=currentXprn)
            
            
            # choose a random word from list
            wordToDraw = chooseRandomWord(sortedByLengthSorted[num])
            
            if len(sortedByLengthSorted[num]) > 1:
                sortedByLengthSorted[num].remove(wordToDraw)
            # print(wordToDraw)
            textBox(wordToDraw,(padding, H-currentHeight-currentSize-30, W, currentSize*1.1)) 
        
            currentHeight += currentSize*1.05
            counter += 1
    currentWght += 100
        
    # textBox(sortedByLength[num],(0,H-boxHeight*index,W,boxHeight))

# textBox(words, (100,500,1200,1000))






file_object.close()