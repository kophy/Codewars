def find_longest(arr):
    arr_len = [len(str(n)) for n in arr];
    return arr[arr_len.index(max(arr_len))];