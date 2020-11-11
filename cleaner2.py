
import random
from sudoku import Sudoku

def clean(grid, n):
    for i in range(n):
        # pick rnd row
        i = random.randint(0, len(grid)-1)
        # pick rnd line
        j = random.randint(0, len(grid[0])-1)

        if grid[i][j]:
            grid[i][j] = 0
            logger(f"Clean cell ({i}, {j}) !")
        else:
            logger(f"The cell ({i}, {j}) is alreday empty !")

def logger(txt):
    if __name__ == "__main__":
        print(txt)
        
def main():
    grid = [[i for i in range(1,10)] for i in range(1, 10)]
    s = Sudoku(grid)
    print (*grid, sep='\n')
    clean(grid, 23)
    print (*grid, sep='\n')
    print(s)


if __name__ == "__main__":
    main()
