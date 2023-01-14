def change(money):
    count, coins = 0, [10, 5, 1]
    for coin in coins:
        div = money // coin
        if div > 0:
            money -= coin * div
            count += div
        if money == 0:
            break
    return count


if __name__ == '__main__':
    m = int(input())
    print(change(m))
