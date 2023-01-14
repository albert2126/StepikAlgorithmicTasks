def optimal_summands(n):
    if n < 3:
        return [n]
    summands = []
    excluded = []
    rng, prev, curr, m = iter(range(1, n + 1)), 0, 0, n
    while m > 0:
        curr = next(rng)
        if curr not in excluded:
            m -= curr
            summands.append(curr)
            if m == 0:
                break
            elif m <= 0:
                excluded.append(prev)
                rng, m, prev, summands = iter(range(1, n + 1)), n, 0, []
                continue
            prev = curr
    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)


"""
Naive non-working solution:
def optimal_summands(n):
    summands = []
    for i in range(1, n):
        n -= i
        summands.append(i)
        if n < i + 1:
            break
    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
"""
