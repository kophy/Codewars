function getNumberOrExpression(num, exp) {
    return exp == undefined? num : exp(num);
}

function zero(exp) { return getNumberOrExpression(0, exp); }
function one(exp) { return getNumberOrExpression(1, exp); }
function two(exp) { return getNumberOrExpression(2, exp); }
function three(exp) { return getNumberOrExpression(3, exp); }
function four(exp) { return getNumberOrExpression(4, exp); }
function five(exp) { return getNumberOrExpression(5, exp); }
function six(exp) { return getNumberOrExpression(6, exp); }
function seven(exp) { return getNumberOrExpression(7, exp); }
function eight(exp) { return getNumberOrExpression(8, exp); }
function nine(exp) { return getNumberOrExpression(9, exp); }

function plus(n2) {
    return function(n1) { return n1 + n2; };
}

function minus(n2) {
    return function(n1) { return n1 - n2; };
}

function times(n2) {
    return function(n1) { return n1 * n2; };
}

function dividedBy(n2) {
    return function(n1) { return n1 / n2; };
}