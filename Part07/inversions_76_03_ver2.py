def merge(left, right):
    sorted_list, inversions = [], 0
    while left and right:
        if left[0] <= right[0]:
            sorted_list.append(left.pop(0))
        else:
            sorted_list.append(right.pop(0))
            inversions += len(left)
    sorted_list.extend(left)
    sorted_list.extend(right)
    return sorted_list, inversions


def sort_count(lst):
    length = len(lst)
    if length == 1:
        return 0
    left = lst[: length // 2]
    right = lst[length // 2: length]
    left_ivs = sort_count(left)
    right_ivs = sort_count(right)
    lst, inversions = merge(left, right)
    return left_ivs + right_ivs + inversions


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(sort_count(elements))


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