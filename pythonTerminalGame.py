#imports letters as a form of iteration
from string import ascii_uppercase as row_letters

#Encapsulates the board for Connect4 using width and length
class Board:
    board_as_list = []

    def __init__(self):
        self.length = 6
        self.width = 6
        Board.board_as_list = [[0, [(number+1) for number in range(self.width)]]]
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
    
    #returns True if a Player has connected 4 pieces horizontally
    def connect4_horizontally(self, player):
        player_piece = 0
        for row in self.board_as_list:
            for item in row[1]:
                if player_piece >= 4:
                    return True
                elif item == player.color[0]:
                    player_piece += 1
                else:
                    player_piece = 0
        return False
    
    #returns True if a Player has connected 4 pieces vertically
    def connect4_vertically(self, player):
        player_piece = 0
        for row in self.board_as_list:
            row_index = self.board_as_list.index(row)
            for item in row[1]:
                if player_piece >= 4:
                    return True
                elif item == player.color[0]:
                    player_piece += 1
                    sublist_index = row[1].index(item)
                    for number in range(1,4):
                        if row_index + number <= 6:
                            if self.board_as_list[self.board_as_list.index(row) + number][1][sublist_index] == player.color[0]:
                                player_piece += 1
                            else:
                                player_piece = 0
        return False
    
    #returns True if a Player has connected 4 pieces diagonally
    def connect4_diagonally(self, player):
        player_piece = 0
        for row in self.board_as_list:
            row_index = self.board_as_list.index(row)
            for item in row[1]:
                item_index = row[1].index(item)
                if player_piece >= 4:
                        return True
                elif item == player.color[0]:
                    player_piece +=1
                    for num in range(1, 4):
                        if (row_index + num <= 6) and (item_index + num <= 5):
                            if self.board_as_list[row_index + num][1][item_index + num ] == player.color[0]:
                                player_piece += 1
                            elif self.board_as_list[row_index + num][1][item_index - num] == player.color[0]:
                                player_piece += 1
                            else:
                                return False
        return False
    
    #checks for all forms of wins in connect4
    def connect4_win(self, player):
        if self.connect4_horizontally(player) == True:
            return True
        elif self.connect4_vertically(player) == True:
            return True
        elif self.connect4_diagonally(player) == True:
            return True
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
    
    #returns an updated Board after a Player has added a piece
    def add_piece(self, board, player_input):
        player_placement = [item for item in player_input]
        #makes sure player's input is valid
        possible_placements = []
        for number in board.board_as_list[0][1]:
            for row in board.board_as_list:
                possible_placements.append([str(row[0]), str(number)])
        for coordinate in possible_placements:
            if '0' in coordinate:
                possible_placements.remove(coordinate)
        #converts player's input into coordinate on board
        if player_placement in possible_placements:
            for row in board.board_as_list:
                if player_placement[0] == row[0]:
                    list_index = board.board_as_list.index(row)
                    sublist_index = int(player_placement[1])  
                    #checks if the coordinate inputted is empty or already taken
                    if board.board_as_list[list_index][1][sublist_index - 1] == '-':
                        return self.make_move(board, list_index, sublist_index)
                    else:
                        return False
        else:
            return False
    
    #implements the add_piece method along with data validation
    def new_turn(self, board, player_coordinate):
        player_move = self.add_piece(board, player_coordinate)
        while player_move == False:
            new_coordinate = input("Sorry that was an invalid input, please try again: ")
            player_move = self.add_piece(board, new_coordinate)
        return player_move
    
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
                     ". In Connect 4 the objective is to connect 4 dots before the other player." +
                     " You can connect your pieces either horiontally, vertically, or diagonally." +
                     " Now that you know the basics, it's time to start! " + player1.name + 
                     " would you like 'Red' or 'Yellow': ")

#checks if user input is invalid for color choice of player1
while color_choice_player1 != "Red" and color_choice_player1 != "Yellow":
    color_choice_player1 = input("Sorry I didn't get that, could you please choose either 'Red' or 'Yellow': ")

#assigns the color chosesn to player1 object
player1.color = color_choice_player1

#assigns other color to player2
if color_choice_player1 == "Red":
    color_choice_player2 = "Yellow"
else:
    color_choice_player2 = "Red"

#assigns the color to player2 object
player2.color = color_choice_player2

#instatiates the connect4 board
connect4_board = Board()

#starts the game
player1_coordinate = input("Alright, that means you're " + player2.color + " " + player2.name + 
                   ". Looks like we have everything set, it's time to begin the game! This is the board you will be playing on.\n\n" +
                   str(connect4_board) + "\nAlright " + player1.name 
                   + ", pick where you would like place your piece with the letter first and then the number (A1): ")

#spacing
print("\n")

#turns player1's input into a coordinate and returns an updated board
print(player1.new_turn(connect4_board, player1_coordinate))

#asks for player2's move
player2_coordinate = input("Great, now it's your turn " + player2.name + ". Pick where your would like to place your piece: ")

#spacing
print("\n")

#turns player2's input into a coordinate and returns an updated board
print(player2.new_turn(connect4_board, player2_coordinate))

#both players keep adding pieces until a player connects 4 pieces
while (connect4_board.connect4_win(player1) == False) and (connect4_board.connect4_win(player2) == False):
    player1_coordinate = input("Your turn " + player1.name + ": ")
    print("\n")
    print(player1.new_turn(connect4_board, player1_coordinate))
    if connect4_board.connect4_win(player1) == True:
        continue
    player2_coordinate = input("Your turn " + player2.name + ": ")
    print("n")
    print(player2.new_turn(connect4_board, player2_coordinate))

#congratulates player who wins
if connect4_board.connect4_win(player1) == True:
    print("Congratulaions " + player1.name + ", you win!")
elif connect4_board.connect4_win(player2) == True:
    print("Congratulations " + player2.name + ", your win!")