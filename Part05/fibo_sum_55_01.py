def fibo_last_digit(number):
    if number <= 1:
        return number
    current, next = 0, 1
    for _ in range(2, number + 1):
        current, next = next, (current + next) % 10
    return next


if __name__ == '__main__':
    n = int(input())
    fb = fibo_last_digit((n + 2) % 60)
    print(fb - 1 if fb else 9)

    # for n in range(1, 1000):
    #     fb = fibo_last_digit(n)
    #     if fb == 0:
    #         print(n)
    #         break
