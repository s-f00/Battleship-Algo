from typing import Any, List
board: List[Any] = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


def check_left(row, col, checker_length):
    if col - checker_length < 0:
        return -1

    checked_tiles = []
    for i in range(checker_length + 1):
        checked_tiles.append(board[row][col - i])

    res = True
    for tile in checked_tiles:
        if not isinstance(tile, int):
            res = False

    if res:
        board[row][col] += 1

    return -1


def check_right(row, col, checker_length):
    if col + checker_length > len(board[row]) - 1:
        return -1

    checked_tiles = []
    for i in range(checker_length + 1):
        checked_tiles.append(board[row][col + i])

    res = True
    for tile in checked_tiles:
        if not isinstance(tile, int):
            res = False

    if res:
        board[row][col] += 1

    return -1


def check_up(row, col, checker_length):
    if row - checker_length < 0:
        return -1

    checked_tiles = []
    for i in range(checker_length + 1):
        checked_tiles.append(board[row - i][col])

    res = True
    for tile in checked_tiles:
        if not isinstance(tile, int):
            res = False

    if res:
        board[row][col] += 1

    return -1


def check_down(row, col, checker_length):
    if row + checker_length > len(board) - 1:
        return -1

    checked_tiles = []
    for i in range(checker_length + 1):
        checked_tiles.append(board[row + i][col])

    res = True
    for tile in checked_tiles:
        if not isinstance(tile, int):
            res = False

    if res:
        board[row][col] += 1

    return -1
