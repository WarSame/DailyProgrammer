#Broken Keyboard Challenge - Short
#Graeme Cliffe

letters=set(raw_input())#allowed letters
f=open('../enable1.txt', 'r')
a=[w for w in f.read().split() if set(w)<=letters]
a=sorted(a,key=len)

print a[-1]
