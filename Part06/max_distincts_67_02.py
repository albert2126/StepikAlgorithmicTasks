def optimal_summands(n):
    if n < 3:
        return [n]
    summands = []
    rng, i, m = list(range(1, n + 1)), 0, n
    while rng and m > 0:
        print(i, m, rng)
        m -= rng[i]
        summands.append(rng[i])
        i += 1
        if m == 0:
            break
        if m < rng[i]:
            del rng[i - 1]
            m, i, summands = n, 0, []
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
