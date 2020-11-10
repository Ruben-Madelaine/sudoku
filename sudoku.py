
import display


class Sudoku:
    grid = []
    size = 0
    hilighted_values = []

    def __init__(self, grid):
        self.set_grid(grid)

    def __str__(self):
        txt = display.board_to_text(self, self.grid, self.cell_to_text)
        return "The great Sudoku !" + txt

    def cell_to_text(self, i, j):
        val = self.grid[i][j]
        h = "*" if val in self.hilighted_values else " "
        c = f" {val}{h}"
        return c

    def set_grid(self, grid):
        if isinstance(grid, str):
            grid = [[int(v) for v in k] for k in txt_to_list(grid)]
        self.grid = grid
        self.size = len(grid)

    def hilight(self, number):
        self.hilighted_values += [number]

    def play(self, val, i, j):
        # verify action
        self.grid[i][j] = val


def txt_to_list(txt):
    return txt.replace(" ", "").split("\n")[1:-1]


def main():
    raw_sudoku = """
        100004080
        040000010
        806200000
        000520700
        007040200
        061093000
        610002503
        080000060
        090300004
    """

    sudoku = Sudoku(raw_sudoku)
    sudoku.hilight(3)
    print(sudoku)

if __name__ == "__main__":
    main()
