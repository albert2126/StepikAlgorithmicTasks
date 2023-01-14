def gcd(a, b):
    c = max(a, b)
    e = min(a, b)
    while e > 0:
        c, e = e, c % e
    return c


if __name__ == '__main__':
    aa, bb = map(int, input().split())
    divisor = gcd(aa, bb)
    print(aa * bb // divisor)
