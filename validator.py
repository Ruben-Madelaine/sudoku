

def validate(board):
    return (
        check_lines_and_zeros(board)
        == check_columns(board)
        == check_squares(board)
        == True
    )

def check_lines_and_zeros(board):
    errors = 0
    for row in board:
        if row.count(0) != 0:
            errors += 1
        for elem in row:
            if row.count(elem) > 1:
                errors += 1
    return errors == 0


def check_columns(board):
    columns = []
    for i in range(len(board)):
        col = []
        for row in board:
            col += [row[i]]
        columns += [col]

    return check_lines_and_zeros(columns)


def check_squares(board):
    errors = 0
    block = []
    ids = [3, 6, 9]
    all_squares = []

    for i in ids:
        for line in board:
            block += [line[(i - 3) : i]]
            if len(block) == 3:
                all_squares += [block]
                block = []

    for square in all_squares:
        for c in square:
            if square.count(c) > 1:
                errors += 1
    return errors == 0


def main():
    board = [
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
    res = validate(board)
    print(res)


if __name__ == "__main__":
    main()
