

import inspect


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

    def play(self, i, j, val):
        # verify action
        self.grid[i][j] = val


class Solver:
    all_possibilities = []
    count = 0

    def __str__(self):
        txt = board_to_text(self, self.all_possibilities, self.cell_to_text)
        return "The great Solver !" + txt

    def cell_to_text(self, r):
        val = ','.join([str(v) for v in r])
        c = f" {val:^7.7} "
        return c

    def solve(self, sudoku):
        self.sudoku = sudoku
        self.size = sudoku.size

        self.retreive_all_possibilities()

        # use cell restriction
        while "solving sudoku":
            self.count += 1
            found_h = self.reduce_possibilities_horizontally()
            found_v = self.reduce_possibilities_vertically()
            found_s = self.reduce_possibilities_in_square()
            if not (found_h or found_v or found_s):
                break

        # look for single possible choice for zone
        found_h = self.single_choice_horizontally()
        found_v = self.single_choice_vertically()
        found_s = self.single_choice_in_square()

        # use zone restriction  

    def retreive_all_possibilities(self):
        for row in self.sudoku.grid:
            l = []
            for c in row:
                l.append([c] if c != 0 else [i for i in range(1, self.sudoku.size+1)])
            self.all_possibilities += [l]

    # ------------------- GLOBAL REDUCERS ------------------

    def reduce_possibilities_horizontally(self):
        found_restrictions = False
        print(f"\n{self.count}-", inspect.currentframe().f_code.co_name.title(), ":")
        for i, row in enumerate(self.all_possibilities):
            restrictions = self.get_restrictions(row)

            found = self.reduce_row(i, restrictions)
            if found:
                found_restrictions = True
        return found_restrictions

    def reduce_possibilities_vertically(self):
        found_restrictions = False
        print(f"\n{self.count}-", inspect.currentframe().f_code.co_name.title(), ":")
        for j in range(self.size):
            column = self.get_column(j)
            restrictions = self.get_restrictions(column)

            found = self.reduce_col(j, restrictions)
            if found:
                found_restrictions = True

        return found_restrictions

    def reduce_possibilities_in_square(self):
        found_restrictions = False
        print(f"\n{self.count}-", inspect.currentframe().f_code.co_name.title(), ":")
        square_size = 3
        for x in range(square_size):
            for y in range(square_size):
                square = self.get_square(square_size*x, square_size*y, square_size)
                restrictions = self.get_restrictions(square)

                found = self.reduce_square(x, y, square_size, restrictions)
                if found:
                    found_restrictions = True

        return found_restrictions

    # ------------------- GETTER ------------------

    def get_column(self, j):
        column = []
        for i in range(self.size):
            c = self.all_possibilities[i][j]
            column += [c]

        return column

    def get_square(self, square_x, square_y, square_size):
        square = []
        for i in range(square_size):
            for j in range(square_size):
                c = self.all_possibilities[square_x+i][square_y+j]
                square += [c]

        return square

    def get_restrictions(self, zone):
        return [c[0] for c in zone if len(c) == 1]

    # ------------------- REDUCERS ------------------

    def reduce_row(self, i, restrictions):
        found = False
        for j in range(self.size):
            c = self.all_possibilities[i][j]
            found = self.remove_possibilities(c, restrictions, i, j)
            
        return found

    def reduce_col(self, j, restrictions):
        found = False
        for i in range(self.size):
            c = self.all_possibilities[i][j]
            found = self.remove_possibilities(c, restrictions, i, j)
            
        return found

    def reduce_square(self, x, y, size, restrictions):
        found = False
        for k in range(self.size):
            i, j = size*x + k//size, size*y + k%size
            c = self.all_possibilities[i][j]
            found = self.remove_possibilities(c, restrictions, i, j)
        return found

    def remove_possibilities(self, cell, restrictions, i, j):
        intersection = set(cell) & set(restrictions)

        if len(cell) > 1 and len(intersection):
            [cell.remove(v) for v in intersection]
            if len(cell) == 1:
                print(f"Found a value at ({i}, {j}) !", cell[0])
                self.sudoku.play(i, j, cell[0])
            return True


    # ------------------- SINGLE CHOICE REDUCER ------------------

    def single_choice_horizontally(self):
        pass
        
    def single_choice_vertically(self):
        pass
        
    def single_choice_in_square(self):
        pass
        

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

    raw_sudoku = """
        100004080
        040000010
        806200000
        000520700
        007040200
        001093000
        000002503
        080000060
        090300004
    """

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

    sudoku = Sudoku()
    sudoku.set_grid(raw_sudoku)
    sudoku.hilight(1)
    sudoku.hilight(2)
    sudoku.hilight(3)
    print(sudoku)

    solver = Solver()
    solver.solve(sudoku)
    print(solver)
    print(sudoku)


if __name__ == "__main__":
    main()
