

def board_to_text(object, grid, cell_to_text):
    txt = ""
    main_sep = 3

    main_sep_v, main_sep_h, sub_sep_v, sub_sep_h = {
        "heavy": ["||", "=", ":", "-"],
        "light": ["|", "-", " ", " "],
    }["light"]

    for i in range(object.size):
        txt += "\n"
        line = ""
        sub_sep = ""
        for j in range(object.size):
            c = object.cell_to_text(i, j).replace("0", " ")

            # Vertical separators
            use_main_sep_v = j > 0 and (j + 1) % main_sep == 0
            line += (
                c + [sub_sep_v, main_sep_v][use_main_sep_v]
                if j < object.size - 1
                else c
            )

            # Horizontal separators
            sub_sep += (
                sub_sep_h * len(c) + [sub_sep_v, main_sep_v][use_main_sep_v]
                if j < object.size - 1
                else sub_sep_h * len(c)
            )
            use_main_sep_h = i > 0 and (i + 1) % main_sep == 0
            sep = main_sep_h * len(line) if use_main_sep_h else sub_sep

        txt += "\n".join([line, sep]) if i < object.size - 1 else line

    return txt


def main():
    class Test:
        def __init__(self, grid):
            self.grid = grid
            self.size = len(grid)

        def __str__(self):
            txt = board_to_text(self, self.grid, self.cell_to_text)
            return "Test!" + txt

        def cell_to_text(self, i, j):
            val = self.grid[i][j]
            c = f" {val} "
            return c

    grid = [
        [1,0,0],
        [1,0,0],
        [1,0,2]
    ]
    test = Test(grid)

    print(test)

if __name__ == "__main__":
    main()