import numpy as np
from random import shuffle


MIX_LOOP = 4
sub = 3
size = sub**2


def generate_grid(sub, size):
    def add_offset(list, offset):
        s = len(list)
        return list[s-offset:] + list[:s-offset]

    grid = []    
    vals = list(range(1, size+1))

    for i in range(size):
        grid += [vals]

        vals = add_offset(vals, sub)
        if i>0 and (i+1)%sub == 0:
            vals = add_offset(vals, 1)

    return grid


def randomizer(grid):
	for i in range(2):
		random_grid = []
		for i in range(0, len(grid), 3):
			a = grid[i:i+3]
			shuffle(a)
			random_grid += a
	return random_grid


def mix_loop(grid,num):
	for i in range(num):
		grid = randomizer(grid)
		grid = np.transpose(grid).tolist()

	return grid

def main(num):
	filled_grid = generate_grid(sub, size)
	random_grid = mix_loop(filled_grid,num)

	print(*random_grid, sep = "\n")


main(MIX_LOOP)
