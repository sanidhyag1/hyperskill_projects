new_col = 0
new_row = 0
blank = " "
board = blank * 9
x_move = True
game_done = False


def draw_board(board):
    print("-" * len(board))
    print("|", " ".join(board[:3]), "|")
    print("|", " ".join(board[3:6]), "|")
    print("|", " ".join(board[6:]), "|")
    print("-" * len(board))


def check_win(board):
    straights = [board[:3], board[3:6], board[6:],
                 board[0:9:3], board[1:9:3], board[2:9:3],
                 board[0:9:4], board[2:7:2]]
    x_wins = True if "XXX" in straights else False
    o_wins = True if "OOO" in straights else False
    if abs(board.count("X") - board.count("O")) > 1 or (x_wins and o_wins):
        print("Impossible")
        return True
    elif x_wins:
        print("X wins")
        return True
    elif o_wins:
        print("O wins")
        return True
    elif board.count(blank) == 0:
        print("Draw")
        return True
    else:
        print("Game not finished")
        return False


def get_coordinates(board):
    global new_col
    global new_row
    coordinates = input("Enter the coordinates: ").strip().split()
    if len(coordinates) != 2 or not (coordinates[0].isdigit() and coordinates[1].isdigit()):
        print("You should enter numbers!")
        return False
    new_col = int(coordinates[0]) - 1
    new_row = 3 - int(coordinates[1])
    if not (0 <= new_row <= 2 and 0 <= new_col <= 2):
        print("Coordinates should be from 1 to 3!")
        return False
    if board[new_row * 3 + new_col] != blank:
        print("This cell is occupied! Choose another one!")
        return False
    return True


# data = input("Enter cells: ")

draw_board(board)

while not game_done:

    valid_data = False
    while not valid_data:
        valid_data = get_coordinates(board)

    board = "".join([("X" if x_move else "O") if i == (new_row * 3 + new_col) else n for i, n in enumerate(board)])
    x_move = not x_move

    draw_board(board)
    game_done = check_win(board)
