"""
Greates common divisor.
Euclid's theorem
gcd(a, b) = gcd(b, a % b)
"""

def gcd(a, b):
    c = max(a, b)
    e = min(a, b)
    while e > 0:
        c, e = e, c % e
    return c


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(gcd(a, b))


"""
Naive solution:
def gcd(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd
"""