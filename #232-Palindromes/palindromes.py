#Palindromes Challenge
#Graeme Cliffe

ignoredChars="?!. ,"
def main():
    numLines=int(raw_input())
    lines=[]
    for x in range(0,numLines):
        lines.append(raw_input())
    lineString=''.join(x for x in str(''.join(lines)).lower() if x not in ignoredChars)
    reversedString=lineString[::-1]
    if reversedString==lineString:
        print "PALINDROME"
    else:
        print "NOT PALINDROME"

main()
