#class for the connect 4 board, determines the width and length
class Board:
    def __init__(self, length=6, width=6):
        self.length = length
        self.width = width
    
    #displays the board as a list
    def board_as_list(self):
        board = []
        for number in range(self.length):
            board.append(["-"] * self.width)
        return board
    
    #displays the board to the player
    def show_board(self):
        board = ""
        for row in self.board_as_list():
            for piece in row:
                board += "-"
            board += "\n"
        return board
    def add_piece(self, player, position):
        pass

#class for each player in connect 4
class Player:
    player_count = 0
    def __init__(self, name, color=""):
        self.name = name
        self.color = color
        Player.player_count += 1
        self.player = Player.player_count
    def __repr__(self):
        return "Hello " + self.name + ", your are player " + str(self.player) + " and your color is " + self.color  + "."

#asks for player1 data with user input
player1_name = input("Welcome to Connect Four! Hello Player 1, can I have your name please: ")

#creates player1
player1 = Player(player1_name)

#asks for player2 data with user input
player2_name = input("Welcome Player 2, could I also have your name please: ")

#creates player2
player2 = Player(player2_name)

#determines the color choice for player1
color_choice_player1 = input("Welcome " + player1.name + " and " + player2.name + 
                     ". In connect four the objective is to connect four dots before the other player." +
                     " You can connect your pieces either horiontally, vertially, or diagonally." +
                     " Now that you know the basics, it's time to start! Player 1 would you like 'Red' or 'Blue': ")

#checks if user input is invalid for color choice of player1
while color_choice_player1 != "Red" and color_choice_player1 != "Blue":
    color_choice_player1 = input("Sorry I didn't get that, could you please choose either 'Red' or 'Blue': ")

#assigns the color chosesn to player1 object
player1.color = color_choice_player1

#assigns other color to player2
if color_choice_player1 == "Red":
    color_choice_player2 = "Blue"
else:
    color_choice_player2 = "Red"

#assigns the color to player2 object
player2.color = color_choice_player2

start_game = input("Alright, that means you're " + player2.color + " " + player2.name + 
                   ". Hit 'Enter' whenever yall are ready to start: ")
