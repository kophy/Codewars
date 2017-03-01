function findNb(m) {
    for (var i = 1; m > 0; ++i) {
        m -= Math.pow(i, 3);
    if (m == 0)
        return i;
    }
    return -1;
}