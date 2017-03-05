def mumble(d):
    return "-" + d[1].upper() + d[1].lower() * d[0];

def accum(s):
    data = list(map(mumble, [(i, s[i]) for i in range(len(s))]));
    return "".join(data)[1:];