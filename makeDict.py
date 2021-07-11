import time

def getWords():
    print("Retrieving Words")
    gettingWords = time.time()
    f = open("words.txt", "r")
    words = f.readlines()
    f.close()
    for i in range(len(words)):
        words[i] = words[i].rstrip()
    print("Retrieved Words", time.time()-gettingWords)
    return words

words = getWords()
alphabet = "abcdefghijklmnopqrstuvwxyz"

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


            

#Consider not constraining to words to know which is best
            
#Divide and conquer
#Amount of steps to get from word1 to word2 no word requirement

#Get all valid words that are off by one and not in seenWords
def getWordsToCheck(startingWords, seenWords, order):
    wordsToCheck = {}
    for word in startingWords:
        neighbors = getOutputs(word)
        for neighbor in neighbors:
            if neighbor not in seenWords:
                if order:
                    wordsToCheck[neighbor] = startingWords[word] + word + " "
                else:
                    wordsToCheck[neighbor] = word + " " + startingWords[word]
    return wordsToCheck


def findLongest(startingWords, seenWords = [""]):
    wordsToCheck = getWordsToCheck(startingWords, seenWords)
    
    if len(wordsToCheck) == 0:
        return "END"
    else:
        print(len(wordsToCheck))
    
    seenWords.extend(list(wordsToCheck.keys()))
    x = findLongest(wordsToCheck, seenWords)
    if x == "END":
        return wordsToCheck
    else:
        return x


#print(findLongest({"card" : ""}))

def find(startingWords, endWord, seenWords):
    wordsToCheck = getWordsToCheck(startingWords, seenWords)
    
    if endWord in wordsToCheck:
        
        return wordsToCheck[endWord] + endWord
    else:
        print(len(wordsToCheck))
        if len(wordsToCheck) == 0:
            return "END"
            
        seenWords.extend(list(wordsToCheck.keys()))
        x = find(wordsToCheck, endWord, seenWords)

        if x == "END":
            
            return wordsToCheck
        else:
            return x

def common_member(a, b): 
    a_set = set(a) 
    b_set = set(b) 
    if (a_set & b_set): 
        return (a_set & b_set) 
    else: 
        return False

def doubleFind(startWords, endWords, seenStartWords, seenEndWords):
    leftWTC = getWordsToCheck(startWords, seenStartWords, True)

    x = common_member(leftWTC, endWords)
    if x:
        x = list(x)[0]
        end = time.time()
        print(end-start)
        return (leftWTC[x] + x + " " + endWords[x])
    
    rightWTC = getWordsToCheck(endWords, seenEndWords, False)
    print(len(leftWTC), " ", len(rightWTC))
    if len(rightWTC) == 0:
        return False
    x = common_member(leftWTC, rightWTC)
    if x:
        x = list(x)[0]
        end = time.time()
        print(end-start)
        return (leftWTC[x] + x + " " + rightWTC[x])
    else:
        seenStartWords.extend(list(leftWTC.keys()))
        seenEndWords.extend(list(rightWTC.keys()))
        return doubleFind(leftWTC, rightWTC, seenStartWords, seenEndWords)
    


def smartFind(startWords, endWords, seenStartWords, seenEndWords, i):
    correctWords = endWords
    correctSeenWords = seenEndWords
    otherWords = startWords
    otherSeenWords = seenStartWords
    order = False

    if len(startWords) < len(endWords): #Start with the list of words thats shorter
        correctWords = startWords
        correctSeenWords = seenStartWords
        otherWords = endWords
        otherSeenWords = seenEndWords
        order = True
        
    if len(startWords) == 0 or len(endWords) == 0:
        return False
    
    wtc = getWordsToCheck(correctWords, correctSeenWords, order)

    i += 1
    print("Step ", i, " ", round(time.time()-start, 2))
    
    if len(wtc) == 0:
        return False
    
    x = common_member(wtc, otherWords)
    if x:
        x = list(x)[0]
        print(round(time.time()-start, 2))
        return wtc[x] + x + " " + otherWords[x]
    else:
        correctSeenWords.extend(list(wtc.keys()))
        if order:
            return smartFind(wtc, otherWords, correctSeenWords, otherSeenWords, i)
        else:
            return smartFind(otherWords, wtc, otherSeenWords, correctSeenWords, i)

start = time.time()
print(smartFind({"stunning" : ""}, {"a" : ""}, [""], [""], 0))
#print(getWordsToCheck({"expert" : ""}, [""], True))
#instead of finding one and doing it, find all, add all to list, then find all from there and so on 
