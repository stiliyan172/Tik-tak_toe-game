player_one_name = input("Player one name:\n").title()
player_two_name = input("Player two name:\n").title()
player_one_symbol = ""
player_two_symbol = ""
player_one = []
player_two = []
symbols = ["X", "O"]
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
board_coords = {
    1: [0, 0],
    2: [0, 1],
    3: [0, 2],
    4: [1, 0],
    5: [1, 1],
    6: [1, 2],
    7: [2, 0],
    8: [2, 1],
    9: [2, 2]
}
while True:
    """What symbol player choose 'X' or 'O'."""
    player_one_symbol = input(f"{player_one_name} would you like to play with 'X' or 'O'?\n").upper()
    if player_one_symbol in symbols:
        if player_one_symbol == "O":
            player_two_symbol = "X"
        else:
            player_two_symbol = "O"
        player_one = [player_one_name, player_one_symbol]
        player_two = [player_two_name, player_two_symbol]
        break
    else:
        print("You can play only with 'X' or 'O'!")
        continue
print("This is the numeration of board:")
print("|   1   |   2   |   3   |")
print("|   4   |   5   |   6   |")
print("|   7   |   8   |   9   |")
print(f"{player_one_name} start first!")


def board_print(game_board):
    """Simple board visualisation."""
    for row in game_board:
        print("|   ", end="")
        print("   |   ".join([str(x) for x in row]), end="")
        print("   |")


def game(game_board, coords, player):
    """Check if the player input number between 1-9 and make board changes!"""
    field = ""
    while True:
        field = input(f"Player {player[0]} choose a board position: 1-9\n")
        if field == "":
            print("Please choose only numbers between 1-9")
            continue
        if not field.isdigit():
            print("Please choose only numbers between 1-9")
            continue
        field = int(field)
        if 0 > field or field > 9:
            print("Please choose only numbers between 1-9")
            continue
        elif field not in coords:
            print("This position is taken, please choose different!!!")
            continue
        else:
            row, col = coords[field]
            del coords[field]
            game_board[row][col] = player[1]
            board_print(game_board)
            break

    return game_board


player_in_turn = player_one
waiting = player_two

winner = ""


def check_for_win(game_board, player):
    """simple player win check"""
    first_row, second_row, third_row, first_col, second_col, third_col, first_diag, second_diag = False, False, False, False, False, False, False, False
    if player[1] == game_board[0][0] == game_board[0][1] == game_board[0][2]:
        first_row = True
    if player[1] == game_board[1][0] == game_board[1][1] == game_board[1][2]:
        second_row = True
    if player[1] == game_board[2][0] == game_board[2][1] == game_board[2][2]:
        third_row = True
    if player[1] == game_board[0][0] == game_board[1][0] == game_board[2][0]:
        first_col = True
    if player[1] == game_board[0][1] == game_board[1][1] == game_board[2][1]:
        second_col = True
    if player[1] == game_board[0][2] == game_board[1][2] == game_board[2][2]:
        third_col = True
    if player[1] == game_board[0][0] == game_board[1][1] == game_board[2][2]:
        first_diag = True
    if player[1] == game_board[0][2] == game_board[1][1] == game_board[2][0]:
        second_diag = True
    if any([first_row, second_row, third_row, first_col, second_col, third_col, first_diag, second_diag]):
        return True
    return False

    # Some how this wont to work
    #
    # first_row = all([x == player[1] for x in game_board[0]])
    # second_row = all([x == player[1] for x in game_board[1]])
    # third_row = all([x == player[1] for x in game_board[2]])
    # first_col = all([x == player[1] for x in [game_board[0][0], game_board[1][0], game_board][2][0]])
    # second_col = all(x == player[1] for x in [game_board[0][1], game_board[1][1], game_board][2][1])
    # third_col = all(x == player[1] for x in [game_board[0][2], game_board[1][2], game_board][2][2])
    # first_diag = all(x == player[1] for x in [game_board[0][0], game_board[1][1], game_board][2][2])
    # second_diag = all(x == player[1] for x in [game_board[0][2], game_board[1][1], game_board][2][0])


while True:
    if winner:
        break
    board = game(board, board_coords, player_in_turn)
    winner = check_for_win(board, player_in_turn)
    if winner:
        print(f"{player_in_turn[0]} won!")
        break
    else:
        player_in_turn, waiting = waiting, player_in_turn