def lps(s):
    n = len(s)
    table = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        table[i][i + 1] = 1
    for size in range(2, n + 1):
        for left in range(n - size + 1):
            right = left + size
            if s[left] == s[right - 1]:
                table[left][right] = table[left + 1][right - 1] + 2
            else:
                table[left][right] = max(table[left + 1][right], table[left][right - 1])
    return table[0][n]


if __name__ == '__main__':
    print(lps(input()))

"""
0123456789
bmanchdaem
"""