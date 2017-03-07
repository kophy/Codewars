import re

def increment_string(strng):
    digit = re.compile(r"\d+$");
    match = digit.search(strng);
    if match != None:
        head = strng[:match.span()[0]];
        tail = strng[match.span()[0]:];
        return head + str(int(tail) + 1).zfill(len(tail));
    else:
        return strng + "1";