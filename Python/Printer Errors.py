def printer_error(s):
    error = sum([ord(c) > ord('m') for c in s]);
    return str(error) + "/" + str(len(s));