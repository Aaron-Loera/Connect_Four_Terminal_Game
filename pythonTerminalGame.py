#class for the connect 4 board, determines the width and length
class Board:
    def __init__(self, length=6, width=6):
        self.length = length
        self.width = width
    def board_as_list(self):
        board = []
        for number in range(self.length):
            board.append(["-"] * self.width)
        return board
    def show_board(self):
        board = ""
        for row in self.board_as_list():
            for piece in row:
                board += "-"
            board += "\n"
        return board
    def add_piece(self, player, position):
        pass


firstBoard = Board(6, 6)
print(firstBoard.board_as_list())
print(firstBoard.show_board())

#creates player1 with user input
player1 = input("Welcome to Connect Four! Hello Player 1, can I have your name please: ")
#creates player2 with user input
player2 = input("Welcome Player 2, could I also have your name please: ")

#determines the color choice for player1
color_choice_player1 = input("Welcome " + player1 + " and " + player2 + 
                     ". In connect four the objective is to connect four dots before the other player." +
                     " You can connect your pieces either horiontally, vertially, or diagonally." +
                     " Now that you know the basics, it's time to start! Player 1 would you like 'Red' or 'Blue': ")

#checks if user input is invalid for color choice of player1
while color_choice_player1 != "Red" and color_choice_player1 != "Blue":
    color_choice_player1 = input("Sorry I didn't get that, could you please choose either 'Red' or 'Blue': ")

#assigns other color to player2
if color_choice_player1 == "Red":
    color_choice_player2 = "Blue"
else:
    color_choice_player2 = "Red"

    

