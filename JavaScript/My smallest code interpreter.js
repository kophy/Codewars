function brainLuck(code, input) {
    let stack = [],
        dict = {},
        output = "";
    for (let i = 0; i < code.length; ++i) {
        let c = code[i];
        if (c == ']') {
            while (stack.length > 0 && stack[stack.length - 1][1] != '[')
                stack.pop();
            let temp = stack.pop();
            dict[i] = temp[0];
            dict[temp[0]] = i;
        } else
            stack.push([i, c]);
    }
    let memory = [],
        ptr = 0;
    input = input.split('');
    for (let i = 0; i < code.length; ++i) {
        let c = code[i];
        // adjust memory when ptr is larger than current size
        while (ptr >= memory.length)
            memory.push(0);
        if (c == '>')
        ++ptr;
        else if (c == '<')
        --ptr;
        else if (c == '+')
            memory[ptr] = (memory[ptr] == 255) ? 0 : memory[ptr] + 1;
        else if (c == '-')
            memory[ptr] = (memory[ptr] == 0) ? 255 : memory[ptr] - 1;
        else if (c == '.')
            output += String.fromCharCode(memory[ptr]);
        else if (c == ',') {
            memory[ptr] = input[0].charCodeAt();
            input.shift();
        } else if (c == '[') {
            if (memory[ptr] === 0)
                i = dict[i];
        } else if (c == ']') {
            if (memory[ptr] !== 0)
                i = dict[i];
        }
    }
    return output;
}