function generateKthDigit(result, neighbor, observed, temp) {
    if (temp.length == observed.length) {
        result[result.length] = temp;
        return;
    }
    var c = observed.charAt(temp.length);
    for (var i = 0; i < neighbor[c].length; ++i)
        generateKthDigit(result, neighbor, observed, temp + neighbor[c][i]);
}

function getPINs(observed) {
    var neighbor = new Array();
    neighbor["0"] = new Array(0, 8);
    neighbor["1"] = new Array(1, 2, 4);
    neighbor["2"] = new Array(1, 2, 3, 5);
    neighbor["3"] = new Array(2, 3, 6);
    neighbor["4"] = new Array(1, 4, 5, 7);
    neighbor["5"] = new Array(2, 4, 5, 6, 8);
    neighbor["6"] = new Array(3, 5, 6, 9);
    neighbor["7"] = new Array(4, 7, 8);
    neighbor["8"] = new Array(0, 5, 7, 8, 9);
    neighbor["9"] = new Array(6, 8, 9);
    
    var result = new Array();
    generateKthDigit(result, neighbor, observed, "");
    return result;
}