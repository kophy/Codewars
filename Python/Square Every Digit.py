def square_digits(num):
    data = [str(pow(int(c), 2)) for c in str(num)];
    return int("".join(data));