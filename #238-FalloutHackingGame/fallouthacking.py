#Fallout Hacking Game Challenge
#Graeme Cliffe

import random
totalGuesses=4

def getWordList(wordLen,numWord):#returns randomized words from enable1.txt
    wordList=[]
    f=open("../enable1.txt","r")

    for line in f.readlines():#pull numWord words of wordLen length
        lineclean=line.strip("\n")
        if len(lineclean)==wordLen:
            wordList.append(lineclean.upper())
    f.close()
    return random.sample(wordList,numWord)

def getGuess(currGuesses):#print number of guesses left while asking for input
    return raw_input("Guess ("+str(totalGuesses-currGuesses)+" left)? ").upper()

def findMatches(guess,answer):#find number of shared letters between words
    numMatches=0
    for i in range(0,len(answer)):
        if guess[i]==answer[i]:
            numMatches+=1
    return numMatches

def main():
    difLev=int(raw_input("Difficulty (1-5)? "))
    difMod={1:(4,5,6),2:(7,8),3:(9,10,11),4:(12,13),5:(14,15)}
    wordLen,numWord=random.choice(difMod[difLev]),random.choice(difMod[difLev])
    #get list of numWord random words of wordLen from enable1.txt
    wordList=getWordList(wordLen,numWord)
    for i in wordList:
        print i
    password=random.choice(wordList)
    for i in range(0,totalGuesses):#iterate through their allowed guesses
        currGuess=getGuess(i)
        while currGuess not in wordList:#if the guess isn't allowed
            print "Not a valid option."
            currGuess=getGuess(i)
        if currGuess==password:#if the guess is right
            print str(len(currGuess))+"/"+str(len(password))+" correct"
            print "You win!"
            break
        else:#if the guess is off
            numMatches=findMatches(currGuess,password)
            print str(numMatches)+"/"+str(len(password))+" correct"
            if (i==totalGuesses-1):
                print "You lose!"
                print "The correct answer was",password
    
main()
