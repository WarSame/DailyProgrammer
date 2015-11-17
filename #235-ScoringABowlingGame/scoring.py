#Scoring a Bowling Game Challenge
#Graeme Cliffe
import string

def getFrames():
    #Get a list of frames. Each frame is a list of its rolls.
    frames=str(raw_input()).split(" ")
    return [list(x) for x in frames]

def getFrameScore(frame):
    #Get the score for a single frame, ignoring strikes/spares
    frameScore,prevRoll=0,"0"
    for roll in frame:
        frameScore+=getRawScore(roll,prevRoll)
        prevRoll=roll
    return frameScore

def getRawScore(currRoll,prevRoll):
    #Get score of a specific roll
    if currRoll in string.digits:
        return int(currRoll)
    if currRoll=="X":
        return 10
    if currRoll=="/":
        if prevRoll=="-":
            return 10
        return 10-int(prevRoll)
    if currRoll=="-":
        return 0

def getNextIndexPair(frameIndex,rollIndex,frames):
    #Find the index pair of next roll
    lenFrame=len(frames[frameIndex])
    newRollIndex,newFrameIndex=rollIndex,frameIndex
    if rollIndex+1>=lenFrame:
        newRollIndex,newFrameIndex=0,frameIndex+1
    else:
        newRollIndex+=1
    return newFrameIndex,newRollIndex

def getBonusScore(specialChar,frameIn,rollIn,frames):
    #Get bonus score given bonus type
    bonusScore=0
    if specialChar=="/":
        currRoll=frames[frameIn][rollIn]
        frameIn,rollIn=getNextIndexPair(frameIn,rollIn,frames)
        bonusScore+=getRawScore(frames[frameIn][rollIn],currRoll)
    if specialChar=="X":
        for i in range(0,2):
            currRoll=frames[frameIn][rollIn]
            frameIn,rollIn=getNextIndexPair(frameIn,rollIn,frames)
            bonusScore+=getRawScore(frames[frameIn][rollIn],currRoll)
    return bonusScore

def getScore(frames):
    #Iterate over the frames and sum their scores
    score=0
    fillBalls=False
    for frameIn in range(0,len(frames)):
        currFrame=frames[frameIn]
        score+=getFrameScore(currFrame)
        for rollIn in range(0,len(currFrame)):
            if currFrame[rollIn]=="/" or currFrame[rollIn]=="X":
                if frameIn==9:#Don't count fill balls twice
                    break
                score+=getBonusScore(currFrame[rollIn],frameIn,rollIn,frames)
    return score

def main():
    print getScore(getFrames())

main()
