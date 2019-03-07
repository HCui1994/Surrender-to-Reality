def union_find(user_list):
    """ wa ?? """
    def _build_graph():
        import collections
        graph = collections.defaultdict(set)
        for l in user_list:
            for i in range(len(l) - 1):
                for j in range(i + 1, len(l)):
                    a, b = l[i], l[j]
                    graph[a].add(b)
                    graph[b].add(a)
        return graph

    graph = _build_graph()
    visited = set()

    def traverse(v):
        if v in visited:
            return
        visited.add(v)
        for u in graph[v]:
            traverse(u)

    cnt = 0
    for v in graph:
        if v not in visited:
            cnt += 1
            traverse(v)

    return cnt



def union_find_2(sets):
    """
    ac and fast
    """
    sets = [set(l) for l in sets]
    cnt = 0
    while sets: 
        unioned = False
        for i in range(len(sets) - 1):
            if sets[-1] & sets[i]:
                sets[i] |= sets[-1]
                unioned = True
                break
        sets.pop()
        if not unioned:
            cnt += 1
    return cnt
                

user_list = [[123, 234, 345], [234, 666], [666]]
print(union_find_2(user_list))
