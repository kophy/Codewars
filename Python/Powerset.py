def dfs(result, nums, path, index):
    if index == len(nums):
        result.append(path[:]);
    else:
        dfs(result, nums, path, index + 1);
        path.append(nums[index]);
        dfs(result, nums, path, index + 1);
        path.pop();

def powerset(nums):
    result = [];
    dfs(result, nums, [], 0);
    return result;