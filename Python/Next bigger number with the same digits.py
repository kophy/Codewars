def next_bigger(n):
    data = list(str(n));
    i, j = len(data) - 2, len(data) - 1;
    while i >= 0 and data[i] >= data[i + 1]:
        i -= 1;
    if i < 0:
        return -1;
    while data[j] <= data[i]:
        j -= 1;
    data[i], data[j] = data[j], data[i];
    data[i + 1:] = sorted(data[i + 1:]);
    return int("".join(data));