class PieceKeys:
    NORTH = "north"
    EAST = "east"
    SOUTH = "north"
    WEST = "north"



class Player:
    def __init__(self, name):
        self.name = name
        
        pieceList = [PieceKeys.NORTH, PieceKeys.EAST, "dragon", "flower", "season"]

        for character in ["character", "bamboo", "dot"]:
            pieceList.extend([f"{character}{str(i)}" for i in range(1,10)])
            
        self.pieces = {str(i): 0 for i in pieceList}


    def printPieces(self):
        print(self.pieces)




    



    

    # pieces["bamboo"] # 0






player1 = Player("joe")

player2 = Player("bob")
print(PieceKeys.NORTH)

player1.printPieces()
# player3 = Player("jim")
# player4 = Player("guy")

# print(player1.pieces)