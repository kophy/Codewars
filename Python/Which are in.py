def in_array(array1, array2):
    result = set();
    for s in array1:
        for t in array2:
            if s in t:
                result.add(s);
    return sorted(list(result));