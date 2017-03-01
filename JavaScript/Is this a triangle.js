function isTriangle(a,b,c) {
    var check = function(a, b, c) {
        return a + b > c && Math.abs(a - b) < c;
    }
    return check(a, b, c) && check(b, c, a) && check(c, a, b);
}