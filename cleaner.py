import random
import numpy as np
import generator as gen


def clean(board, level=3):
    sqrt = int(len(board) ** (1 / 2))
    for i in range(len(board)):
        for j in range(len(board)):
            limit = len(board) + 1 - random_value(level)
            board = gen.randomize(board, sqrt)
            if count(board, board[i][j]) > limit:
                board[i][j] = 0
    return board


def dificulty(level):
    min_elem = [0, 2, 4, 6, 8]
    max_elem = [m + 2 for m in min_elem]
    selection = [min_elem[level], max_elem[level]]
    return selection


def random_value(level):
    selection = dificulty(level)
    level = random.randrange(selection[0], selection[1])
    return level


def count(board, num):
    count = 0
    for row in board:
        for elem in row:
            if num == elem:
                count += 1
    return count


def show(board):
    from sudoku import Sudoku

    sudoku = Sudoku(board)
    print(sudoku)


def main():
    level = 3
    board = gen.generate(level)
    board = clean(
        gen.randomize(board, int(len(board) ** (1 / 2))),
    )
    show(board)


if __name__ == "__main__":
    main()
