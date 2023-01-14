from sys import stdin


# def min_refills(distance, tank, stops):
#     count, pitstop, current, stop = 0, 0, 0, 0
#     for stop in stops:
#         # print(pitstop, current, stop)
#         if stop - pitstop <= tank:
#             current = stop
#         elif current == pitstop:
#             return -1
#         else:
#             pitstop = current
#             count += 1
#             if distance - pitstop <= tank:
#                 return count
#     if distance - pitstop <= tank:
#         return count
#     if distance - stop <= tank:
#         count += 1
#         return count
#     return -1

def min_refills(distance, tank, stops, location=0):
    if distance - location <= tank:
        return 0
    if not stops or stops[0] - location > tank:
        return float('inf')
    last_station = location
    while stops and stops[0] - location <= tank:
        last_station = stops[0]
        stops.pop(0)
    return 1 + min_refills(distance, tank, stops, last_station)


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    # d, m, _, *stops = 950, 400, 4, 200, 375, 550, 750
    count = min_refills(d, m, stops)
    if count == float('inf'):
        count = -1
    print(count)
