def backtrack(result, target_sum, level, path, curr_sum):
    if len(path) > level or curr_sum > target_sum:
        return;
    if curr_sum == target_sum:
        if len(path) == level:
            result.append(int("".join(list(map(str, path)))));
        return;
    for i in range(path[-1], 10):
        path.append(i);
        backtrack(result, target_sum, level, path, curr_sum + i);
        path.pop();

def find_all(sum_dig, digs):
    data = [];
    for i in range(1, 10):
        backtrack(data, sum_dig, digs, [i], i);
    return [len(data), min(data), max(data)] if len(data) > 0 else [];
    