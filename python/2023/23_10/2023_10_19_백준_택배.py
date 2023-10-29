# https://www.acmicpc.net/problem/1719

def dj(node):
    heap = [(0, node)]
    visited = [float('inf')] * (n + 1)
    prev = [-1] * (n + 1)
    visited[node] = 0

    while heap:
        cost, cur_node = heapq.heappop(heap)
        if visited[cur_node] < cost:
            continue
        for n_node, n_cost in graph[cur_node]:
            if visited[n_node] > cost + n_cost:
                heapq.heappush(heap, (n_cost + cost, n_node))
                visited[n_node] = cost + n_cost
                prev[n_node] = cur_node

    return prev


if __name__ == "__main__":
    import sys
    import heapq
    from collections import defaultdict

    input = sys.stdin.readline

    n, v = map(int, input().split())
    graph = defaultdict(list)

    for _ in range(v):
        start, end, cost = map(int, input().split())
        graph[start].append((end, cost))
        graph[end].append((start, cost))

    result = []
    for node in range(1, n+1):
        path = dj(node)
        t = []
        for i in range(1, n+1):
            if i == node:
                t.append('-')
            else:
                cur_node = i
                while path[cur_node] != node:
                    cur_node = path[cur_node]
                t.append(str(cur_node))
        print(' '.join(t))
