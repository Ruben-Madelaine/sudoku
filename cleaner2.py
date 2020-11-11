import random


def clean(grid, n):
    for _ in range(n):
        i = random.randint(0, len(grid) - 1)
        j = random.randint(0, len(grid[0]) - 1)

        if grid[i][j]:
            grid[i][j] = 0


def logger(txt):
    if __name__ == "__main__":
        print(txt)


def main():
    from sudoku import Sudoku

    grid = [[i for i in range(1, 10)] for i in range(1, 10)]
    s = Sudoku(grid)
    clean(grid, 50)
    print(s)


if __name__ == "__main__":
    main()
