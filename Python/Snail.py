def snail(array):
    result = [];
    if len(array) == 0 or len(array[0]) == 0:
        return result;
    l, r, d, u = 0, len(array[0]) - 1, 0, len(array) - 1;
    while l <= r and d <= u:
        for j in range(l, r + 1):
            result.append(array[d][j]);
        d += 1;
        if d > u: break;
        for i in range(d, u + 1):
            result.append(array[i][r]);
        r -= 1;
        if r < l: break;
        for j in range(r, l - 1, -1):
            result.append(array[u][j]);
        u -= 1;
        if u < d: break;
        for i in range(u, d - 1, -1):
            result.append(array[i][l]);
        l += 1;
        if l > r: break;
    return result;