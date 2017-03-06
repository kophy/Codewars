var calc = s => {
    s = s.replace(/\s/g, '');
    s = s.replace(/--/g, '+');

    let rParenthesis = /\(([^(]*?)\)/;
    let rTerm = /(.*[^*/]\b)([+-])(.+)/;
    let rFactor = /(.+)([*/])(.+)/;
    let rDigit = /^[-+]?\d+(\.\d+)?$/;

    let temp;

    while (temp = rParenthesis.exec(s))
        s = s.replace(rParenthesis, calc(temp[1]));

    while (temp = rTerm.exec(s)) {
        let left = calc(temp[1]),
            right = calc(temp[3]);
        let operator = temp[2];
        let result = (operator === '+') ? left + right : left - right;
        s = s.replace(rTerm, result);
    }

    while (temp = rFactor.exec(s)) {
        let left = calc(temp[1]),
            right = calc(temp[3]);
        let operator = temp[2];
        let result = (operator === '*') ? left * right : left / right;
        s = s.replace(rFactor, result);
    }

    if (temp = rDigit.exec(s))
        return Number(temp[0]);
    return s;
};