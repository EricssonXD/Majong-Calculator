# from src.playerManager import PieceKey
from playerManager import PieceKey
from gameManager import GameManager

def main():
    # Your main code goes here
    game = GameManager()
    # game.printPlayers()
    print(PieceKey.Character1.value)
    # game.run()
    print(game.players[0].pieces[PieceKey.Character1])

if __name__ == "__main__":
    main()