#Palindrome Challenge Bonus
#Graeme Cliffe

def main():
    f=open("../enable1.txt","r")
    lines=list(x.strip("\n") for x in f.readlines())
    f.close()
    for line in lines:
        for line2 in lines:
            if len(line)==len(line2) and line==''.join(list(reversed(line2))):
                print line, line2

main()
