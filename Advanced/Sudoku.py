def get_user_input():
    print("Write the sudoku row by row. ")
    print("Use 0 for the empty positions and separate the digits with a single space")
    user_grid = []
    for i in range(9):
        while True:
            try:
                line = input(f"Row {i+1}: ")
                row = [int(x) for x in line.split()]
                if len(row) == 9:
                    user_grid.append(row)
                    break
                else:
                    print("Please enter a valid row.")
            except ValueError:
                print("Please enter valid digits.")
    return user_grid


def is_valid_move(grid, row, col, number):
    for x in range(9):
        if grid[row][x] == number:
            return False
    for x in range(9):
        if grid[x][col] == number:
            return False

    corner_row = row - row % 3
    corner_col = col - col % 3
    for x in range(3):
        for y in range(3):
            if grid[corner_row + x][corner_col + y] == number:
                return False
    return True


def solve(grid, row, column):
    if column == 9:
        if row == 8:
            return True
        row += 1
        column = 0
    if grid[row][column] > 0:
        return solve(grid, row, column + 1)
    for num in range(1, 10):
        if is_valid_move(grid, row, column, num):
            grid[row][column] = num
            if solve(grid, row, column + 1):
                return True
            grid[row][column] = 0
    return False

def print_sudoku(grid):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(grid[i][j], end=" ")
        print()

grid = get_user_input()
print("Solution")
if solve(grid, 0, 0):
    print_sudoku(grid)
else:
    print("No solution")
