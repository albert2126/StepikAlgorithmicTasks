def lcs3(first_sequence, second_sequence, third_sequence):
    n, m, l, length = len(first_sequence), len(second_sequence), len(third_sequence), 0
    table = [[[0] * (l + 1) for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, l + 1):
                table[i][j][k] = max(table[i][j][k - 1], table[i][j - 1][k], table[i - 1][j][k])
                if first_sequence[i - 1] == second_sequence[j - 1] and first_sequence[i - 1] == third_sequence[k - 1]:
                    table[i][j][k] = max(table[i][j][k], table[i - 1][j - 1][k - 1] + 1)
    return table[n][m][l]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))
