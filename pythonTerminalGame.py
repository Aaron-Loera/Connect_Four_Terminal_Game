player1 = input("Welcome to Connect Four! Hello Player 1, can I have your name please: ")
player2 = input("Welcome Player 2, could I also have your name please: ")

color_choice_player1 = input("Welcome " + player1 + " and " + player2 + 
                     ". In connect four the objective is to connect four dots before the other player." +
                     " You can connect your pieces either horiontally, vertially, or diagonally." +
                     " Now that you know the basics, it's time to start! Player 1 would you like 'Red' or 'Blue': ")

while color_choice_player1 != "Red" and color_choice_player1 != "Blue":
    color_choice_player1 = input("Sorry I didn't get that, could you please choose either 'Red' or 'Blue': ")

if color_choice_player1 == "Red":
    color_choice_player2 = "Blue"
else:
    color_choice_player2 = "Red"
