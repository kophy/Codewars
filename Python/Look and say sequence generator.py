from itertools import groupby

def look_and_say(s):
    num_cc = [(key, len(list(group))) for key, group in groupby(list(s))];
    result = "".join([str(cc) + num for num, cc in num_cc]);
    return result;
    

def look_and_say_sequence(first_element, n):
    for i in range(n - 1):
        first_element = look_and_say(first_element);
    return first_element;