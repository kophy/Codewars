var sum_pairs = function(ints, s) {
    var val2idx = new Array();
    for (var i = 0; i < ints.length; ++i) {
        var target = s - ints[i];
        if (target in val2idx)
            return new Array(target, ints[i]);
        val2idx[ints[i]] = i;
    }
    return undefined;
}