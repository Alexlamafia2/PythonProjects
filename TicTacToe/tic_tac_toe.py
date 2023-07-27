"""
   TIC TAC TOE LOGIC
   1- Two Players should be able to play the game (both sitting at the same computer)
   2- The board should be printed out everytime a player makes a move
   3- You should be able to accept input of the player position and then place a symbol on the board 
   4- We will use the "numpad" to match numbers to the grid on a tic tac toe board
"""


def choose_mark():
    player_one_choice = "WRONG"
    player_two_choice = "OPPOSITE"

    while player_one_choice != "X" or player_one_choice != "O":
        player_one_choice = input("Player 1: Do you want to be X or O?: ").upper()
        if player_one_choice == "X" or player_one_choice == "O":
            print("Player 1 will go first.")
            if player_one_choice == "X":
                player_two_choice = "O"
            elif player_one_choice == "O":
                player_two_choice = "X"
            player_choices = [player_one_choice, player_two_choice]
            return player_choices
        else:
            print("You need to choose X or O")


def run_game():
    print("Welcome to Tic Tac Toe!")

    players_mark = choose_mark()
    print(players_mark)
    player_one = players_mark[0]
    player_one_turn = True
    player_two = players_mark[1]
    player_two_turn = False

    top_row = [" ", " ", " "]
    middle_row = [" ", " ", " "]
    bottom_row = [" ", " ", " "]

    top_row_range = range(7, 9)
    middle_row_range = range(4, 6)
    bottom_row_range = range(1, 3)

    player_ready = "WRONG"
    while player_ready != "YES" or player_ready != "NO":
        player_ready = input("Are you ready to play? Enter Yes or No: ").upper()
        if player_ready == "YES":
            player_input = "WRONG"
            acceptable_range = range(1, 9)
            in_range = False
            game_over = False
            while (
                player_input.isdigit() == False
                or in_range == False
                or game_over == False
            ):
                print(top_row)
                print(middle_row)
                print(bottom_row)
                if player_one_turn == True:
                    print("Player 1 Turn")
                elif player_one_turn == False:
                    print("Player 2 Turn")
                player_input = input("Choose your next position: (1-9): ")
                if player_input.isdigit() == False:
                    print("I am sorry, that is not a digit.")
                if player_input.isdigit():
                    if int(player_input) in acceptable_range:
                        in_range = True

                        if int(player_input) in top_row_range and player_one_turn:
                            if int(player_input) == 7:
                                top_row[0] = player_one
                                player_one_turn = False
                                player_two_turn = True
                            elif int(player_input) == 8:
                                top_row[1] = player_one
                                player_one_turn = False
                                player_two_turn = True
                            elif int(player_input) == 9:
                                top_row[2] = player_one
                                player_one_turn = False
                                player_two_turn = True
                        elif int(player_input) in middle_row_range and player_one_turn:
                            if int(player_input) == 4:
                                middle_row[0] = player_one
                                player_one_turn = False
                                player_two_turn = True
                            elif int(player_input) == 5:
                                middle_row[1] = player_one
                                player_one_turn = False
                                player_two_turn = True
                            elif int(player_input) == 6:
                                middle_row[2] = player_one
                                player_one_turn = False
                                player_two_turn = True
                        elif int(player_input) in bottom_row_range and player_one_turn:
                            if int(player_input) == 1:
                                bottom_row[0] = player_one
                                player_one_turn = False
                                player_two_turn = True
                            elif int(player_input) == 2:
                                bottom_row[1] = player_one
                                player_one_turn = False
                                player_two_turn = True
                            elif int(player_input) == 3:
                                bottom_row[2] = player_one
                                player_one_turn = False
                                player_two_turn = True

                        if int(player_input) in top_row_range and player_two_turn:
                            if int(player_input) == 7:
                                top_row[0] = player_two
                                player_one_turn = True
                                player_two_turn = False
                            elif int(player_input) == 8:
                                top_row[1] = player_two
                                player_one_turn = True
                                player_two_turn = False
                            elif int(player_input) == 9:
                                top_row[2] = player_two
                                player_one_turn = True
                                player_two_turn = False
                        elif int(player_input) in middle_row_range and player_two_turn:
                            if int(player_input) == 4:
                                middle_row[0] = player_two
                                player_one_turn = True
                                player_two_turn = False
                            elif int(player_input) == 5:
                                middle_row[1] = player_two
                                player_one_turn = True
                                player_two_turn = False
                            elif int(player_input) == 6:
                                middle_row[2] = player_two
                                player_one_turn = True
                                player_two_turn = False
                        elif int(player_input) in bottom_row_range and player_two_turn:
                            if int(player_input) == 1:
                                bottom_row[0] = player_two
                                player_one_turn = True
                                player_two_turn = False
                            elif int(player_input) == 2:
                                bottom_row[1] = player_two
                                player_one_turn = True
                                player_two_turn = False
                            elif int(player_input) == 3:
                                bottom_row[2] = player_two
                                player_one_turn = True
                                player_two_turn = False

                    else:
                        in_range = False
                        print("I am sorry, you are not in range")

                if (
                    top_row[0] == middle_row[0]
                    and top_row[0] == bottom_row[0]
                    and top_row[0] != " "
                    and middle_row[0] != " "
                    and bottom_row[0] != " "
                ):
                    game_over = True
                elif (
                    top_row[0] == middle_row[1]
                    and top_row[0] == bottom_row[2]
                    and top_row[0] != " "
                    and middle_row[1] != " "
                    and bottom_row[2] != " "
                ):
                    game_over = True
                elif (
                    top_row[0] == top_row[1]
                    and top_row[0] == top_row[2]
                    and top_row[0] != " "
                    and top_row[1] != " "
                    and top_row[2] != " "
                ):
                    game_over = True
                elif (
                    top_row[1] == middle_row[1]
                    and top_row[1] == bottom_row[1]
                    and top_row[1] != " "
                    and middle_row[1] != " "
                    and bottom_row[1] != " "
                ):
                    game_over = True
                elif (
                    middle_row[0] == middle_row[1]
                    and middle_row[0] == middle_row[2]
                    and middle_row[0] != " "
                    and middle_row[1] != " "
                    and middle_row[2] != " "
                ):
                    game_over = True
                elif (
                    bottom_row[2] == middle_row[2]
                    and bottom_row[2] == top_row[2]
                    and top_row[2] != " "
                    and middle_row[2] != " "
                    and bottom_row[2] != " "
                ):
                    game_over = True
                elif (
                    bottom_row[2] == bottom_row[1]
                    and bottom_row[2] == bottom_row[0]
                    and bottom_row[0] != " "
                    and bottom_row[1] != " "
                    and bottom_row[2] != " "
                ):
                    game_over = True
                elif (
                    bottom_row[0] == middle_row[1]
                    and bottom_row[0] == top_row[2]
                    and top_row[2] != " "
                    and middle_row[1] != " "
                    and bottom_row[0] != " "
                ):
                    game_over = True

                if game_over:
                    if player_one_turn == False:
                        print("Game Over player one won")
                    elif player_one_turn == True:
                        print("Game Over player two won")

                    play_again = input(
                        "Do you want to play again? (Yes or No): "
                    ).upper()
                    if play_again == "YES":
                        run_game()
                    elif play_again == "NO":
                        print("We hope to see you back soon!")
                        break

        elif player_ready == "NO":
            quit = input("Do you want to quit? (Yes or No): ").upper()
            if quit == "YES":
                print("We hope to see you back soon!")
                break
            elif play_again == "NO":
                pass
        else:
            print("Please choose yes or no")
            pass


run_game()
