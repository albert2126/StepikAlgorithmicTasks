from bisect import bisect_left


def count_smaller(lst, x):
    # print(f"Count_smaller: {lst}, {x}")
    if x > lst[0]:
        left, right = 0, len(lst) - 1
        while left < right:
            # print(f"Left: {left}, right: {right}")
            idx = (left + right) // 2
            if x <= lst[idx]:
                left = idx + 1
            else:
                right = idx - 1
        return len(lst[:right]) if x < lst[right] else len(lst[:right + 1])
    return 0


def inversions(a):
    length = len(a)
    if length == 1:
        return 0
    left = a[: length // 2]
    right = a[length // 2:]
    ivs_internal = inversions(left) + inversions(right)
    right = sorted(right)
    return ivs_internal + sum([bisect_left(right, x) for x in left])


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(inversions(elements))


"""
Naive solution:
from itertools import combinations


def inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(inversions_naive(elements))
"""