# Puzzle format
# [
#     [-1, -1, -1, -1, -1, -1, -1, -1, -1]
#     [-1, -1, -1, -1, -1, -1, -1, -1, -1]
#     ...
#     [-1, -1, -1, -1, -1, -1, -1, -1, -1]
# ]

def is_valid(puzzle, guess, row, col):
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    row_start = (row // 3) * 3
    col_start = (col // 3) * 3  
    grid_vals = [puzzle[i][j] for i in range(row_start, row_start +3) for j in range(col_start, col_start+3)]
    if guess in grid_vals:
        return False

    return True

def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r,c
    return None,None

def solve_sudoku(puzzle):
    # Look for next empty location
    row,col = find_next_empty(puzzle)

    if row is None and col is None: # all locations filled 
        return True
    for guess in range(1, 10):    
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            if solve_sudoku(puzzle):
                return True
        
        puzzle[row][col] = -1

    return False