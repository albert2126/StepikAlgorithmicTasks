def edit_distance(first_string, second_string):
    n, m = len(first_string), len(second_string)
    table = [[0] * (m + 1) for _ in range(n + 1)]
    table[0] = list(range(m + 1))
    for i in range(n + 1):
        table[i][0] = i
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            insertion = table[i][j - 1] + 1
            deletion = table[i - 1][j] + 1
            match = table[i - 1][j - 1]
            mismatch = table[i - 1][j - 1] + 1
            if first_string[i - 1] == second_string[j - 1]:
                table[i][j] = min(insertion, deletion, match)
            else:
                table[i][j] = min(insertion, deletion, mismatch)
    return table[n][m]


if __name__ == '__main__':
    print(edit_distance(input(), input()))
