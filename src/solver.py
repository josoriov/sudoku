# %% importing the libraries

import numpy as np

# %% Defining the sudoku grid

grid = [
    [0,0,0,0,3,0,0,0,9],
    [0,0,0,0,0,5,0,6,0],
    [0,0,0,0,0,7,5,0,8],
    [0,0,6,0,0,0,0,0,0],
    [3,2,0,0,0,0,6,0,0],
    [0,0,0,0,8,0,0,5,4],
    [0,3,0,0,5,0,0,0,0],
    [8,1,0,9,4,3,0,0,0],
    [9,0,0,0,0,8,0,0,0]
]

# Converting the grid to matrix for better indexing
grid_matrix = np.matrix(grid)
# grid_matrix[0,2] == 3
# grid_matrix[3,0] == 6

# %%
# Validation methods

# Check if number can be inputted into row
def check_row(sudoku_grid, x, num):
    sol = np.sum(np.isin(num, sudoku_grid[x,:]))
    if(sol == 0):
        return True
    else:
        return False

# Check if number can be inputted into column
def check_column(sudoku_grid, y, num):
    sol = np.sum(np.isin(num, sudoku_grid[:,y]))
    if(sol == 0):
        return True
    else:
        return False

# Check if number can be inputted into the 3x3 grid
def check_3_3(sudoku_grid, x, y, num):
    x_pos = x//3
    y_pos = y//3
    grid_3x3 = sudoku_grid[ x_pos*3:(x_pos+1)*3, y_pos*3:(y_pos+1)*3 ]

    sol = np.sum(np.isin(num, grid_3x3))
    if(sol == 0):
        return True
    else:
        return False

def check_possible(sudoku_grid, x, y, num):
    row = check_row(sudoku_grid, x, num)
    column = check_column(sudoku_grid, y, num)
    small_grid = check_3_3(sudoku_grid, x, y, num)
    if(row and column and small_grid):
        return True
    else:
        return False

# %%
# Solver algorithm
def solve(sudoku_grid):
    for x in range(9):
        for y in range(9):
            if(sudoku_grid[x,y] == 0):
                for n in range(1, 10):
                    if (check_possible(sudoku_grid, x, y, n)):
                        sudoku_grid[x, y] = n
                        solve(sudoku_grid)
                        sudoku_grid[x, y] = 0
                return "Completed :D"
    print(sudoku_grid)
# %%
solve(grid_matrix)
