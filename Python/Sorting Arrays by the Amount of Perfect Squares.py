from math import sqrt
import itertools
from sets import Set

def check_perfsq(num):
    return pow(int(sqrt(num)), 2) == num;

def count_perfsq(num):
    digits = list(str(num));
    result = [];
    for comb in itertools.permutations(digits, len(digits)):
        n = int("".join(comb));
        if check_perfsq(n):
            result.append(n);
    return len(Set(result));

def sort_by_perfsq(arr):
    data = [];
    for num in arr:
        data.append((-count_perfsq(num), num));
    data = sorted(data);
    return [p[1] for p in data];