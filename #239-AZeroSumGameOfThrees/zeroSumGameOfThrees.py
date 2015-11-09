#A Zero-Sum Game Of Threes Challenge
#Graeme Cliffe

children=[-2,-1,1,2]
memoTable={}

def isInTable(nodeTot,nodeSum):
    #Memo table func - if it's in the table, return True
    #If it's not, return false and insert it
    if (nodeTot,nodeSum) in memoTable:
        return True
    else:
        memoTable[(nodeTot,nodeSum)]=True
        return False

def dfsChildren(parentRunTot,parentSum):#spin children off of parent node
    for childVal in children:#Attempt all of the children branches
        childSum=parentSum+childVal
        childRunTot=parentRunTot+childVal
        
        additionList=dfs(childRunTot,childSum)
        if additionList:#If this child returns True, then append and return up

            additionList.append(childVal)
            return additionList
    return None#No case matched

#Use a DFS. If we reach more than 3*initial number a solution is impossible
def dfs(parentRunTot,parentSum):
    #If we've already hit this total/sum pair, then
    #It must not work - return false
    if isInTable(parentRunTot,parentSum):
        return False
    if parentRunTot==1:
        if parentSum==0:
            #If we have hit the base case
            baseList=list()
            baseList.append(0)
            return baseList
        return None#End of branch
    if parentRunTot>3*initNum:
        #If we reach too high, end this child
        return None
    if parentRunTot<1:
        #If we move below 1, end this child
        return None
    if parentRunTot%3==0:
        #If we can divide by 3, we do
        parentRunTot/=3
        retList=dfs(parentRunTot,parentSum)
        if retList:#If we get returned a list of addition/subtraction
            retList.append("/3")
        return retList
    #If we aren't at the base case, but no problems, keep checking children
    else:
        return dfsChildren(parentRunTot,parentSum)

initNum=int(raw_input())
result=None
try:#Recursion error on impossible solution
    result=dfs(initNum,0)
    result=list(reversed(result))
except:
    result=None
if result:
    print "Starting with:",initNum
    print "Additions and subtractions in order:"
    for i in result:
        print i,
else:
    print "Impossible!"
