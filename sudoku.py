# pylint: disable=missing-docstring


def sudoku_validator(grid):
    valid_set = {1,2,3,4,5,6,7,8,9}


    for row in grid:
        if set(row) != valid_set:
            return False


    for col in range(9):
        column = []
        for row in range(9):
            column.append(grid[row][col])

        if set(column) != valid_set:
            return False


    for block_row in [0,3,6]:
        for block_col in [0,3,6]:
            square = []
            for r in range(block_row, block_row + 3):
                for c in range(block_col, block_col + 3):
                    square.append(grid[r][c])

            if set(square) != valid_set:
                return False

    return True
