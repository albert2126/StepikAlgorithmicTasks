def maximum_value(ds):
    n = len(ds) // 2 + 1
    mins = [[float('inf')] * n for _ in range(n)]
    maxs = [[-float('inf')] * n for _ in range(n)]
    for i in range(n):
        mins[i][i] = maxs[i][i] = int(ds[i * 2])
    for s in range(1, n):
        for l in range(n - s):
            r = l + s
            for m in range(l, r):
                op = ds[m * 2 + 1]
                # print(f"l: {l}, m: {m}, r: {r}, op: {op}")
                a = eval(f"{mins[l][m]} {op} {mins[m + 1][r]}")
                b = eval(f"{mins[l][m]} {op} {maxs[m + 1][r]}")
                c = eval(f"{maxs[l][m]} {op} {mins[m + 1][r]}")
                d = eval(f"{maxs[l][m]} {op} {maxs[m + 1][r]}")
                mins[l][r] = min(mins[l][r], a, b, c, d)
                maxs[l][r] = max(maxs[l][r], a, b, c, d)
    return maxs[0][n - 1]


if __name__ == "__main__":
    print(maximum_value(input()))
