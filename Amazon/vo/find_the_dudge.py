import collections

def find_the_judge(n, trust):
    all_people = set(range(1, n + 1))
    trusting = collections.default(set)
    trusted = collections.default(set)
    for a, b in trust:
        trusting[a].add(b)
        trusted[b].add(a)
    candidate = all_people - trusting.keys()
    for c in candidate:
        if len(trusted[c]) == n - 1:
            return c
    return -1
