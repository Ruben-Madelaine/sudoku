import random
from main import Sudoku
import numpy as np
# from generator import randomize


LEVEL = 2
BOARD = [
        [4, 5, 6, 8, 9, 7, 1, 3, 2],
        [1, 2, 3, 5, 6, 4, 7, 9, 8],
        [7, 8, 9, 2, 3, 1, 4, 6, 5],
        [6, 7, 8, 1, 2, 9, 3, 5, 4],
        [9, 1, 2, 4, 5, 3, 6, 8, 7],
        [3, 4, 5, 7, 8, 6, 9, 2, 1],
        [5, 6, 7, 9, 1, 8, 2, 4, 3],
        [2, 3, 4, 6, 7, 5, 8, 1, 9],
        [8, 9, 1, 3, 4, 2, 5, 7, 6],
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
            for elem_selected in range(len(board)):
                if board[row][elem_selected] == elem_to_replace+1 and count < limit:
                    count += 1
                    board[row][elem_selected] = 0
    return board


def cleanable(board, row, elem_selected):
    board = np.array(board)
    local_square_angle = 
    local_square = 





    if board[i:,] == board[:i,] == selection ==
    print(board)

def random_value(level):
    selection = dificulty(level)
    level = random.randrange(selection[0], selection[1])
    return level


def show(board):
    sudoku = Sudoku()
    sudoku.set_grid(board)
    sudoku.hilight(2)
    print(sudoku)


def main():
    board = clean(LEVEL,BOARD)
    print(*board, sep='\n')
    # board = randomize(board, int(len(board)**(1/2)))
    show(board)

# main()

cleanable(BOARD)