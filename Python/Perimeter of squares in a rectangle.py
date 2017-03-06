def perimeter(n):
    data = [];
    for i in range(n + 1):
        data.append(data[-2] + data[-1] if i >= 2 else 1);
    return 4 * sum(data);