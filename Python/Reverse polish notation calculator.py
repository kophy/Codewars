def calc(expr):
    stack = [];
    for e in expr.split():
        if e in ["+", "-", "*", "/"]:
            n1, n2 = stack[-2], stack[-1]; 
            del stack[-2:];
            if e == "+":
                stack.append(n1 + n2);
            elif e == "-":
                stack.append(n1 - n2);
            elif e == "*":
                stack.append(n1 * n2);
            else:
                stack.append(n1 / n2);
        else:
            stack.append(eval(e));
    return stack[-1] if len(stack) > 0 else 0;