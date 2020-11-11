# :memo: Sudoku

A sudoku generator and solver

## :tada: Examples

``` haskell
The great Sudoku !
 5   2   4 | 9   1   3 | 7   6   8 
           |           |           
 6   1   3 | 7   5   8 | 9   4   2 
           |           |           
 9   7   8 | 2   4   6 | 3   5   1 
-----------------------------------
 2   6   9 | 5   3   1 | 8   7   4 
           |           |           
 8   5   1 | 4   6   7 | 2   9   3 
           |           |           
 3   4   7 | 8   9   2 | 6   1   5 
-----------------------------------
 1   9   2 | 3   7   5 | 4   8   6 
           |           |           
 7   3   5 | 6   8   4 | 1   2   9 
           |           |           
 4   8   6 | 1   2   9 | 5   3   7 
```

## :spiral_calendar: Dates

### :rocket: Started 
Project pitched and started the _7th november 2020_

### :dart: Release date 
First expected release the friday **9th november 2020** 


## Dependencies
1. Set your Virtual Environment:

	``` bash
	# Download venv librairy
	apt-get install python3-venv -y
	# Create your venv
	py -m venv my_venv
	# Activate your venv
	. venv/bin/activate
	```
	
	_For more information, go to [Python Virtual Environment Official Documentation](https://docs.python.org/3/library/venv.html)._

1. Install the project dependencies:

	``` bash
	apt install python3-pip
	pip install numpy
	```


## :clipboard: Tasks

- [x] Print a sudoku board
- [x] Solve the sudoku automatically
- [ ] Allow a user to play
- [ ] Solve any Sudoku's variants 
- [ ] Try to create an hexagonal sudoku

- [ ] Display solver related stats (curves)
- [ ] Compete between solvers
