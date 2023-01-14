from collections import namedtuple
from itertools import combinations
from math import sqrt


Point = namedtuple('Point', 'x y')


def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2


def minimum_distance_squared(points):
    length = len(points)
    if length <= 4:
        min_distance_squared = float("inf")
        for p1, p2 in combinations(points, 2):
            min_distance_squared = min(min_distance_squared, distance_squared(p1, p2))
        return min_distance_squared
    middle_index = length // 2
    min_distance_squared = min(minimum_distance_squared(points[:middle_index]),
                               minimum_distance_squared(points[middle_index:]))
    point = points[middle_index]
    band = []
    i = middle_index - 1
    while i >= 0 and (point.x - points[i].x) ** 2 < min_distance_squared:
        band.append(points[i])
        i -= 1
    i = middle_index
    while i < length and (points[i].x - point.x) ** 2 < min_distance_squared:
        band.append(points[i])
        i += 1
    band = sorted(band, key=lambda p: p.y)
    for i in range(len(band)):
        j = i + 1
        while j < len(band) and (band[i].y - band[j].y) ** 2 < min_distance_squared:
            if abs(band[i].x - point.x) <= abs(band[i].x - band[j].x):
                min_distance_squared = min(min_distance_squared, distance_squared(band[i], band[j]))
            j += 1
    return min_distance_squared


if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    print("{0:.9f}".format(sqrt(minimum_distance_squared(sorted(input_points, key=lambda p: p.x)))))


"""
Naive:
from collections import namedtuple
from itertools import combinations
from math import sqrt


Point = namedtuple('Point', 'x y')


def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2


def minimum_distance_squared_naive(points):
    min_distance_squared = float("inf")

    for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared,
                                   distance_squared(p, q))

    return min_distance_squared


if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    print("{0:.9f}".format(sqrt(minimum_distance_squared_naive(input_points))))
"""
