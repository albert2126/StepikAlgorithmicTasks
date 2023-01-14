def optimal_summands(n):
    # if n < 3:
    #     return [n]
    summands, sum = [], 0
    for k in range(1, n + 1):
        if sum + 2 * k + 1 > n:
            summands.append(n - sum)
            break
        if sum + 2 * k + 1 == n:
            summands.append(k)
            summands.append(k+1)
            break
        sum += k
        summands.append(k)
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
