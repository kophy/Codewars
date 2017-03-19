def generate(result, string, used, path):
    if len(path) == len(string):
        result.add(path);
    else:
        for i in range(len(used)):
            if not used[i]:
                used[i] = True;
                generate(result, string, used, path + string[i]);
                used[i] = False;

def permutations(string):
    result = set();
    used = [False] * len(string);
    generate(result, string, used, "");
    return result;