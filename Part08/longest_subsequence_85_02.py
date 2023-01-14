def lcs2(first_sequence, second_sequence):
    n, m, length = len(first_sequence), len(second_sequence), 0
    table = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            table[i][j] = max(table[i][j - 1], table[i - 1][j])
            if first_sequence[i - 1] == second_sequence[j - 1]:
                table[i][j] = max(table[i][j], table[i - 1][j - 1] + 1)
    return table[n][m]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
