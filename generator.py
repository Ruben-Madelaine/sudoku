import numpy as np
from random import shuffle
from validator import valid_solution


MIX_LOOP = 4
sub = 3
size = sub ** 2


def generate_board(sub, size):
    def add_offset(list, offset):
        s = len(list)
        return list[s - offset :] + list[: s - offset]

    board = []
    vals = list(range(1, size + 1))

    for i in range(size):
        board += [vals]

        vals = add_offset(vals, sub)
        if i > 0 and (i + 1) % sub == 0:
            vals = add_offset(vals, 1)

    return board


def randomizer(board):
    for i in range(2):
        random_board = []
        for i in range(0, len(board), 3):
            a = board[i : i + 3]
            shuffle(a)
            random_board += a
    return random_board


def mix_loop(board, num):
    for i in range(num):
        board = randomizer(board)
        board = np.transpose(board).tolist()

    return board


def validation_test(board):
    test = valid_solution(board)
    return test


def main(num):
    filled_board = generate_board(sub, size)
    random_board = mix_loop(filled_board, num)

    print(*random_board, sep="\n")
    print(validation_test(random_board))


main(MIX_LOOP)
