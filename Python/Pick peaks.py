def pick_peaks(arr):
    data = [];
    for i in range(len(arr)):
        if data == [] or data[-1][1] != arr[i]:
            data.append([i, arr[i]]);
    result = {"pos" : [], "peaks" : []};
    for i in range(1, len(data) - 1):
        if data[i][1] > data[i - 1][1] and data[i][1] > data[i + 1][1]:
            result["pos"].append(data[i][0]);
            result["peaks"].append(data[i][1]);
    return result;