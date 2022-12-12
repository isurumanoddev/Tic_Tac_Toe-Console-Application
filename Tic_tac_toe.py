board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-", ]


def display_board():
    print("|", board[0], "|", board[1], "|", board[2], "|")
    print("|", board[3], "|", board[4], "|", board[5], "|")
    print("|", board[6], "|", board[7], "|", board[8], "|")


game_still_going = True
current_player = "X"
winner = None


def play_game():
    display_board()
    while game_still_going:
        handle_turn(current_player)
        check_game_over()
        flip_player()

    if winner == "X" or winner == "O":
        print(winner + " Game Won ! ")
    elif winner == None:
        print("Game Tie !")


def check_if_win():
    pass


def check_if_tie():
    pass


def check_game_over():
    check_for_winner()
    check_if_tie()


def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"


def check_for_winner():
    global winner
    rows = check_rows()
    columns = check_columns()
    diagonals = check_diagonals()

    if rows:
        winner = rows
    elif columns:
        winner = columns
    elif diagonals:
        winner = diagonals
    else:
        winner = None


def check_rows():
    global game_still_going
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    if row1 or row2 or row3:
        game_still_going = False
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]


def check_columns():
    global game_still_going
    column1 = board[0] == board[3] == board[6] != "-"
    column2 = board[1] == board[4] == board[7] != "-"
    column3 = board[2] == board[5] == board[8] != "-"
    if column1 or column2 or column3:
        game_still_going = False
    if column1:
        return board[0]
    elif column2:
        return board[3]
    elif column3:
        return board[6]


def check_diagonals():
    global game_still_going
    diagonal1 = board[0] == board[4] == board[8] != "-"
    diagonal2 = board[6] == board[4] == board[2] != "-"
    if diagonal1 or diagonal2:
        game_still_going = False
    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[6]


def handle_turn(player):
    position = int(input("Enter number between 1-9 : ")) - 1
    board[position] = player
    display_board()




play_game()
