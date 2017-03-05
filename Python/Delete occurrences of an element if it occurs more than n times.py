def delete_nth(order,max_e):
    count = {};
    for c in order:
        count[c] = max_e;
    result = [];
    for c in order:
        count[c] -= 1;
        if count[c] >= 0:
            result.append(c);
    return result;