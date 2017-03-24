def valid(i, j, M, N):
    return i >= 0 and i < M and j >= 0 and j < N;

def mark_future(cells, i, j):
    M, N = len(cells), len(cells[0]);
    count = 0;
    for di in range(-1, 2):
        for dj in range(-1, 2):
            if (di != 0 or dj != 0) and valid(i + di, j + dj, M, N):
                count += cells[i + di][j + dj] % 2;
    # live
    if cells[i][j] % 2 == 1:
        if count == 2 or count == 3:
            cells[i][j] += 2;
    # dead
    else:
        if count == 3:
            cells[i][j] += 2;

def generate(past):
    M, N = len(past), len(past[0]);
    next = [];
    for i in range(M + 2):
        next.append([0 for j in range(N + 2)]);
    # enlarge cells
    for i in range(M):
        for j in range(N):
            next[i + 1][j + 1] = past[i][j];
    
    # mark state in next step
    for i in range(0, M + 2):
        for j in range(0, N + 2):
            mark_future(next, i, j);
    
    for i in range(0, M + 2):
        for j in range(0, N + 2):
            next[i][j] /= 2;
    
    # shrink cells
    while sum(next[0]) == 0:
        del next[0];
    while sum(next[-1]) == 0:
        del next[-1];
    while sum([row[0] for row in next]) == 0:
        for row in next:
            del row[0];
    while sum([row[-1] for row in next]) == 0:
        for row in next:
            del row[-1];
    return next;

def get_generation(cells, generations):
    temp = cells;
    for i in range(generations):
        temp = generate(temp);
    return temp;