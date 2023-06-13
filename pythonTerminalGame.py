#imports letters as a form of iteration
from string import ascii_uppercase as row_letters

#Encapsulates the board for Connect4 using width and length
class Board:
    board_as_list = []
    def __init__(self):
        self.length = 6
        self.width = 6
        Board.board_as_list= [[0, [(number+1) for number in range(self.width)]]]
        for letter in row_letters:
            if row_letters.index(letter) in range(self.width):
                Board.board_as_list.append([letter, ["-"] * self.width])

    def __repr__(self):
        board_as_string = ""
        for row in Board.board_as_list:
            for item in row:
                if Board.board_as_list.index(row) == 0 and row.index(item) == 1:
                    for list_item in item:
                        board_as_string += "  " + str(list_item) + "  "
                else:
                    board_as_string += str(item)
            board_as_string += "\n"
        return board_as_string
    
    #returns an updated Board after a Player has added a piece
    def add_piece(self, player, player_input):
        player_placement = [item for item in player_input]
        for row in self.board_as_list:
            if player_placement[0] == row[0]:
                list_index = self.board_as_list.index(row)
                sublist_index = int(player_placement[1])
        return player.make_move(self, list_index, sublist_index)
    
    #returns True if a Player has connected 4 pieces horizontally
    def connect4_horizontally(self, player):
        player_piece = 0
        for row in self.board_as_list:
            for item in row[1]:
                if player_piece == 4:
                    return True
                elif item == player.color[0]:
                    player_piece += 1
                else:
                    player_piece = 0
        return False
    
    def connect4_vertically(self, player):
        player_piece = 0
        for row in self.board_as_list:
            for item in row[1]:
                if player_piece == 4:
                    return True
                elif item == player.color[0]:
                    player_piece += 1
                    sublist_index = row[1].index(item)
                    for number in range(1,4):
                        if self.board_as_list[self.board_as_list.index(row) + number][1][sublist_index] == player.color[0]:
                            player_piece += 1
                        else:
                            return False


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
       board_name.board_as_list[list_index][1][sublist_index-1] = self.color[0]
       return board_name
    
    #returns the total pieces on the board of the Player
    def total_pieces(self, board_name):
        count = 0
        for row in board_name.board_as_list:
            for item in row[1]:
                if self.color[0] == item:
                    count +=1
        return count
    
testBoard = Board()
testPlayer = Player("A", "Red")
testBoard.add_piece(testPlayer, "E2")
testBoard.add_piece(testPlayer, "B2")
testBoard.add_piece(testPlayer, "C2")
print(testBoard.add_piece(testPlayer, "D1"))
print(testBoard.connect4_vertically(testPlayer))


# #asks for player1 name data with user input
# player1_name = input("Welcome to Connect Four! Hello Player 1, can I have your name please: ")

# #creates player1 with name
# player1 = Player(player1_name)

# #asks for player2 data with user input
# player2_name = input("Welcome Player 2, could I also have your name please: ")

# #creates player2
# player2 = Player(player2_name)

# #determines the color choice for player1
# color_choice_player1 = input("Welcome " + player1.name + " and " + player2.name + 
#                      ". In connect four the objective is to connect four dots before the other player." +
#                      " You can connect your pieces either horiontally, vertially, or diagonally." +
#                      " Now that you know the basics, it's time to start! Player 1 would you like 'Red' or 'Blue': ")

# #checks if user input is invalid for color choice of player1
# while color_choice_player1 != "Red" and color_choice_player1 != "Blue":
#     color_choice_player1 = input("Sorry I didn't get that, could you please choose either 'Red' or 'Blue': ")

# #assigns the color chosesn to player1 object
# player1.color = color_choice_player1

# #assigns other color to player2
# if color_choice_player1 == "Red":
#     color_choice_player2 = "Blue"
# else:
#     color_choice_player2 = "Red"

# #assigns the color to player2 object
# player2.color = color_choice_player2

# #instatiates the connect4 board
# connect4_board = Board()

# #starts the game
# player1_move = input("Alright, that means you're " + player2.color + " " + player2.name + 
#                    ". Now that we have everything set it's time to begin the game. This is the board you will be playing on.\n\n" +
#                    str(connect4_board) + "\nAlright " + player1.name 
#                    + ", pick where you would like place your piece with the letter first and then the number: ")

# print(connect4_board.add_piece(player1, player1_move))

# #asks for player2's move
# player2_move = input("Great, now it's your turn " + player2.name + ". Pick where your would like to place your piece: ")

# #turns player1's input into a list
# print(connect4_board.add_piece(player2, player2_move))

# while player1.total_pieces(connect4_board) < 4 and player2.total_pieces(connect4_board) < 4:
#     player1_move = input("Your turn " + player1.name + ": ")
#     print(connect4_board.add_piece(player1, player1_move))
#     player2_move = input("Youe turn " + player2.name + ": ")
#     print(connect4_board.add_piece(player2, player2_move))