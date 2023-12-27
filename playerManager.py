class Player:
    def __init__(self, name):
        self.name = name
        print("Player created: " + self.name)
    
    piece = {
        "character": ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
        "bamboo": ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
        "dot": ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
        "wind": ["east", "south", "west", "north"],
        "dragon": ["red", "green", "white"],
        "flower": ["plum", "orchid", "chrysanthemum", "bamboo"],
        "season": ["spring", "summer", "autumn", "winter"]
    }






player1 = Player("joe")
player2 = Player("bob")
player3 = Player("jim")
player4 = Player("guy")

print(player4.capitalize_name())
player3.piece