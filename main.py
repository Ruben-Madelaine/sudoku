class Sudoku:
    grid = []
    size = 0
    hilighted_values = []

    def __str__(self):
        txt = board_to_text(self, self.grid, self.cell_to_text)
        return "The great Sudoku !" + txt

    def cell_to_text(self, r):
        h = "*" if r in self.hilighted_values else " "
        c = f" {r}{h}"
        return c

    def set_grid(self, grid):
        if isinstance(grid, str):
            grid = [[int(v) for v in k] for k in txt_to_list(grid)]
        self.grid = grid
        self.size = len(grid)

    def hilight(self, number):
        self.hilighted_values += [number]


def txt_to_list(txt):
    return txt.replace(" ", "").split("\n")[1:-1]


def board_to_text(object, grid, cell_to_text):
    txt = ""
    main_sep = 3

    main_sep_v, main_sep_h, sub_sep_v, sub_sep_h = {
        "heavy": ["||", "=", ":", "-"],
        "light": ["|", "-", " ", " "],
    }["light"]

    for i, row in enumerate(grid):
        txt += "\n"
        line = ""
        sub_sep = ""
        for j, r in enumerate(row):
            c = object.cell_to_text(r)

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
    raw_sudoku = """
        004903008
        003050002
        978200000
        269030000
        000060000
        000090615
        000005486
        700080100
        400109500
    """

    sudoku = Sudoku()
    sudoku.set_grid(raw_sudoku)
    sudoku.hilight(2)
    print(sudoku)


if __name__ == "__main__":
    main()
