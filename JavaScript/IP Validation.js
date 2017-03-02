function isValidIP(str) {
    console.log(str)
    if(!/^\d+\.\d+\.\d+\.\d+$/.test(str))
        return false;
    var nums = str.split(".");
    for (var i = 0; i < 4; ++i) {;
        var n = parseInt(nums[i]);
        if (n < 0 || n > 255 || (nums[i] != 0 && nums[i].charAt(0) == '0'))
            return false;
    }
    return true;
}