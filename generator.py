import numpy as np
from random import shuffle


def generate(sub_size):
    size = sub_size ** 2
    board = create_board(size, sub_size)
    return axial_shuffle(board, sub_size)


def create_board(size, sub_size):
    def add_offset(list, offset):
        s = len(list)
        return list[s - offset :] + list[: s - offset]

    board = []
    vals = list(range(1, size + 1))

    for i in range(size):
        board += [vals]

        vals = add_offset(vals, sub_size)
        if i > 0 and (i + 1) % sub_size == 0:
            vals = add_offset(vals, 1)

    return board


def axial_shuffle(board, sub_size):
    for i in range(2):
        board = randomize(board, sub_size)
        board = np.transpose(board).tolist()
    return board


def randomize(board, sub_size):
    random_board = []
    for i in range(0, len(board), sub_size):
        group_of_rows = board[i : i + sub_size]
        shuffle(group_of_rows)
        random_board += group_of_rows
    return random_board


def main():
    sub_size = 3
    random_board = generate(sub_size)
    print(*random_board, sep="\n")


if __name__ == "__main__":
    main()
