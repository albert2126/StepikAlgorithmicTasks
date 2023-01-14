from sys import stdin


def points_cover(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)

    sorted_starts, sorted_ends = sorted(starts), sorted(ends)
    sorted_points = sorted(enumerate(points), key=lambda x: x[1])
    print(sorted_starts, sorted_ends, sorted_points)
    segments = 0
    for i in range(len(count)):
        point = sorted_points[i][1]
        print(sorted_starts, sorted_ends, point)
        while sorted_starts and sorted_starts[0] <= point:
            segments += 1
            sorted_starts.pop(0)
        while sorted_ends and sorted_ends[0] < point:
            segments -= 1
            sorted_ends.pop(0)
        count[sorted_points[i][0]] = segments
    return count


if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    output_count = points_cover(input_starts, input_ends, input_points)
    print(*output_count)

"""
Naive solution:
def points_cover_naive(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)

    for index, point in enumerate(points):
        for start, end in zip(starts, ends):
            if start <= point <= end:
                count[index] += 1

    return count

"""