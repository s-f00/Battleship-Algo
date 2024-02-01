import checker
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]


def update_board():
    ship_checker(2)
    ship_checker(3)
    ship_checker(3)
    ship_checker(4)
    ship_checker(5)
    print_board()
    checker.board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    return -1


def print_board():
    boardString = ""
    for row in range(len(checker.board)):
        rowString = ""
        for col in range(len(checker.board[row])):
            rowString += ("[" + str(checker.board[row][col]) + "]")
        boardString += rowString + "\n"

    print(boardString)


def hit_board(row, col):
    checker.board[letters.index(row)][col - 1] = "--"
    return -1


def ship_checker(ship_length):
    for row in range(len(checker.board)):
        for col in range(len(checker.board[row])):
            checker_length = ship_length - 1
            checker.check_left(row, col, checker_length)
            checker.check_right(row, col, checker_length)
            checker.check_up(row, col, checker_length)
            checker.check_down(row, col, checker_length)
