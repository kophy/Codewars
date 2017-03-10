import itertools

def recoverSecret(triplets):
    result = "";
    while len(triplets):
        tails = list(itertools.chain(*[list(t[1:]) for t in triplets]));
        heads = [t[0] for t in triplets]
        for c in heads:
            if c not in tails:
                result += c;
                for t in triplets:
                    if t[0] == c:
                        t.pop(0);
                break;
        triplets = [t for t in triplets if len(t) > 0];
    return result;