def get_length_of_missing_array(array_of_arrays):
    if len(array_of_arrays) <= 1 or None in array_of_arrays:
        return 0;
    data = sorted([len(array) for array in array_of_arrays]);
    if data[0] == 0:
        return 0;
    full = sum([i for i in range(data[0], data[-1] + 1)]);
    if data[-1] - data[0] != len(data):
        return 0;
    else:
        return full - sum(data);