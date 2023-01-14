"""
Compute the minimum number of coins needed to change the given value into coins with denominations 11, 33, and 44.
Input: An integer \text{money}money.
Output: The minimum number of coins with denominations 11, 33, and 44 that changes \text{money}money.
"""

money = int(input())
n, m = money // 4, money % 4
print(2 if money == 2 else n if m == 0 else n + 1)
