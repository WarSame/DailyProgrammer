#A Zero-Sum Game Of Threes Challenge
#Graeme Cliffe

class node:
    children=list()
    additions=list()
    currTotal=0#Value remaining from original number
    currSum=0#Sum of additions so far
    visited=False
    def __init__(self):
        self.children=[2,1,-1,-2]
    def setValues(self,additions,currSum):
        self.children=[2,1,-1,-2]
        self.additions=additions
        self.currSum=currSum
    def setTotal(self,currTotal):
        self.currTotal=currTotal
    def getTotal(self):
        return self.currTotal
    def getChild(self):
        if len(self.children)==0:
            return None
        return self.children.pop()

#Use a DFS. If we reach more than 3*initial number a solution is impossible
def dfs(currNode):
    if currNode.currTotal==1:
        return True
    if currNode.currTotal>3*initNum:
        return False
    if currNode.currTotal<1:
        return False
    childRets=list()
    for child in currNode.children:#Attempt all of the children branches
        childVal=currNode.getChild()
        childNode=node()
        
        childAdditions=currNode.additions
        childAdditions.append(childVal)
        childSum=currNode.currSum+childVal
        childNode.setTotal(currNode.getTotal()+childVal)
        childNode.setValues(childAdditions,childSum)
        
        retVal=dfs(childNode)
        childRets.append(retVal)
    return any(childRets)

initNum=int(raw_input())
currNode=node()
currNode.setTotal(initNum)
print dfs(currNode)
