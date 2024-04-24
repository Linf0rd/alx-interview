#!/usr/bin/python3
"""
Rotate an n x n 2D matrix 90 degrees clockwise in-place.

Args:
    matrix: A 2D list representing the n x n matrix.
"""


def rotate_2d_matrix(matrix):
  """
  Rotates a 2D matrix 90 degrees clockwise in-place.

  Performs the rotation by transposing the matrix and then reversing each row.

  Args:
      matrix: A 2D list representing the n x n matrix.
  """
  n = len(matrix)
  for i in range(n):
    for j in range(i, n):
      matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

  for row in matrix:
    row.reverse()
