#Consonants and Vowels Challenge
#Graeme Cliffe

from random import choice

def main():
    strDict={'c':"bcdfghjklmnpqrstvwxyz",'v':"aeiou"}
    strDict['C'],strDict['V']=strDict['c'].upper(),strDict['v'].upper()
    print ''.join((choice(strDict[j])) for j in raw_input() )

main()
