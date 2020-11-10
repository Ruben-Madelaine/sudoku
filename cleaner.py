import random
from main import Sudoku
import numpy as np
# from generator import randomize


LEVEL = 2
BOARD = [
        [1, 2, 3, 5, 4, 6, 8, 7, 9],
        [7, 8, 9, 2, 1, 3, 5, 4, 6],
        [4, 5, 6, 8, 7, 9, 2, 1, 3],
        [9, 1, 2, 4, 3, 5, 7, 6, 8],
        [6, 7, 8, 1, 9, 2, 4, 3, 5],
        [3, 4, 5, 7, 6, 8, 1, 9, 2],
        [2, 3, 4, 6, 5, 7, 9, 8, 1],
        [5, 6, 7, 9, 8, 1, 3, 2, 4],
        [8, 9, 1, 3, 2, 4, 6, 5, 7]
        ]


def dificulty(level):
    min_elem = [2, 4, 6]
    max_elem = [5, 8, 9]
    selection = [min_elem[level], max_elem[level]]
    return selection


def clean(level, board):
    for elem_to_replace in range(len(board)):
        limit = random_value(level)
        count = 0

        for row in range(len(board)):
            for column in range(len(board)):
                if board[row][column] == elem_to_replace+1:# and count < limit:
                    print(elem_to_replace+1)
                    condition = cleanable(board, row, column)
                    if condition:
                        count += 1
                        board[row][column] = 0
    return board


def random_value(level):
    selection = dificulty(level)
    level = random.randrange(selection[0], selection[1])
    return level


def cleanable(board, column, row):
    sqrt = int(len(board)**(1/2))
    angle1 = column//sqrt*sqrt
    angle2 = column//sqrt*sqrt+sqrt
    angle3 = row//sqrt*sqrt
    angle4 = row//sqrt*sqrt+sqrt
    matrix = np.array(board)[angle1 : angle2, angle3 : angle4].tolist()
    set_matrix = set(sum(matrix, []))
    condition = len(set_matrix)



    print("row:", row, "column:", column, "val:", board[row][column])
    print("angle1", angle1, "angle2", angle2, "angle3", angle3, "angle4", angle4)
    print(matrix)
    print("\n")
    # import pdb; pdb.set_trace()
    return condition > 2


def show(board):
    sudoku = Sudoku()
    sudoku.set_grid(board)
    sudoku.hilight(2)
    print(sudoku)


def main():
    # board = clean(LEVEL, randomize(board, int(len(board)**(1/2))))
    board = clean(LEVEL,BOARD)
    show(board)


main()