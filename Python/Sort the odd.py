def sort_array(source_array):
    odd_nums = sorted([n for n in source_array if n % 2 == 1]);
    odd_inds = [i for i in range(len(source_array)) if source_array[i] % 2 == 1];
    for i in range(len(odd_inds)):
        source_array[odd_inds[i]] = odd_nums[i];
    return source_array;