#Broken Keyboard Challenge - Shortest
#Graeme Cliffe

i=set(raw_input()); print sorted([w for w in open('enable1.txt','r').read().split()
                                  if all(c in i for c in set(w))], key=len)[-1]
