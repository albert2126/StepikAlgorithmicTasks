fibo = {}

def fibonacci_number(n):
    if n <= 1:
        return n
    fb = fibo.get(n)
    if fb:
        return fb
    fb = fibonacci_number(n - 1) + fibonacci_number(n - 2)
    fibo.setdefault(n, fb)
    return fb


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
