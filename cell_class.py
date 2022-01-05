class cell:
    row = 0
    column = 0
    value = 0
    # adjacent values
    left_cell_value = 0
    right_cell_value = 0
    up_cell_value = 0
    down_cell_value = 0

    def __init__(self, r, c, puzzle):
        self.row = r
        self.column = c
        self.value = puzzle[r][c]
        # adding adjacent values
        if c > 0:
            self.left_cell_value = puzzle[r][c - 1]
        if c < 8:
            self.right_cell_value = puzzle[r][c + 1]
        if r > 0:
            self.up_cell_value = puzzle[r - 1][c]
        if r < 8:
            self.down_cell_value = puzzle[r + 1][c]
