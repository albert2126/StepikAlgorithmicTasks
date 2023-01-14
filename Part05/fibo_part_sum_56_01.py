def fibo_last_digit(number):
    if number <= 1:
        return number
    current, next = 0, 1
    for _ in range(2, number + 1):
        current, next = next, (current + next) % 10
    return next


if __name__ == '__main__':
    m, n = map(int, input().split())
    fbn = fibo_last_digit((n + 2) % 60)
    fbm = fibo_last_digit((m + 1) % 60)
    print((fbn - fbm + 10) % 10)


"""
Naive solution:
import sys


def fibonacci_partial_sum_naive(from_, to):
    _sum = 0

    current = 0
    _next = 1

    for i in range(to + 1):
        if i >= from_:
            _sum += current

        current, _next = _next, current + _next

    return _sum % 10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))
    
"""