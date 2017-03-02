function queueTime(customers, n) {
    var queue = new Array();
    for (var i = 0; i < n; ++i)
        queue[i] = 0;
    var result = 0;
    for (var j = 0; j < customers.length; ++j) {
    	var c = customers[j];
        var pos = 0;
        for (var i = 1; i < n; ++i)
            if (queue[i] < queue[pos])
                pos = i;
        queue[pos] += c;
        result = Math.max(result, queue[pos]);
    }
    return result;
}