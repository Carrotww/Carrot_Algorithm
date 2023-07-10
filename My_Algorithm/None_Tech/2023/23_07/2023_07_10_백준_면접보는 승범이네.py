# https://www.acmicpc.net/problem/17835

def dj():
    import heapq
    visited = [float('inf')] * (n + 1)
    heap = []
    for t in target_city:
        visited[t] = 0
        heap.append((0, t))

    while heap:
        cur_cost, cur_node = heapq.heappop(heap)
        if visited[cur_node] < cur_cost:
            continue
        for n_node, cost in graph[cur_node]:
            if visited[n_node] > cur_cost + cost:
                heapq.heappush(heap, (cost+cur_cost, n_node))
                visited[n_node] = cost+cur_cost
    return visited


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n, m, k = map(int, input().split())
    graph = {x: [] for x in range(1, n+1)}
    for _ in range(m):
        u, v, c = map(int, input().split())
        graph[v].append((u, c))

    target_city = list(map(int, input().split()))
    visited = dj()
    max_val = 0

    for i in range(1, n+1):
        if visited[i] != float('inf'):
            max_val = max(max_val, visited[i])
    for i in range(1, n+1):
        if visited[i] == max_val:
            print(i)
            break
    print(max_val)
