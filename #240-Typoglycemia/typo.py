#Typoglycemia Challenge
#Graeme Cliffe

import random, string
def scrambleWord(word):
    #Given a word, scramble it except the first and last char
    #Don't move punctuation
    wordLen=len(word)
    if wordLen<3:
        return word
    scrambleWord=[None]*wordLen
    scrambleWord[0],scrambleWord[wordLen-1]=word[0],word[wordLen-1]
    interiorLetters=[x for x in word[1:-1] if x not in string.punctuation]
    for x in range(1,wordLen-1):
        currChar=word[x]
        if currChar in string.punctuation:
            scrambleWord[x]=currChar
        else:
            scrambleWord[x]=random.choice(interiorLetters)
            interiorLetters.remove(scrambleWord[x])
    return ''.join(scrambleWord)

wordArray=[scrambleWord(x) for x in str(raw_input()).strip("\n").split(" ")]
print ' '.join(wordArray)
