print(f" Welcome to the Tic Tac Toe game")

player = 'X'
winner = None
score = 0

board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]


def display_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("_" * 9)
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("_" * 9)
    print(board[6] + " | " + board[7] + " | " + board[8])


def player_move(board):
    move = int(input(f"player {player}, Enter your move: "))
    if 1 <= move <= 9 and board[move - 1] == " ":
        board[move - 1] = player
    elif 1 <= move <= 9 and board != " ":
        print("The spot is already taken, try another one")
        switch_player()
    elif 0 >= move or move > 9:
        print("Invalid number")
        switch_player()


def switch_player():
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"


def horizontal_row(board):
    global winner
    if (board[0] == board[1] == board[2] and board[0] != " " or
            board[3] == board[4] == board[5] and board[3] != " " or
            board[6] == board[7] == board[8] and board[6] != " "):
        winner = player
        return True


def vertical_row(board):
    global winner
    if (board[0] == board[3] == board[6] and board[0] != " " or
            board[1] == board[4] == board[7] and board[1] != " " or
            board[2] == board[5] == board[8] and board[2] != " "):
        winner = player
        return True


def diagonal_row(board):
    global winner
    if (board[0] == board[4] == board[8] and board[0] != " " or
            board[2] == board[4] == board[6] and board[2] != " "):
        winner = player
        return True


def check_win(board):
    global winner
    if horizontal_row(board) or vertical_row(board) or diagonal_row(board):
        print(f"The winner is player {winner}")


# def check_tie(board):
#     if board[0-8] != " ":
#         print("The game is drawn")


def check_score(score):
    global winner
    if winner is not None:
        score += 1
        print(f"The player {player} have {score} score ")


def game_playing():
    while True:
        display_board(board)
        player_move(board)
        check_win(board)
        if winner:
            display_board(board)
            check_score(score)
            break

        switch_player()


def play_again():
    while True:
        game_playing()
        play_again_game = input("Do you want play again, y or n: ").lower()
        if play_again_game == 'n':
            print("Have nice day")
            break
        else:
            display_board(board)


play_again()
