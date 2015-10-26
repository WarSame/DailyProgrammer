#Ruth Aaron Challenge
#Graeme Cliffe

def findFactors(n):
    factors=[]
    f=2
    while n!=1:
        if (n%f)==0:
            factors.append(f)
            n/=f
        else:
            f+=1

    return factors

def readInput():
    numPairs=int(raw_input("Enter number of pairs:"))
    pairs=[]
    for i in range(0,numPairs):
        pair = raw_input().strip("(").strip(")")
        pairSplit = [int(n) for n in pair.split(",")]
        pairs.append(pairSplit)
    return pairs

def main():
    pairs=readInput()
    for i in pairs:
        fact1=findFactors(i[0])
        fact2=findFactors(i[1])
        print fact1
        print fact2
        print i,
        print "VALID" if (abs(i[0]-i[1])==1 and sum(fact1)==sum(fact2)) else "NOT VALID"

main()
