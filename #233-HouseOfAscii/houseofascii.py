#The house that ASCII built Challenge
#Graeme Cliffe

def determineSep(currUnit, adjUnit,align):#call with "*" or " " and "top/left/right/bot"
    if adjUnit==currUnit:#if they are the same unit, no divider
        return " "
    else:#if they are not the same unit, we need a divider
        if align=="vert":
            return "-"
        if align=="horiz":
            return "|"

def printBox(curr,top,left,right,bot):
    formatString=''
    topSep,leftSep=determineSep(curr,top,"vert"),determineSep(curr,left,"horiz")
    botSep,rightSep=determineSep(curr,bot,"vert"),determineSep(curr,right,"horiz")
    for row in range(0,3):
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
        formatString+="\n"

    return formatString

def pullAdj(levels,x,y):#return list of nearby units
    #levels is first by descending levels, then left to right
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

def printHouse():
    pass

def getRowColumnLists(levels,numLevels):#break levels into columns and rows
    rowList,columnList=list(),list()
    numColumns=len(levels[-1])
    #get rows
    for row in range(0,numLevels):#iterate through levels
        currRow=list()
        for column in range(0,numColumns):
            try:
                currRow.append(levels[row][column])
            except IndexError:
                    currRow.append(" ")
        rowList.append(currRow)
        
    #get columns
    for column in range(0,numColumns):
        currCol=list()
        for row in rowList:
            try:
                currCol.append(row[column])
            except IndexError:
                currCol.append(" ")
        columnList.append(currCol)
    return rowList,columnList

def main():
    numLevels=int(raw_input())
    levels=[]
    for i in range(0,numLevels):
        levels.append(list(raw_input()))
    #rowList,columnList=getRowColumnLists(levels,numLevels)
    print pullAdj(levels,0,0)#levels,x,y
    #above,left,right,down=' ',' ',' ',' '
    #print printBox('*',above,left,right,down)

main()
