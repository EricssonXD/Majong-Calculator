from src.playerManager import Player 

class GameManager:
    def __init__(self):
        self.players = [Player(f"Player{i}")for i in range(4)]
        self.playerTurn = 0
        self.gameOver = False
        self.currentRound = 0
    
    def printPlayers(self):
        for player in self.players:
            print(player.name)
            # player.printPieces()

    def run(self):
        print("Yo start the game")