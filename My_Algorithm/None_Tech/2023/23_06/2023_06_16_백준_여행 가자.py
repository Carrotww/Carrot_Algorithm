# https://www.acmicpc.net/problem/1976

def solve():
    import sys
    from collections import defaultdict, deque

    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    graph = defaultdict(set)
    for i in range(1, n+1):
        city = 1
        for j in list(map(int, sys.stdin.readline().split())):
            if j == 1 or city == i:
                graph[i].add(city)
                graph[city].add(i)
            city += 1

    route = list(map(int, sys.stdin.readline().split()))
    check = set()
    queue = deque()
    queue.append(route[0])

    while queue:
        cur_city = queue.popleft()
        for n_city in graph[cur_city]:
            if (cur_city, n_city) not in check:
                check.add((cur_city, n_city))
                queue.append(n_city)

    check_city = set()
    for a, b in check:
        check_city.add(a)
        check_city.add(b)

    is_yes = True
    for r in route:
        if r not in check_city:
            is_yes = False
            break
    if is_yes:
        print('YES')
    else:
        print('NO')

def solve1():
    import sys

    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    parent = dict()
    travel_path = dict()

    for i in range(1, n+1):
        parent[i] = i
        travel_path[i] = [i]

    def find_parent(parent, x):
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]
    
    def union(parent, travel_path, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)

        # if a < b:
        #     parent[b] = a
        #     travel_path[a] += travel_path[b]
        # else:
        #     parent[a] = b
        #     travel_path[b] += travel_path[a]
        if a != b:
            parent[b] = a
            travel_path[a] += travel_path[b]

    for i in range(1, n+1):
        temp = list(map(int, sys.stdin.readline().split()))
        city = 1
        for te in temp:
            if te == 1 or i == city:
                union(parent, travel_path, i, city)
            city += 1
    
    route = list(map(int, sys.stdin.readline().split()))
    check = set(travel_path[find_parent(parent, route[0])])

    is_yes = True
    for re in route:
        if re not in check:
            is_yes = False
            break
    
    if is_yes:
        print('YES')
    else:
        print('NO')

def solve2():
    import sys

    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    parent = dict()
    travel_path = dict()

    for i in range(1, n+1):
        parent[i] = i
        travel_path[i] = {i}

    def find_parent(parent, x):
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]
    
    def union(parent, travel_path, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)

        if a < b:
            parent[b] = a
            for t in travel_path[b]:
                travel_path[a].add(t)
        else:
            parent[a] = b
            for t in travel_path[a]:
                travel_path[b].add(t)

    for i in range(1, n+1):
        temp = list(map(int, sys.stdin.readline().split()))
        city = 1
        for te in temp:
            if te == 1 or i == city:
                union(parent, travel_path, i, city)
            city += 1
    
    route = list(map(int, sys.stdin.readline().split()))
    check = travel_path[find_parent(parent, route[0])]

    is_yes = True
    for re in route:
        if re not in check:
            is_yes = False
            break
    
    if is_yes:
        print('YES')
    else:
        print('NO')

if __name__ == "__main__":
    solve2()
