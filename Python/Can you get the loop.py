def loop_size(node):
    slow, fast = node, node;
    while fast.next != None and fast.next.next != None:
        slow = slow.next;
        fast = fast.next.next;
        if slow == fast:
            loop = 0;
            while True:
                loop += 1;
                slow = slow.next;
                if slow == fast:
                    return loop;
    return None;