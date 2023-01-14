"""
The Coin Game
Given an array formed by an even number of coins positioned on a line, two players take turns to take a coin from one of
the ends of the array until there are no coins left. Find the maximum amount of money the first player can win under
the assumption that the second player plays optimally.

Input: An integer array with an even number of elements that represents the values of coins positioned on a line.
Alice and Bob take turns to take a coin from one of the ends of the array until there are no coins left.
A player with the largest amount of money (total value of all taken coins) wins.

Output: The maximum amount of money the first player can win under the assumption that the second player plays
optimally.
"""

table = {}


def game(coins, i, k2):
    if k2 == 2:
        table[i, k2] = max(coins[i], coins[i + 1])
    else:
        k = k2 - 2
        a = table.get((i + 2, k))
        b = table.get((i + 1, k))
        c = table.get((i, k))
        if not a:
            a = game(coins, i + 2, k)
        if not b:
            b = game(coins, i + 1, k)
        if not c:
            c = game(coins, i, k)
        table[(i, k2)] = max((coins[i] + min(a, b)), (coins[i + k2 - 1] + min(b, c)))
    return table[(i, k2)]


if __name__ == '__main__':
    n = int(input())
    coins_init = list(map(int, input().split()))
    assert n == len(coins_init)
    print(game(coins_init, 0, n))
