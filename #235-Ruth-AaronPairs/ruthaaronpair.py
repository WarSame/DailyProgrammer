#Ruth Aaron Challenge
#Graeme Cliffe

def findFactors(n):
    factors=set()
    f=2
    while n!=1:
        while (n%f)==0:
            factors.add(f)
            n/=f
        f+=1
    return factors

def readInput():
    pairs=[]
    for i in range(0,int(raw_input("Enter number of pairs:"))):
        pair = raw_input().strip("(").strip(")")
        pairSplit = [int(n) for n in pair.split(",")]
        pairs.append(pairSplit)
    return pairs

def main():
    pairs=readInput()
    for i in pairs:
        fact1=findFactors(i[0])
        fact2=findFactors(i[1])
        print i,
        print "VALID" if (abs(i[0]-i[1])==1 and sum(fact1)==sum(fact2)) else "NOT VALID"

main()
