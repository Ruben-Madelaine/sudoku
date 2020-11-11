
from generator import generate
from cleaner import clean
from sudoku import Sudoku
from solver import Solver
from validator import validate

def test():
    sub_size = 3
    grid = generate(sub_size)
    clean(grid, 50)

    # store it in Sudoku
    sudoku = Sudoku(grid)
    # print(sudoku)

    solver = Solver(sudoku)
    solver.solve()
    # print(sudoku)

    return solver.is_completed(), validate(sudoku.grid), solver.count, solver.found


def main():
    results = []
    sample_size = 200
    for i in range(sample_size):
        results += [test()]

    # print(*results, sep="\n")
    solving_ratio = (len([b for b, _, _, _ in results if b])/sample_size) *100
    print(f"Solving ratio {solving_ratio}%")


if __name__ == "__main__":
    main()
