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
    from collections import defaultdict, deque
    input = sys.stdin.readline

    n = int(input())
    m = int(input())
    parent = [x for x in range(n+1)]

    cost = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        heapq.heappush(cost, [c, a, b])
    result = 0

    while cost:
        c, a, b = heapq.heappop(cost)
        a, b = find(a), find(b)
        if a != b:
            union(a, b)
            result += c

    print(result)

