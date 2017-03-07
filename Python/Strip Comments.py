def solution(string, markers):
    data = string.split("\n");
    if len(data) == 0:
        return "";
    for i in range(len(data)):
        for m in markers:
            data[i] = data[i].split(m)[0];
        data[i] = data[i].strip();
    result = data[0];
    for i in range(1, len(data)):
        result += "\n" + data[i];
    return result;