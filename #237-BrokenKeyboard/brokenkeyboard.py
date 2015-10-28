#Broken Keyboard Challenge - Daily Programmer
#Graeme Cliffe

import sys, string

def findLongestWord(keyboard):
    #pull all words
    f = open('../enable1.txt', 'r')
    longestWord=""
    #only allow letters from the keyboard to be used
    disallowedLetters=set(string.lowercase) - set(keyboard)
    for word in f.readlines():
        word=word.strip("\n")
        if (len(disallowedLetters)>len(disallowedLetters-set(word))):
            #if it has non-keyboard letters, don't count the word
            continue
        if (len(word)<=len(longestWord)):
            #if it doesn't beat our current record
            continue
        #if it passes both criteria then it is the longest word
        #for this keyboard so far
        longestWord=word
    f.close()
    return longestWord

def getInput():
    #take user input of valid keyboards
    numLines=int(sys.stdin.readline())
    keyboards=[]
    for i in range(0,numLines):
        keyboards.append(sys.stdin.readline().strip("\n"))
    return keyboards

def main():
    keyboards = getInput()
    for i in keyboards:
        result=findLongestWord(i)
        print("{0} = {1}".format(i,result))
    
main()
