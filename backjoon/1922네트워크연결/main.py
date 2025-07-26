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
    import sys, heapq

    input = sys.stdin.readline

    n = int(input())
    m = int(input())

    parent = [x for x in range(n + 1)]
    heap = []

    for _ in range(m):
        a, b, c = map(int, input().split())
        heapq.heappush(heap, (c, a, b))

    result = 0
    while heap:
        cost, a, b = heapq.heappop(heap)
        if find(a) != find(b):
            union(a, b)
            result += cost

    print(result)
