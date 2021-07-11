def getWords():
    f = open("words.txt", "r")
    words = f.readlines()
    f.close()
    for i in range(len(words)):
        words[i] = words[i].rstrip()
    return words

words = getWords()
alphabet = "abcdefghijklmnopqrstuvwxyz"

def getOutputs(word):
    results = []
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
    return results

def findIt(start, end, path = []):
    try:
        nextWords = getOutputs(start)
    except KeyError:
        return False
    if end in nextWords:
        return end
    else:
        for word in nextWords:
            if word not in path:
                path.append(word)
                hmm = findIt(word, end, path)
                if not hmm:
                    continue
                else:
                    return word + " " + hmm
            else:
                continue
        return False



startingWord = "ran"
endingWord = "cab"

print(startingWord + " " + findIt(startingWord, endingWord))

#instead of finding one and doing it, find all, add all to list, then find all from there and so on 

#current output:
# ran an ban bean ben be abe babe babel abel
# bel bell ell cell cello hello hell shell
# sell smell smells sells ells lls ills ill
# bill bills fills fill frill rill drill dill
# dilly billy filly frilly frills rills drills
# grills gills gill grill grille grilled drilled
# frilled filled filed fled led bled bed bred
# red re are bare bar bear ear dear drear rear
# rearm ream ram am cam cab
