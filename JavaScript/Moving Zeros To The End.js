var moveZeros = function (arr) {
    var j = 0;
    for (var i = 0; i < arr.length; ++i)
        if (typeof arr[i] != "number" || arr[i] != 0)
            arr[j++] = arr[i];
    for (; j < arr.length; ++j)
        arr[j] = 0;
    return arr;
}