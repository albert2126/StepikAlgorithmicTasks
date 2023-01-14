"""
Find the minimum number of operations needed to get a positive integer nn from 11 by using only three operations: add 1, multiply by 22, and multiply by 33.
Input: An integer nn.
Output: The minimum number of operations “+1+1”, “\times2×2”, and “\times 3×3” needed to get nn from 11.
"""


def compute_operations(n):
    current = 1
    ops = [1]
    while current < n:
        if current <= n // 3:
            current = 3 * ops[-1]
        elif current <= n // 2:
            current = 2 * ops[-1]
        else:
            current = 1 + ops[-1]
        ops = ops + [current]
    return ops


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
