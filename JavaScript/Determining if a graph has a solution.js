function solve_graph(start, end, arcs) {
    let stack = [start];
    let visited = new Set();
    while (stack.length > 0) {
        let curr = stack.pop();
        if (curr == end)
            return true;
        visited.add(curr);
        for (let i = 0; i < arcs.length; ++i) {
            if (arcs[i].start == curr && !(visited.has(arcs[i].end)))
                stack.push(arcs[i].end);
        }
    }
    return false;
}