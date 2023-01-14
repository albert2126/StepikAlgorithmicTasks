def fb_square_sum(number):
    if number <= 1:
        return number
    crt, nxt = 0, 1
    for _ in range(1, number + 1):
        crt, nxt = nxt, (crt + nxt) % 10
    return (crt * nxt) % 10


if __name__ == '__main__':
    n = int(input())
    print(fb_square_sum(n % 60))


"""
Naive solution:

def fibonacci_sum_squares(n):
    if n <= 1:
        return n

    previous, current, sum = 0, 1, 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares(n))
"""