import re

def parse_molecule (formula):
    formula = re.sub('[\[\{]', '(', formula);
    formula = re.sub('[\]\}]', ')', formula);
    
    N = len(formula);
    stk = [];
    
    i = 0;
    while i < N:
        c = formula[i];
        if c.isdigit():
            val = 0;
            while i < N and formula[i].isdigit():
                c = formula[i];
                val = val * 10 + ord(c) - ord('0');
                i += 1;
            stk.append(val);
        else:
            if c.islower():
                stk[-1] += c;
            else:
                stk.append(c);
            i += 1;
    
    S = len(stk);
    result = [{}];
    
    i = 0;
    while i < S:
        if stk[i].isalpha():
            elem, cc = stk[i], 1;
            if i + 1 < S and isinstance(stk[i + 1], int):
                cc = stk[i + 1];
                i += 2;
            else:
                i += 1;
            if not elem in result[-1]:
                result[-1][elem] = cc;
            else:
                result[-1][elem] += cc;
        elif stk[i] == '(':
            result.append({});
            i += 1;
        elif stk[i] == ')':
            cc = 1;
            if i + 1 < S and isinstance(stk[i + 1], int):
                cc = stk[i + 1];
                i += 2;
            else:
                i += 1;
            for elem in result[-1]:
                if not elem in result[-2]:
                    result[-2][elem] = cc * result[-1][elem];
                else:
                    result[-2][elem] += cc * result[-1][elem];
            result.pop();
    return result[0];