#!/usr/bin/python3
"""
Program that solves the N queens problem.
"""
import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col].
    Args:
        board: A list of lists representing the chessboard
        row: The current row to check
        col: The current column to check

    Returns:
        True if it's safe to place a queen, else False
    """
    for i in range(col):
        if board[row][i]:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True


def solve_nqueens(board, col):
    """
    Solve the N queens problem recursively using backtracking.
    Args:
        board: A list of lists representing the chessboard
        col: The current column to check

    Returns:
        True if all queens are placed, else False
    """
    n = len(board)

    if col >= n:
        return True

    for i in range(n):
        if is_safe(board, i, col):
            board[i][col] = 1

            if solve_nqueens(board, col + 1):
                return True

            board[i][col] = 0

    return False


def print_solution(board):
    """
    Print the solution to the N queens problem.
    Args:
        board: A list of lists representing the chessboard
    """
    for row in board:
        print(row)


def nqueens(n):
    """
    Solve the N queens problem for a given value of N.
    Args:
        n: The size of the chessboard (number of rows/columns)

    Returns:
        None
    """
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * n for _ in range(n)]

    if not solve_nqueens(board, 0):
        print("No solution exists")
        sys.exit(1)

    for solution in board:
        print_solution([solution])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    nqueens(N)
