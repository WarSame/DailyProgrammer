#A Game Of Threes Challenge
#Graeme Cliffe

num=int(raw_input())
while num!=1:
    print num,
    if num%3==0:
        print "0"
        num/=3
    elif num%3==1:
        print "-1"
        num-=1
    elif num%3==2:
        print "+1"
        num+=1

print num
