def get_sign(num):
    if num > 0:
        return 1;
    elif num < 0:
        return -1;
    return 0;

def sequence_classifier(arr):
    diff = [get_sign(arr[i] - arr[i - 1]) for i in range(1, len(arr))];
    inc, dec, cns = diff.count(1), diff.count(-1), diff.count(0);
    if inc == len(diff):
        return 1;
    elif inc > 0 and dec == 0 and cns > 0:
        return 2;
    elif dec == len(diff):
        return 3;
    elif dec > 0 and inc == 0 and cns > 0:
        return 4;
    elif cns == len(diff):
        return 5;
    return 0;