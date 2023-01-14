from sys import stdin


def partition3(values):
    total = sum(values)
    if total % 3:
        return 0
    n, part = len(values), total // 3
    split = [[[False] * (part + 1) for _ in range(part + 1)] for _ in range(n + 1)]
    split[0][0][0] = True
    for i in range(1, n + 1):
        for s1 in range(part + 1):
            for s2 in range(part + 1):
                split[i][s1][s2] = split[i - 1][s1][s2]
                if s1 >= values[i - 1]:
                    split[i][s1][s2] = split[i][s1][s2] or split[i - 1][s1 - values[i - 1]][s2]
                if s2 >= values[i - 1]:
                    split[i][s1][s2] = split[i][s1][s2] or split[i - 1][s1][s2 - values[i - 1]]
    return int(split[n][part][part])


if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))
