#!/usr/bin/python3
"""
This script contains a function to calculate the minimum number of coins
needed to achieve a given total. The function uses a dynamic programming
approach to find the optimal solution.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total.

    :param coins: List of integer values representing the coin denominations.
    :param total: The total amount to be made with the coins.
    :return: Fewest number of coins needed to meet total, or -1
             if not possible.
    """
    if total <= 0:
        return 0

    inf = float("inf")
    dp = [inf] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != inf else -1
