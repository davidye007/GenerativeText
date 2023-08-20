import random
from random import randint
# MAX_N = 4
nGrams = {}
corpus = []

# names = ['corpus', 'DownAndOutInTheMagicKingdom','RomeoAndJuliet','TheOdyssey', 'TheDisciple','PeterPan','TheWizardOfOz',
#          'LambToTheSlaughter','CNN_Walmart','LoveStoryTS','NPRSubway','SongMix','LadyGaga','PickupLines','Jokes']

names = ['RomeoAndJuliet','TheOdyssey','PeterPan','LoveStoryTS','NPRSubway','CNN_Walmart','SongMix','LadyGaga','PickupLines','Jokes']

with open(names[1]+".txt", "r", encoding="utf-8") as f:
    for line in f.readlines():
        for word in line.split(" "):
            if len(word) == 0:
                continue
            corpus.append(word.strip())

def train(corpus):
    # TODO: Populate the nGrams variable based on the corpus.
    for i in range(len(corpus) - MAX_N - 1):
        for n in range(1, MAX_N+1):
            key = tuple(corpus[i:i+n])
            value = corpus[i+n]
            if key not in nGrams:
                nGrams[key] = {}
            if value not in nGrams[key]:
                nGrams[key][value] = 0
            nGrams[key][value] += 1

def nextWord(dict):
    total = 0
    counter = 0
    for x in dict:
        total += dict[x]
    num = randint(1, total)
    for x in dict:
        counter += dict[x]
        if num <= counter:
            return x

def getKey(backwards,n):
    length = len(backwards)
    key = (backwards[length-n],)
    for i in range(n-1,0,-1):
        key = key + (backwards[length-i],)
    return key

def generateText(initialWord, numWords):
    wordsGenerated = 0
    backWords = [initialWord]
    genText = initialWord # text to return
    n = 1 # n-gram
    # Prior to Backoff Smoothing
    while wordsGenerated < MAX_N - 1:
        key = getKey(backWords,n) # n-gram
        if key not in nGrams and wordsGenerated == 0:
            raise Exception("Invalid initial input. Please use a different initial input.")
        # add exception if initial word not in text
        freqTable = nGrams[key] # frequency table
        newWord = nextWord(freqTable) # new word
        genText += (" " + newWord) # append new word to text
        backWords.append(newWord) # append new word to backWords
        wordsGenerated+=1 # index words generated
        n+=1 # index n-gram

    while wordsGenerated < numWords:
        # Backoff Smoothing
        key = getKey(backWords,n) # n-gram
        # while key does not exist in nGrams decrement n
        # (i.e. if n decrements, gets new word, and now n = N n-gram does not exist in text)
        while key not in nGrams:
            n -=1
            key = getKey(backWords,n)
        freqTable = nGrams[key] # frequency table
        total = 0
        for x in freqTable:
            total += freqTable[x]
        num = randint(1, total+1)
        if (num == 1) and n!=1: # probability of backoff
            n-=1
        else:
            newWord = nextWord(freqTable) # new word
            genText += (" " + newWord) # append new word to text
            for i in range(len(backWords)-1): # shift backWords left
                backWords[i] = backWords[i+1]
            backWords[-1] = newWord # add new word to end of backWords
            wordsGenerated+=1 # index words generated
            print(n)
            n = MAX_N # set n to MAX_N
    return genText

MAX_N = 16
train(corpus)
initialInput = "Sail"
numWordsToGenerate = 50
generatedText = generateText(initialInput, numWordsToGenerate)

print("Generated Text: " + generatedText)
