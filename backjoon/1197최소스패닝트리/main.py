import sys
sys.setrecursionlimit(10**6)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    v, e = map(int, input().split())
    graph = []
    parent = [i for i in range(v + 1)]
    for _ in range(e):
        a, b, c = map(int, input().split())
        graph.append([a, b, c])

    graph.sort(key=lambda x:x[2])

    result = 0
    for a, b, c in graph:
        if find(a) != find(b):
            union(a, b)
            result += c

    print(result)
