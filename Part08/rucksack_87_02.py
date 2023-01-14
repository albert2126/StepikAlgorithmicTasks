"""Maximum Amount of Gold
Given a set of gold bars of various weights and a backpack that can hold at most WW pounds, place as much gold
as possible into the backpack.
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


def full_pack(weights, pack, capacity):
    pack[0][0] = True
    for w in range(capacity + 1):
        for i in range(1, len(weights) + 1):
            if weights[i - 1] > w:
                pack[w][i] = pack[w][i - 1]
            else:
                pack[w][i] = pack[w][i - 1] or pack[w - weights[i - 1]][i - 1]
    return pack


def maximum_gold(capacity, weights):
    bar_number = len(weights)
    init_pack = [[False] * (bar_number + 1) for _ in range(capacity + 1)]
    pack = full_pack(weights, init_pack, capacity)
    for cap in range(capacity, -1, -1):
        if pack[cap][bar_number]:
            return cap
    return 0


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
