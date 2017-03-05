def sum_two_smallest_numbers(numbers):
    data = list(filter(lambda x: x > 0, numbers));
    data.sort();
    return data[0] + data[1];