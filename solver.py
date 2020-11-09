
import inspect
import display


class Cell:
    options = []
    value = 0

    def __init__(self, i, j):
        self.pos = (i, j)

    def __str__(self):
        return f"{self.pos}: {self.value if self.value else ','.join(self.options)}"

    def is_empty(self):
        return self.value == 0

    def remove(self, value):
        self.options.remove(value)

    def one_option_left(self):
        return len(self.options) == 1

    def set_value(self, value):
        self.value = value
        self.options = []


class Solver:
    all_options = {}
    count = 0

    def __str__(self):
        txt = display.board_to_text(self, self.all_options, self.cell_to_text)
        return "The great Solver !" + txt

    def cell_to_text(self, i, j):
        cell = self.all_options[(i,j)]
        elems = [cell.value] if cell.value else cell.options
        val = ','.join([str(v) for v in elems])
        c = f" {val:^7.7} "
        return c

    def solve(self, puzzle):
        self.puzzle = puzzle
        self.size = puzzle.size

        self.retreive_all_possibilities()

        # use cell restriction
        while "solving puzzle":
            self.count += 1
            found_h = self.reduce_options_horizontally()
            found_v = self.reduce_options_vertically()
            found_s = self.reduce_options_in_square()
            if not (found_h or found_v or found_s):
                break

        # look for single possible choice for zone
        found_h = self.single_choice_horizontally()
        found_v = self.single_choice_vertically()
        found_s = self.single_choice_in_square()

        # use zone restriction  

    def retreive_all_possibilities(self):
        for i in range(self.puzzle.size):
            for j in range(self.puzzle.size):
                c = Cell(i, j)
                if self.puzzle.grid[i][j]:
                    c.value = self.puzzle.grid[i][j]
                else:
                    c.options = [i for i in range(1, self.puzzle.size+1)]
                self.all_options[(i,j)] = c


    # ------------------- GLOBAL REDUCERS ------------------

    def reduce_options_horizontally(self):
        found_restrictions = False
        print(f"\n{self.count}-", inspect.currentframe().f_code.co_name.title(), ":")
        for i in range(self.size):
            row = self.get_row(i)
            restrictions = self.get_zone_restrictions(row)

            found = self.reduce_row(i, restrictions)
            if found:
                found_restrictions = True
        return found_restrictions

    def reduce_options_vertically(self):
        found_restrictions = False
        print(f"\n{self.count}-", inspect.currentframe().f_code.co_name.title(), ":")
        for j in range(self.size):
            column = self.get_column(j)
            restrictions = self.get_zone_restrictions(column)

            found = self.reduce_col(j, restrictions)
            if found:
                found_restrictions = True

        return found_restrictions

    def reduce_options_in_square(self):
        found_restrictions = False
        print(f"\n{self.count}-", inspect.currentframe().f_code.co_name.title(), ":")
        square_size = 3
        for x in range(square_size):
            for y in range(square_size):
                square = self.get_square(square_size*x, square_size*y, square_size)
                restrictions = self.get_zone_restrictions(square)

                found = self.reduce_square(x, y, square_size, restrictions)
                if found:
                    found_restrictions = True

        return found_restrictions

    # ------------------- GETTER ------------------

    def get_row(self, i):
        row = []
        for j in range(self.size):
            c = self.all_options[(i,j)]
            row += [c]

        return row

    def get_column(self, j):
        column = []
        for i in range(self.size):
            c = self.all_options[(i,j)]
            column += [c]

        return column

    def get_square(self, square_x, square_y, square_size):
        square = []
        for i in range(square_size):
            for j in range(square_size):
                c = self.all_options[(square_x+i,square_y+j)]
                square += [c]

        return square

    def get_zone_restrictions(self, zone):
        return [cell.value for cell in zone if cell.value]

    def get_zone_options(self, zone):
        return [cell.options for cell in zone if not cell.value]

    # ------------------- REDUCERS ------------------

    def reduce_row(self, i, restrictions):
        found = False
        for j in range(self.size):
            c = self.all_options[(i,j)]
            found = self.remove_options(c, restrictions, i, j)
            
        return found

    def reduce_col(self, j, restrictions):
        found = False
        for i in range(self.size):
            c = self.all_options[(i,j)]
            found = self.remove_options(c, restrictions, i, j)
            
        return found

    def reduce_square(self, x, y, size, restrictions):
        found = False
        for k in range(self.size):
            i, j = size*x + k//size, size*y + k%size
            c = self.all_options[(i,j)]
            found = self.remove_options(c, restrictions, i, j)
        return found

    def remove_options(self, cell, restrictions, i, j):
        intersection = set(cell.options) & set(restrictions)

        if cell.is_empty() and len(intersection):
            [cell.remove(v) for v in intersection]
            if cell.one_option_left():
                cell.set_value(cell.options[0])
                self.puzzle.play(cell.value, *cell.pos)
                print(f"Found a value at {cell} !")
                
            return True


    # ------------------- SINGLE CHOICE REDUCER ------------------

    def single_choice_horizontally(self):
        for i in range(self.size):
            row = self.get_row(i)
            # print("row", row)
            options = self.get_zone_options(row)
            print("options", options)


    def single_choice_vertically(self):
        pass

    def single_choice_in_square(self):
        pass


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

    from sudoku import Sudoku
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
