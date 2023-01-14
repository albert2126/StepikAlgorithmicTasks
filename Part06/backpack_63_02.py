from sys import stdin


def optimal_value(capacity, weights, values):
    value = 0.
    goods = sorted(zip(weights, values), key=lambda x: x[1] / x[0], reverse=True)
    for weight, price in goods:
        print(capacity, value, weight, price)
        if weight < capacity:
            value += price
            capacity -= weight
        else:
            value += price * capacity / weight
            break
    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))