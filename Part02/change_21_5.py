"""
Source: https://stepik.org/lesson/862113/step/5?unit=866150
Task: Find the minimal number of coins to change a sum of money.
"""
import math


def BruteForceChange(money: int, c: list[int]) -> int:
    smallestNumberOfCoins = math.inf
    