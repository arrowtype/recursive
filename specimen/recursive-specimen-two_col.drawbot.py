# file_object = open("./drawbot-drawing-tools.txt", 'r')
# codeExample = file_object.read()

# file_object_2 = open("./drawbot-misc.txt")
# codeExample += file_object_2.read()

import os
import random
import math

from pythonCodeExamples import sortedByLengthSorted

W,H = 595, 842
padding = 150

minWordLength = 8
maxWordLength = 30
textColumnWidth = W-padding*2


textBoxes = len(sortedByLengthSorted.keys())

# print(textBoxes)
boxHeight = H / textBoxes * 1.25

# print(boxHeight)

def chooseRandomWord(list):
    listLength = len(list)
    item = random.randint(0, listLength-1)
    return list[item]
    
def calcFontSize(currentLetters, t):
    # textColumnWidth += textColumnWidth * (1 - t)
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
currentXprn = 1

for page in range(0,weightSteps*2):
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
            print(currentSize)
            fontSize(currentSize)
            lineHeight(currentSize)
            
            font("RecursiveMonoVar-StrictLight")
            fontVariations(wght=currentWght, XPRN=currentXprn)
            
            
            # choose a random word from list
            wordToDraw = chooseRandomWord(sortedByLengthSorted[num])
            
            # if len(sortedByLengthSorted[num]) > 1:
            #     sortedByLengthSorted[num].remove(wordToDraw)
            # print(wordToDraw)
            textBox(wordToDraw,(padding, H-currentHeight-currentSize-padding/2, W, currentSize*1.1)) 
        
            currentHeight += currentSize*1.1
            counter += 1
    currentWght += 100
    if currentWght == maxWght:
        currentWght = minWght
        currentXprn = 0.001
        
    # textBox(sortedByLength[num],(0,H-boxHeight*index,W,boxHeight))

# textBox(words, (100,500,1200,1000))




saveImage('exports/recursive-mono-030319.pdf')


