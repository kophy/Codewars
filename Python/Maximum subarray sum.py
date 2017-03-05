from copy import deepcopy

def maxSequence(arr):
    if arr == None or len(arr) == 0:
        return 0;
    sums = deepcopy(arr);
    for i in range(1, len(sums)):
        sums[i] = max(sums[i], sums[i - 1] + arr[i]);
    return max(sums);