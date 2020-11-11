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
    found = 0

    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.size = puzzle.size

        self.retreive_all_possibilities()
        self.reduce_cells_options()

    def __str__(self):
        txt = display.board_to_text(self, self.all_options, self.cell_to_text)
        return (
            f"The great Solver ! found {self.found} values in {self.count} iterations"
            + txt
        )

    def cell_to_text(self, i, j):
        cell = self.all_options[(i, j)]
        show_max_options = 3
        elems = (
            [cell.value]
            if cell.value
            else cell.options
            if len(cell.options) <= show_max_options
            else [f"({len(cell.options)})"]
        )
        val = ",".join([str(v) for v in elems])
        c = f" {val:^7.7} "
        return c

    def solve(self):
        found_at_least_one = True
        while found_at_least_one:
            found_at_least_one = self.apply_single_choice_rule()

    def is_completed(self):
        for row in self.puzzle.grid:
            if 0 in row:
                return False
        return True

    def retreive_all_possibilities(self):
        for i in range(self.puzzle.size):
            for j in range(self.puzzle.size):
                c = Cell(i, j)
                if self.puzzle.grid[i][j]:
                    c.value = self.puzzle.grid[i][j]
                else:
                    c.options = [i for i in range(1, self.puzzle.size + 1)]
                self.all_options[(i, j)] = c

    def reduce_cells_options(self):
        found_at_least_one_value = False
        while "solving puzzle":
            self.count += 1
            logger(self.count)
            found_h = self.reduce_options(self.get_row)
            found_v = self.reduce_options(self.get_col)
            found_s = self.reduce_options(self.get_sqr)

            if not found_at_least_one_value and (found_h or found_s or found_v):
                found_at_least_one_value = True

            if not (found_h or found_v or found_s):
                break
        return found_at_least_one_value

    def apply_single_choice_rule(self):
        found_h = self.single_choices(self.get_row)
        found_v = self.single_choices(self.get_col)
        found_s = self.choices_in_square()
        return found_h or found_v or found_s

    # ------------------- GLOBAL REDUCERS ------------------

    def reduce_options(self, get_zone):
        found_restrictions = False
        for z in range(self.size):
            zone = get_zone(z)
            if self.reduce_zone(zone):
                found_restrictions = True
        return found_restrictions

    # ------------------- GETTER ------------------

    def get_row(self, i):
        row = []
        for j in range(self.size):
            row += [self.all_options[(i, j)]]
        return row

    def get_col(self, j):
        column = []
        for i in range(self.size):
            column += [self.all_options[(i, j)]]
        return column

    def get_sqr(self, s):
        square = []
        sqr_size = int(self.size ** (1 / 2))

        x, y = (s // sqr_size) * sqr_size, (s % sqr_size) * sqr_size
        for k in range(self.size):
            i, j = x + k // sqr_size, y + k % sqr_size

            square += [self.all_options[(i, j)]]
        return square

    def get_restrictions(self, zone):
        return [cell.value for cell in zone if cell.value]

    def get_options(self, zone):
        list_of_options = [cell.options for cell in zone if not cell.value]
        # flatten the list of sublists
        return [opt for options in list_of_options for opt in options]

    def retrieve_pos(self, zone, choice):
        for i, c in enumerate(zone):
            if choice in c.options:
                return c.pos

    # ------------------- REDUCERS ------------------

    def reduce_zone(self, zone):
        found_new = False
        restrictions = self.get_restrictions(zone)
        for c in zone:
            found = self.remove_options(c, restrictions)

            if not found_new and found:
                found_new = True
        return found_new

    def remove_options(self, cell, restrictions):
        intersection = set(cell.options) & set(restrictions)

        if cell.is_empty() and len(intersection):
            for v in intersection:
                cell.remove(v)

            if cell.one_option_left():
                self.set_value(cell, cell.options[0])

            return True

    # ------------------- SETTER ------------------

    def set_value(self, cell, value):
        self.found += 1
        cell.set_value(value)
        cell.options = []

        self.puzzle.play(cell.value, *cell.pos)
        logger(f"Found a value at {cell} !")

    # ------------------- SINGLE CHOICE REDUCER ------------------

    def single_choices(self, get_zone):
        found_new_value = False
        for i in range(self.size):
            zone = get_zone(i)

            count_options = self.count_options(zone)
            found_new_value = self.single_choice(zone, count_options)
        return found_new_value

    def choices_in_square(self):
        found_new_value = False
        for s in range(self.size):
            square = self.get_sqr(s)

            count_options = self.count_options(square)
            found_s = self.single_choice(square, count_options)

            if not found_new_value and found_s:
                found_new_value = True

        return found_new_value

    def count_options(self, zone):
        options = self.get_options(zone)
        # count duplicate options per zone
        return {opt: options.count(opt) for opt in set(options)}

    def single_choice(self, zone, count_options):
        found_new_value = False
        # get only single choices
        single_choices = [k for k, v in count_options.items() if v == 1]

        if single_choices:
            found_new_value = True

            cells_and_choices = self.retrieve_cells_and_choice(zone, single_choices)
            for cell, choice in cells_and_choices:
                self.set_value(cell, choice)
                self.reduce_cells_options()

        return found_new_value

    def retrieve_cells_and_choice(self, zone, choices):
        cells = []
        for choice in choices:
            pos = self.retrieve_pos(zone, choice)
            cells += [[self.all_options[pos], choice]]
        return cells


def logger(txt):
    if __name__ == "__main__":
        print(txt)


def logger(txt):
    if __name__ == "__main__":
        print(txt)
        

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

    from sudoku import Sudoku

    sudoku = Sudoku(raw_sudoku)
    sudoku.hilight(4)

    test_time(sudoku)

def simple_test(sudoku):
    solver = Solver(sudoku)
    solver.solve()
    print(solver)
    print(sudoku)
    print(solver.is_completed())

def test_time(sudoku):
    import time
    import datetime

    t0 = time.time()
    simple_test(sudoku)
    t1 = time.time()

    total = t1 - t0
    print("Total time:", str(datetime.timedelta(seconds=total)))


if __name__ == "__main__":
    main()
