def count_change(money, coins):
    if money == 0:
        return 0;
    data = [0] * (money + 1);
    data[0] = 1;
    for c in coins:
        for i in range(1, money + 1):
            if i >= c:
                data[i] += data[i - c];
    return data[money];