class GameManager:
    def __init__(self):
        self.players = []
        self.playerTurn = 0
        self.gameOver = False
        self.currentRound = 0
    
    def run(self):
        print("Yo start the game")