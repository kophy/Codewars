def first_non_repeating_letter(string):
    temp = string.lower();
    for c in string:
        if temp.count(c.lower()) == 1:
            return c;
    return '';