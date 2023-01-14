def max_pairwise_product(n, numbers):
    mx1 = max(numbers[0], numbers[1])
    mx2 = min(numbers[0], numbers[1])
    for i in range(2, n):
        if numbers[i] >= mx1:
            mx2, mx1 = mx1, numbers[i]
        elif numbers[i] > mx2:
            mx2 = numbers[i]
    return mx1 * mx2


if __name__ == '__main__':
    n = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(n, input_numbers))
