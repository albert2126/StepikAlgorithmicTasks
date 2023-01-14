def can_be_cooked(number, dishes, cook_time):
    if number == 1: return 'Yes'
    i, n = 0, number
    while dishes and i < n:
        print(f"n: {n}, i: {i}, dishes: {dishes}")
        cook_time_rest = cook_time - dishes[i][0]
        if dishes[i][1] >= cook_time_rest:
            cook_time = cook_time_rest
            del dishes[i]
            i, n = 0, n-1
        else:
            i += 1
    return 'No' if dishes else 'Yes'


if __name__ == '__main__':
    n = int(input())
    dishes = list(map(lambda x: (int(x[0]), int(x[1])), [input().split() for _ in range(n)]))
    cook_time_total = sum([x for x, _ in dishes])
    print(can_be_cooked(n, sorted(dishes, key=lambda x: -x[1]), cook_time_total))
