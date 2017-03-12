from queue import PriorityQueue

def dbl_linear(n):
    data = PriorityQueue();
    data.put(1);
    for i in range(n):
        curr = data.get();
        while not data.empty() and data.queue[0] == curr:
            data.get();
        data.put(curr * 2 + 1);
        data.put(curr * 3 + 1);
    return data.get();