function gcd(a, b) {
    a = parseInt(a), b = parseInt(b);
    if (a > b)
        return gcd(b, a);
    if (b % a == 0)
        return a;
    return gcd(b % a, a);
}

function lcm(a, b) {
    a = parseInt(a), b = parseInt(b);
    return a * b / gcd(a, b);
}

function convertFrac(lst){
    var d = 1;
    for (var i = 0; i < lst.length; ++i)
        d = lcm(d, lst[i][1]);
    var result = "";
    for (var i = 0; i < lst.length; ++i) {
        result += "(" + (lst[i][0] * d / lst[i][1]).toString() + "," + d.toString() + ")";
    }
    return result;
}