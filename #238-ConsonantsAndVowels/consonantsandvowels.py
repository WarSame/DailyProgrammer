#Consonants and Vowels Challenge
#Graeme Cliffe

import random

def randChar(formatChar):
    vow=list("aeiou")
    con=list("bcdfghjklmnpqrstvwxyz")
    vowUp=list(c.upper() for c in vow)
    conUp=list(c.upper() for c in con)
    strDict={'c':random.choice(con), 'C':random.choice(conUp),
             'v':random.choice(vow), 'V':random.choice(vowUp)}
    return strDict.get(formatChar) or 'ERROR'

def main():
    outstring=[]
    for i in raw_input():
        outstring.append(randChar(i))
    print ''.join(outstring)

main()
