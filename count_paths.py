def count_paths(grid, row=0, col=0):
    rows, cols = len(grid), len(grid[0])

    # Failure base cases: out of bounds or blocked by an obstacle
    if row >= rows or col >= cols or grid[row][col] == 1:
        return 0

    # Success base case: reached the bottom-right destination
    if row == rows - 1 and col == cols - 1:
        return 1

    # Recursive case: sum paths moving down and moving right
    down = count_paths(grid, row + 1, col)
    right = count_paths(grid, row, col + 1)
    return  down + right

grid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 1, 0]
]
print(count_paths(grid))