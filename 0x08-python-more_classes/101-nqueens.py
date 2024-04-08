#!/usr/bin/python3
import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with empty spaces."""
    board = [[' ' for _ in range(n)] for _ in range(n)]
    return board


def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at position (row, col)."""
    # Check the column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 'Q':
            return False

    return True


def solve_nqueens(board, row, n, solutions):
    """Solve the N-queens problem recursively."""
    if row == n:
        solutions.append([row[:] for row in board])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'
            solve_nqueens(board, row + 1, n, solutions)
            board[row][col] = ' '  # Backtrack


def print_solutions(solutions):
    """Print the solutions."""
    for solution in solutions:
        print([[r, c] for r in range(len(solution)) for c in range(len(solution[0])) if solution[r][c] == 'Q'])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            raise ValueError
    except ValueError:
        print("N must be an integer greater than or equal to 4")
        sys.exit(1)

    board = init_board(n)
    solutions = []
    solve_nqueens(board, 0, n, solutions)
    print_solutions(solutions)

