#!/usr/bin/python3
"""
Island Perimeter
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Args:
        grid (list of list of int): A list of list of integers
        representing the island.
            0 represents water, 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                if i == len(grid) - 1 or grid[i+1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                if j == len(grid[i]) - 1 or grid[i][j+1] == 0:
                    perimeter += 1
    return perimeter
