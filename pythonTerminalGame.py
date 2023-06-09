#imports letters as a form of iteration
from string import ascii_uppercase as letter

#Encapsulates the board for Connect4 using width and length
class Board:
    board_as_list = []

    def __init__(self):
        self.length = 6
        self.width = 6
        Board.board_as_list = [(["-"] * self.width) for number in range(self.length)]
    
    def __repr__(self):
        board_as_string = ""
        for row in Board.board_as_list:
            for item in row:
                board_as_string += item
            board_as_string += "\n"
        return board_as_string

#Encapsulates the data for a player in Connect4
class Player:
    player_count = 0

    def __init__(self, name, color=""):
        self.name = name
        self.color = color
        Player.player_count += 1
        self.player = Player.player_count
    
    def __repr__(self):
        return "Hello " + self.name + ", your are player " + str(self.player) + " and your color is " + self.color  + "."
    
    #returns the new Board after a Player has made a move
    def make_move(self, board_name, list_index, sublist_index):
       board_name.board_as_list[list_index][sublist_index] = self.color[0]
       return board_name
    

#asks for player1 name data with user input
player1_name = input("Welcome to Connect Four! Hello Player 1, can I have your name please: ")

#creates player1 with name
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

#instatiates the connect4 board
connect4_board = Board()

#starts the game
player1_move = input("Alright, that means you're " + player2.color + " " + player2.name + 
                   ". Now that we have everything set it's time to begin the game. This is the board you will be playing on.\n\n" +
                   str(connect4_board) + "\nAlright " + player1.name 
                   + ", pick which row you would like to place your piece: ")

#player1 makes the first move
print(player1_move)
