from random import randint

thisdict = {
    "brand":6, #6/100
    "model":25, #25/100
    "year":50, #50/100
    "yoda":19, #19/100

}


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

# counts = {}
# for i in range(10000):
#     word = nextWord(thisdict)
#     if word in counts:
#         counts[word] += 1
#     else:
#         counts[word] = 1
# print(counts)

# a = ['day','pay','may','bay']
a = ['day']

def getKey(backwards,n):
    length = len(backwards)
    key = (backwards[length-n],)
    for i in range(n-1,0,-1):
        key = key + (backwards[length-i],)
    return key

print(getKey(a,1))

backWords = ['a','b','c','d']
newWord = 'e'
for i in range(len(backWords)-1):
    backWords[i] = backWords[i+1]
backWords[-1] = newWord
print(backWords)