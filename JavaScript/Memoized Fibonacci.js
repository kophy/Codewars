var fibonacci = (function() {
    var memo = {};
    
    function f(n) {
        var value = n;
        if (n in memo) {
            value = memo[n];
        } else {
            if (n > 1)
                value = f(n - 1) + f(n - 2);
            memo[n] = value;
        }
        return value;
    }
    return f;
})();