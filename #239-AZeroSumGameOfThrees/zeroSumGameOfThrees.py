#A Zero-Sum Game Of Threes Challenge
#Graeme Cliffe

children=[-2,-1,1,2]

def dfsChildren(parentRunTot,parentSum):#spin children off of parent node
    #print "Checking children"
    for childVal in children:#Attempt all of the children branches
        print "New child: parent value total=",parentRunTot
        print "Childval is",childVal
        
        childSum=parentSum+childVal
        childRunTot=parentRunTot+childVal
        
        retBool,additionList=dfs(childRunTot,childSum)

        if retBool:#If this child returns True, then append and return up
            print "Returning",additionList
            additionList.append(childVal)
            return True, additionList
    print "No case matched"
    return False,0#No case matched

#Use a DFS. If we reach more than 3*initial number a solution is impossible
def dfs(parentRunTot,parentSum):
    print "=====Entering dfs====="
    print "Current value is",parentRunTot
    print "Current sum is",parentSum
    if parentRunTot==1:
        if parentSum==0:
            #If we have hit the base case
            print "Base case"
            baseList=list()
            baseList.append(0)
            return True,baseList
        return False,0#End of branch
    if parentRunTot>3*initNum:
        #If we reach too high, end this child
        print "Too high"
        return False,0
    if parentRunTot<1:
        #If we move below 1, end this child
        print "Below 1"
        return False,0
    if parentRunTot%3==0:
        #If we can divide by 3, we do
        print "Dividing by 3"
        parentRunTot/=3
        return dfsChildren(parentRunTot,parentSum)
    #If we aren't at the base case, but no problems, keep checking children
    else:
        print "Normal children"
        return dfsChildren(parentRunTot,parentSum)

initNum=int(raw_input())
print dfs(initNum,0)
