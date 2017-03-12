def longest_slide_down(pyramid):
    for i in range(1, len(pyramid)):
        pyramid[i][0] += pyramid[i - 1][0];
        pyramid[i][i] += pyramid[i - 1][i - 1];
        for j in range(1, i):
            pyramid[i][j] += max(pyramid[i - 1][j], pyramid[i - 1][j - 1]);
    return max(pyramid[-1]);