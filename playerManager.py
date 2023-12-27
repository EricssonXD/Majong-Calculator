# We import this to use the enum class
from enum import Enum

class Player:
    def __init__(self, name):
        self.name = name
        self.pieces = {e: 0 for e in PieceKey}


    def printPieces(self):
        print(self.pieces)
        # print(PieceKeys().__dir__())


# List of keys for the pieces
class PieceKey(Enum):
    Character1 = "character1"
    Character2 = "character2"
    Character3 = "character3"
    Character4 = "character4"
    Character5 = "character5"
    Character6 = "character6"
    Character7 = "character7"
    Character8 = "character8"
    Character9 = "character9"
    Bamboo1 = "bamboo1"
    Bamboo2 = "bamboo2"
    Bamboo3 = "bamboo3"
    Bamboo4 = "bamboo4"
    Bamboo5 = "bamboo5"
    Bamboo6 = "bamboo6"
    Bamboo7 = "bamboo7"
    Bamboo8 = "bamboo8"
    Bamboo9 = "bamboo9"
    Dot1 = "dot1"
    Dot2 = "dot2"
    Dot3 = "dot3"
    Dot4 = "dot4"
    Dot5 = "dot5"
    Dot6 = "dot6"
    Dot7 = "dot7"
    Dot8 = "dot8"
    Dot9 = "dot9"
    North = "north"
    East = "east"
    South = "south"
    West = "west"
    Flower = "flower"
    Season = "season"