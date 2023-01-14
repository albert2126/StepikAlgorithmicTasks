"""
Maximum Amount of Gold
Given a set of gold bars of various weights and a backpack that can hold at most WW pounds, place as much gold as possible into the backpack.
Input: A set of nn gold bars of integer weights w_{1}, \dotsc, w_{n}w
1
​
 ,…,w
n
​
  and a backpack that can hold at most WW pounds.
Output: A subset of gold bars of maximum total weight not exceeding WW.
"""


from sys import stdin


def memoized(weights, pack, w, i):
    if (w, i) not in pack:
        if i == 0 and w == 0:
            pack[(w, i)] = True
        elif i == 0 and w > 0:
            pack[(w, i)] = False
        elif i > 0 and weights[i - 1] > w:
            pack[(w, i)] = memoized(weights, pack, w, i - 1)
        else:
            pack[(w, i)] = memoized(weights, pack, w, i - 1) or \
                           memoized(weights, pack,
                                    w - weights[i - 1], i - 1)

    return pack[(w, i)]


if __name__ == '__main__':
    input_capacity, input_n, *input_weights = \
        list(map(int, stdin.read().split()))
    assert len(input_weights) == input_n
    memorized_pack = {}
    for s in range(input_capacity, -1, -1):
        if memoized(input_weights, memorized_pack, s, input_n):
            print(s)
            break