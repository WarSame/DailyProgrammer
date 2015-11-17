#Vampire Numbers Challenge
#Graeme Cliffe

import itertools, operator, math

def combo(s,v):#alias function
    return itertools.combinations_with_replacement(s,v)

def findLims(numDig):#range of a number with numDig digits
    return 10**(numDig-1),10**(numDig)

def numDigits(n):#number of digits of a number
    return int(math.log10(n))+1

def main():
    numDig, numFang=map(int,raw_input().split())
    #vampire can be in this range
    vampBot,vampTop=findLims(numDig)
    fangBot,fangTop=findLims(numDig/numFang)
    vampires={}#dict containing all vampires in vamprange
    for fang in combo(range(fangBot,fangTop),numFang):
        #combo for 10 to 99 returns 10,11,12,etc.
        #multiply the combination values together
        vampire=reduce(operator.mul,fang)
        vampLen=numDigits(vampire)
        if vampLen!=numDig:
            continue
        #remove double trailing zeros vampires
        if str(vampire)[-2:] == "00":
            continue
        #get ordered list of numbers to compare
        fangDig=sorted(''.join(map(str,fang)))
        vampDig=sorted(str(vampire))
        if fangDig == vampDig:
            #if numbers match, store in dict
            vampires[vampire]=fang
    for v,f in sorted(vampires.items()):
        print "{}={}".format(v,'*'.join(map(str,f)))

main()
