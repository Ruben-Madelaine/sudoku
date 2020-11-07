

class Sudoku:
    grid = []
    size = 0
    hilighted_values = []
    

    def __str__(self):
        txt = ""
        main_sep = 3

        main_sep_v, main_sep_h, sub_sep_v, sub_sep_h = {
            "heavy": ['||', '=',   ':', '-'],
            "light": ['|' , '-',    ' ', ' '],
        }["light"]

        hilight_char = ["*", "^"][0]

        for i, row in enumerate(self.grid):
            txt += "\n"
            line = ''
            sub_sep = ''
            for j, r in enumerate(row):
                h = hilight_char if r in self.hilighted_values else " "
                c = f" {r}{h}" 

                # Vertical separators
                use_main_sep_v = j>0 and (j+1)%main_sep == 0
                line += c + [sub_sep_v, main_sep_v][use_main_sep_v] if j < self.size-1 else c

                # Horizontal separators
                sub_sep += sub_sep_h*len(c) + [sub_sep_v, main_sep_v][use_main_sep_v] if j < self.size-1 else sub_sep_h*len(c)
                use_main_sep_h = i>0 and (i+1)%main_sep == 0
                sep = main_sep_h * len(line) if use_main_sep_h else sub_sep

            txt += "\n".join([line, sep]) if i < self.size-1 else line

        return "The great Sudoku !" + txt

    def set_grid(self, grid):
        if isinstance(grid, str):
            grid = [[int(v) for v in k] for k in txt_to_list(grid)]
        self.grid = grid
        self.size = len(grid)

    def hilight(self, number):
        self.hilighted_values += [number]


def txt_to_list(txt):
    return txt.replace(" ", "").split("\n")[1:-1]


def main():
    sudoku = """
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
