# https://www.acmicpc.net/problem/1922

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

if __name__ == "__main__":
    import sys, heapq
    input = sys.stdin.readline

    n = int(input())
    m = int(input())
    heap = []
    parent = [x for x in range(n+1)]

    for _ in range(m):
        a, b, cost = map(int, input().split())
        heapq.heappush(heap, (cost, a, b))
    
    total = 0
    while heap:
        cur_cost, a, b = heapq.heappop(heap)
        if find(a) == find(b):
            continue
        union(a, b)
        total += cur_cost

    print(total)

