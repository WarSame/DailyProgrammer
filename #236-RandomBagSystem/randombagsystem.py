#Random Bag System Challenge
#Graeme Cliffe

import random

pieceList="OISZLJT"
class tetroBag():
    def __init__(self):
        self.pieces=list(pieceList)
    def fillBag(self):
        self.pieces=list(pieceList)
    def pullPiece(self):
        piece=random.choice(self.pieces)
        self.pieces.remove(piece)
        if (len(self.pieces)==0):
            self.fillBag()
        return piece

def verify(lVer):
    #count number of times piece occurs in 7 piece chunks
    #it must occur exactly once
    index,currChunk=0,[]
    for currPiece in lVer:
        if index%7==0:
            currChunk=lVer[index:index+7]
        if len(currChunk)!=len(set(currChunk)) or not (c in pieceList for c in currChunk):
            return "NOT VALID"
        index+=1
    return "VALID"

def main():
    x,y = tetroBag(),[]
    for i in range(0,50):
        y.append(x.pullPiece())
    print ''.join(y), "is", verify(y)

main()
