import time
import json

#read the dictionary
with open('theDictionary.txt') as json_file:
    gettingWords = time.time()
    data = json.load(json_file)
    print("Retrieved Words", time.time()-gettingWords)


words = data.keys()
alphabet = "abcdefghijklmnopqrstuvwxyz"

#find all words that are 1 Levenshtein distance away from the given word
#a brute-force method that tries every possible string and checks if it is a word
def getOutputs(word):
    results = [word]
    for i in range(len(word)): #remove a letter
        newWord = word[:i] + word[i+1:]
        if newWord in words and newWord not in results:
            results.append(newWord)
    for i in range(len(word)+1): #add a letter
        for j in alphabet:
            newWord = word[:i] + j + word[i:]
            if newWord in words and newWord not in results:
                results.append(newWord)
    for i in range(len(word)): #change a letter
        for j in alphabet:
            newWord = word[:i] + j + word[i+1:]
            if newWord in words and newWord not in results:
                results.append(newWord)
    return results[1:]

#Get all valid words that are off by one and not in seenWords
def getWordsToCheck(startingWords, seenWords, order):
    wordsToCheck = {}
    for word in startingWords:
        try:
            neighbors = data[word]
        except KeyError:
            neighbors = getOutputs(word)
        for neighbor in neighbors:
            if neighbor not in seenWords:
                if order:
                    wordsToCheck[neighbor] = startingWords[word] + word + " "
                else:
                    wordsToCheck[neighbor] = word + " " + startingWords[word]
    return wordsToCheck

#find the common elements in two lists
def intersect(a, b): 
    a_set = set(a) 
    b_set = set(b) 
    if (a_set & b_set): 
        return (a_set & b_set) 
    else: 
        return False

#The recursive function with accumulators to loop until a path is found or 
# all paths are proven to be dead-ends, uses an adapted breadth-first search
def smartFind(startWords, endWords, seenStartWords, seenEndWords, i, startTime, s, e):
    cWords = startWords
    cSeenWords = seenStartWords
    cw = s
    oWords = endWords
    oSeenWords = seenEndWords
    ow = e
    order = True

    if len(startWords) > len(endWords): #Start with the list of words thats shorter
        cWords = endWords
        cSeenWords = seenEndWords
        cw = e
        oWords = startWords
        oSeenWords = seenStartWords
        ow = s
        order = False
        
    if len(startWords) == 0 or len(endWords) == 0:
        return False
    
    wtc = getWordsToCheck(cWords, cSeenWords, order)
    i += 1
    print("Step " + str(i), str(len(wtc)) + " words", round(time.time()-startTime, 2))
    
    if len(wtc) == 0:
        return False
    
    x = intersect(wtc, oWords)
    if x:
        x = list(x)[0]
        print(round(time.time()-startTime, 2))
        result = [];
        if order:
            result = wtc[x] + x + " " + oWords[x]
        else:
            result = oWords[x] + x + " " + wtc[x]
        return result[:-1] #.split(" ")
    else:
        cSeenWords.extend(list(wtc.keys()))
        if order:
            return smartFind(wtc, oWords, cSeenWords, oSeenWords, i, startTime, s, e)
        else:
            return smartFind(oWords, wtc, oSeenWords, cSeenWords, i, startTime, s, e)

#The main find function that can take in a series of words and find the path between them if it exists
def find(*argv):
    startingTime = time.time()
    if len(argv) == 0:
        return None
    elif len(argv) == 1:
        return agrv[0]
    else:
        for i in range(len(argv)-1):
            print(smartFind({argv[i] : ""}, {argv[i+1] : ""}, [""], [""], 0, startingTime, argv[i], argv[i+1]))
        


#This function is based on find, to identify the word in the english language that is farthest from the given word
def findLongest(startingWords, seenWords = [""]):
    wordsToCheck = getWordsToCheck(startingWords, seenWords, True)
    
    if len(wordsToCheck) == 0:
        return "END"
    else:
        seenWords.extend(list(wordsToCheck.keys()))
        x = findLongest(wordsToCheck, seenWords)
        
    if x == "END":
        return wordsToCheck
    else:
        return x
