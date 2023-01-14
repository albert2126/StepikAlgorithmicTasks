table = {}
palindrom = {}


def lps(s, i, j):
    if (i, j) not in table:
        # print(f"i: {i}, j: {j}")
        if i == j:
            table[(i, j)] = 0
        elif i == j - 1:
            table[(i, j)] = 1
        else:
            if s[i] == s[j - 1]:
                table[(i, j)] = lps(s, i + 1, j - 1) + 2
            else:
                table[(i, j)] = max(lps(s, i + 1, j), lps(s, i, j - 1))
    return table[(i, j)]


def build_palindrom(s):
    n, pal_list = len(s), []
    for i in range(n, 0, -1):
        # print(pal_list)
        # print(*table[0])
        if table[(0, i)] == 1:
            if s[i - 1] != s[i]:
                pal_list.append(s[i - 1])
                pal_list = pal_list + list(reversed(pal_list))[1:]
            else:
                pal_list = pal_list + list(reversed(pal_list))
            break
        if table[(0, i)] == table[(0, i - 1)] + 2:
            pal_list.append(s[i - 1])
    return ''.join(pal_list)


if __name__ == '__main__':
    string = input()
    lps(string, 0, len(string))
    [print(k, v) for k, v in table.items()]
    print(build_palindrom(string))

"""
0123456789
bmanchdaem
dgdcgdhhddhgaehbbbce
dgdcgdhhdd
"""