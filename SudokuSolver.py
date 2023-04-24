def solve(board):
    """
    Solves a Sudoku board using a backtracking algorithm.

    :param board: A 9x9 list representing the Sudoku board, where empty cells are represented by 0s.
    :return: True if a solution is found, False otherwise.
    """

    # Find the next empty cell
    row, col = find_empty_cell(board)

    # If there are no more empty cells, the board is solved
    if row is None:
        return True

    # Try each possible number in the empty cell
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            # If the number is valid, place it in the cell
            board[row][col] = num

            # Recursively try to solve the rest of the board
            if solve(board):
                return True

            # If the recursion failed, backtrack and try the next number
            board[row][col] = 0

    # If no number works, the board is unsolvable
    return False


def find_empty_cell(board):
    """
    Finds the next empty cell in a Sudoku board.

    :param board: A 9x9 list representing the Sudoku board, where empty cells are represented by 0s.
    :return: A tuple (row, col) representing the coordinates of the next empty cell, or (None, None) if there are no more empty cells.
    """

    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col

    return None, None


def is_valid(board, row, col, num):
    """
    Checks if a number is valid in a given cell of a Sudoku board.

    :param board: A 9x9 list representing the Sudoku board, where empty cells are represented by 0s.
    :param row: The row index of the cell to check.
    :param col: The column index of the cell to check.
    :param num: The number to check.
    :return: True if the number is valid in the cell, False otherwise.
    """

    # Check row and column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check 3x3 box
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if board[i][j] == num:
                return False

    return True
