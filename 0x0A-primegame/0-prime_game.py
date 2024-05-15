#!/usr/bin/python3
"""Module to determine the winner of the prime game."""


def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def get_primes(n):
    """Get prime numbers up to n."""
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes


def isWinner(x, nums):
    """Determine the winner of each game."""
    winner_count = {"Maria": 0, "Ben": 0}

    for n in nums:
        primes = get_primes(n)
        if len(primes) % 2 == 0:
            winner_count["Ben"] += 1
        else:
            winner_count["Maria"] += 1

    if winner_count["Maria"] > winner_count["Ben"]:
        return "Maria"
    elif winner_count["Maria"] < winner_count["Ben"]:
        return "Ben"
    else:
        return None
