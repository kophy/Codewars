def to_underscore(string):
    if not isinstance(string, str):
        return str(string);
    if len(string) == 0 or not string[0].isalpha():
        return "";
    data = [];
    for c in string:
        if c.isalpha() and c.upper() == c:
            data.append("_" + c.lower());
        else:
            data[-1] += c;
    return "".join(data)[1:];