function dirReduc(arr) {
    var result = new Array();
    var match = {"NORTH" : "SOUTH", "SOUTH" : "NORTH", "EAST" : "WEST", "WEST" : "EAST"};
    
    for (var i = 0; i < arr.length; ++i) {
        var curr = arr[i];
        if (result.length == 0 || result[result.length - 1] != match[curr])
            result[result.length] = curr;
        else
            result.pop();
    }
    return result;
}