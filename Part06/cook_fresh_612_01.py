def can_be_cooked(n, dishes, cook_time):
    print(cook_time)
    print(*dishes)
    if n == 1:
        return 'Yes'
    for i in range(n):
        cook_others = cook_time - dishes[i][0]
        if dishes[i][1] >= cook_others:
            del dishes[i]
            return can_be_cooked(n - 1, dishes, cook_others)
    return 'No'


if __name__ == '__main__':
    n = int(input())
    dishes = list(map(lambda x: (int(x[0]), int(x[1])), [input().split() for _ in range(n)]))
    cook_time_total = sum([x for x, _ in dishes])
    print(can_be_cooked(n, sorted(dishes, key=lambda x: -x[1]), cook_time_total))
