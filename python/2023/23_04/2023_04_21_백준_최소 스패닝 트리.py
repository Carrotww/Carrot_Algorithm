# https://www.acmicpc.net/problem/1197

def solve2():
    import sys
    N, E = map(int, sys.stdin.readline().split())
    graph = []
    for i in range(E):
        start, end, weight = map(int, sys.stdin.readline().split())
        graph.append([start, end, weight])
    graph.sort(key=lambda x: x[2])

    result = 0
    parent = [x for x in range(N+1)]

    def find_parent(node):
        if parent[node] != node:
            return find_parent(parent[node])
        return parent[node]
    
    def union_parent(a, b):
        a = find_parent(a)
        b = find_parent(b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b 

    for start, end, weight in graph:
        if find_parent(start) != find_parent(end):
            union_parent(start, end)
            result += weight
    print(result)

def solve():
    import sys
    V, E = map(int, sys.stdin.readline().split())
    graph = []
    for _ in range(E):
        temp = list(map(int, sys.stdin.readline().split()))
        graph.append(temp)
    result = 0
    parent = [x for x in range(V+1)]
    graph.sort(key=lambda x:x[2])

    def find_parent(node):
        if parent[node] == node:
            return node
        return find_parent(parent[node])
    
    def union_parent(a, b):
        a_val = find_parent(a)
        b_val = find_parent(b)
        if a_val < b_val:
            parent[b_val] = a_val
        else:
            parent[a_val] = b_val
    
    for start, end, weight in graph:
        if find_parent(start) != find_parent(end):
            union_parent(start, end)
            result += weight
    print(result)
    
if __name__ == "__main__":
    solve()