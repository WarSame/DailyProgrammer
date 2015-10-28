#The house that ASCII built Challenge
#Graeme Cliffe


def printHouse(levels):
    prevElement=" "
    rowStrings=[]
    for level in reversed(levels):#level of house
        prevElement=" "
        topRow,midRow,botRow='','',''
        for element in level:#asterisks or spaces in level
            if element=="*":
                if prevElement==" ":
                    topRow+="|    "
                    midRow+="|    "
                    botRow+="|    "
                if prevElement=="*":
                    topRow+="_____"
                    midRow+=" "
                    botRow+="_____"
            if element==" ":
                if prevElement==" ":
                    topRow+="     "
                    midRow+="     "
                    botRow+="     "
                if prevElement=="*":
                    topRow+="|    "
                    midRow+="|    "
                    botRow+="|    "
            prevElement=element
            
        print topRow
        print midRow
        print botRow

def main():
    numLevels=int(raw_input())
    levels=[]
    for i in range(0,numLevels):
        levels.append(raw_input())
    printHouse(levels)

main()
