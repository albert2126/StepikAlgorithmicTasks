def largest_number_naive(numbers):
    numbers = sorted(list(map(str, numbers)), reverse=True)
    changed = True
    while changed:
        changed = False
        for i in range(len(numbers) - 1):
            if numbers[i] + numbers[i + 1] < numbers[i + 1] + numbers[i]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                changed = True
                print(f"Changed: {changed}")
    largest = ''.join(numbers)
    return largest


if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number_naive(input_numbers))