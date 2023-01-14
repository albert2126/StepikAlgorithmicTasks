"""
Find the minimum number of operations needed to get a positive integer nn from 11 by using only three operations: add 1, multiply by 22, and multiply by 33.
Input: An integer nn.
Output: The minimum number of operations “+1+1”, “\times2×2”, and “\times 3×3” needed to get nn from 11.
"""
import math
from copy import copy


def compute_operations(n):
    table = {k: {'ops': [], 'count': 0} for k in range(1, n)}
    table[1] = {'ops': [1], 'count': 0}
    for k in range(2, n + 1):
        table_local = {i: {'ops': [], 'count': math.inf} for i in range(1, 4)}
        table_local[1] = copy(table[k - 1])
        table_local[1]['ops'] = table_local[1]['ops'] + [table_local[1]['ops'][-1] + 1]
        if k % 2 == 0:
            table_local[2] = copy(table[k // 2])
            table_local[2]['ops'] = table_local[2]['ops'] + [table_local[2]['ops'][-1] * 2]
        if k % 3 == 0:
            table_local[3] = copy(table[k // 3])
            table_local[3]['ops'] = table_local[3]['ops'] + [table_local[3]['ops'][-1] * 3]
        table[k] = min(table_local.values(), key=lambda v: v['count'])
        table[k]['count'] += 1
    return table[n]['ops']


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
