def max_sum(numbers):
    length = len(numbers)
    if length == 1:
        return numbers[0]
    sum = max(max_sum(numbers[:length // 2]), max_sum(numbers[length // 2:]))
    left_sum = current_sum = numbers[length // 2 - 1]
    for i in range(length // 2 - 2, -1, -1):
        current_sum += numbers[i]
        if current_sum > left_sum:
            left_sum = current_sum
    right_sum = current_sum = numbers[length // 2]
    for i in range(length // 2 + 1, length):
        current_sum += numbers[i]
        if current_sum > right_sum:
            right_sum = current_sum
    return max(sum, left_sum + right_sum)


def max_sum_naive(numbers):
    sum = 0
    for i in range(len(numbers)):
        cur_sum = 0
        for j in range(i, len(numbers)):
            cur_sum += numbers[j]
            if cur_sum > sum:
                sum = cur_sum
    if sum == 0:
        sum = max(numbers)
    return sum


if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    assert n == len(numbers)
    print(max_sum(numbers))
    print(max_sum_naive(numbers))
