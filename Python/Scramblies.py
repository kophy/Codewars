def scramble(s1,s2):
    diff = [0 for i in range(26)];
    for c in s1:
        diff[ord(c) - ord('a')] += 1;
    for c in s2:
        diff[ord(c) - ord('a')] -= 1;
    for i in range(26):
        if diff[i] < 0:
            return False;
    return True;