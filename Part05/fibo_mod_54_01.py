def pisano_period(modulo):
    current, next, period = 0, 1, 0
    while True:
        old_next = next
        next = (current + next) % modulo
        current = old_next
        period += 1
        if (current, next) == (0, 1):
            print(f"Period: {period}")
            return period


def fibo_mod(number, modulo):
    if number <= 1:
        return number
    current, next = 0, 1
    for _ in range(2, number + 1):
        current, next = next, (current + next) % modulo
    return next


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibo_mod(n % pisano_period(m), m))
