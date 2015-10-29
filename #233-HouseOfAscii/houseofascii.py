#The house that ASCII built Challenge
#Graeme Cliffe

def determineSideSep(currUnit, adjUnit,align):#call with "*" or " " and "top/left/right/bot"
    if adjUnit==currUnit:#if they are the same unit, no divider
        return " "
    elif currUnit=="*":#if they are not the same unit, we need a divider
        if align=="vert":
            return "-"
        if align=="horiz":
            return "|"
    return " "

def formatBox(curr,adjlist):
    #returns a list with the three rows of the box of curr
    #this is based on the adjacent units - similar units don't have borders
    formatList=[]
    topleft,top,topright=adjlist[0],adjlist[1],adjlist[2]
    left,right=adjlist[3],adjlist[4]
    botleft,bot,botright=adjlist[5],adjlist[6],adjlist[7]
    topSep,leftSep=determineSideSep(curr,top,"vert"),determineSideSep(curr,left,"horiz")
    botSep,rightSep=determineSideSep(curr,bot,"vert"),determineSideSep(curr,right,"horiz")

    for row in range(0,3):
        formatString=''
        for element in range(0,5):
            if row==0:
                formatString+=topSep
            if row==2:
                formatString+=botSep
            if row==1:
                if element==0:
                    formatString+=leftSep
                elif element==4:
                    formatString+=rightSep
                else:
                    formatString+=" "
        formatList.append(formatString)
    return formatList

def pullAdj(levels,x,y):#return list of nearby units
    #returns from left to right then top to bot
    #top left...top right...bot left...bot right
    adj=list()
    for xVal in range(-1,2):
        for yVal in range(-1,2):
            if xVal==0 and yVal==0:
                continue
            if x+xVal<0 or y+yVal<0:
                adj.append(" ")
            else:
                try:
                    adj.append(levels[x+xVal][y+yVal])
                except IndexError:
                    adj.append(" ")
    return adj

def getInput():
    #Take input from user - number of levels, then level layout
    numLevels=int(raw_input())
    levels=[]
    for i in range(0,numLevels):
        levels.append(list(raw_input()))
    return numLevels,levels

def printRow(n,levels,printTop,printBot):
    #Print a row given the row number and the layout array
    rowStrings=['','','']
    for i in range(len(levels[n])):
        #list of sub-row strings
        boxLists=formatBox(levels[n][i],pullAdj(levels,n,i))
        rowStrings[0]+=boxLists[0]
        rowStrings[1]+=boxLists[1]
        rowStrings[2]+=boxLists[2]
    if printTop:
        print rowStrings[0]
    print rowStrings[1]
    if printBot:
        print rowStrings[2]
        
def printHouse(levels,numLevels):
    for i in range(0,numLevels):
        printTop=False
        printBot=False
        if i-1<0:#if the above level doesn't exist
            printTop=True
        elif levels[i]!=levels[i-1]:
            #if current level and previous have different layouts
            #then don't print the seperators
            printTop=True
        if i+1>numLevels-1:
            printBot=True
        elif levels[i]!=levels[i+1]:
            #if current level and next have different layouts
            #don't print seperators
            printBot=True
        printRow(i,levels,printTop,printBot)

def main():
    numLevels,levels=getInput()
    printHouse(levels,numLevels)

main()
