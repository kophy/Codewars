def is_balanced(source, caps):
    match = {};
    for i in range(0, len(caps), 2):
        match[caps[i]] = caps[i + 1];
    print(match)
    data = [];
    for c in source:
        if c not in caps:
            continue;
        elif c in match:
            if c == match[c] and len(data) > 0 and data[-1] == c:
                data.pop();
            else:
                data.append(match[c]);
        else:
            if len(data) <= 0 or data[-1] != c:
                return False;
            data.pop();
    return len(data) == 0;