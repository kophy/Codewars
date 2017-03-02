function sumDigits(str) {
    var n = parseInt(str), temp = 0;
    while (n > 0) {
        temp += parseInt(n % 10);
        n = parseInt(n / 10);
    }
    return temp;
}

function orderWeight(strng) {
    weights = strng.split(" ");
    if (weights.length == 0)
        return "";
    weights.sort(function(a, b) {
        var na = sumDigits(a), nb = sumDigits(b);
        return (na > nb || ((na == nb) && (a > b)))? 1 : -1;
    });
    var result = weights[0];
    for (var i = 1; i < weights.length; ++i)
        result += " " + weights[i];
    return result;
}