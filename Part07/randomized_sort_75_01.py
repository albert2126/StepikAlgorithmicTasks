from random import randint


def partition3(array, left, right):
    middle, m1, m2 = array[left], left, left
    for i in range(left + 1, right + 1):
        # print(f"{i}, {array}, left: {left}, right: {right}, m1: {m1}, m2: {m2}")
        if array[i] == middle:
            m2 += 1
            array[m2], array[i] = array[i], array[m2]
        elif array[i] < middle:
            array[m1], array[i] = array[i], array[m1]
            m1 += 1
            m2 += 1
            array[m2], array[i] = array[i], array[m2]
    return m1, m2


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    print(m2 + 1, right)
    randomized_quick_sort(array, m2 + 1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)


"""
Initial code:

from random import randint


def partition3(array, left, right):
    # write your code here
    ...

def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
"""