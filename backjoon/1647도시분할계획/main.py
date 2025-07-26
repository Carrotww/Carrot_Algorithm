import sys

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
    input = sys.stdin.readline

    n, m = map(int, input().split())
    parent = [i for i in range(n + 1)]
    # n -> home cnt
    # m -> road cnt 

    graph = []
    for i in range(m):
        a, b, c = map(int ,input().split())
        graph.append([a, b, c])

    graph.sort(key=lambda x:x[2])

    result = 0
    c_list = []
    for a, b, c in graph:
        if find(a) != find(b):
            union(a, b)
            result += c
            c_list.append(c)

    print(result - c_list[-1])
