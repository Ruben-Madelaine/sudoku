from generator import generate
from cleaner2 import clean
from sudoku import Sudoku
from solver import Solver
from validator import validate


def test(sub_size, difficulty_lvl):
    grid = generate(sub_size)
    clean(grid, difficulty_lvl)
    sudoku = Sudoku(grid)

    solver = Solver(sudoku)
    solver.solve()

    return solver.is_completed(), validate(sudoku.grid), solver.count, solver.found


def main():
    sub_size = 3
    difficulty_lvl = 40

    sample_size = 200
    results = []

    for i in range(sub_size, sample_size):
        results += [test(sub_size, difficulty_lvl)]

    solving_ratio = (len([b for b, _, _, _ in results if b]) / sample_size) * 100
    print(f"Solving ratio {solving_ratio}%")


if __name__ == "__main__":
    main()
