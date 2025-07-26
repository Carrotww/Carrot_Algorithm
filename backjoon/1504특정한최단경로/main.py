
def dj(start, end):
    heap = []
    heapq.heappush(heap, (0, start))
    dist = [float('inf')] * (n + 1)
    dist[start] = 0

    while heap:
        cost, node = heapq.heappop(heap)

        if dist[node] < cost:
            continue

        for n_node, n_cost in graph[node]:
            if dist[n_node] > cost + n_cost:
                heapq.heappush(heap, (cost + n_cost, n_node))
                dist[n_node] = cost + n_cost

    return dist[end]

if __name__ == "__main__":
    import sys, heapq

    input = sys.stdin.readline
    
    n, m = map(int, input().split())

    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append([b, c])
        graph[b].append([a, c])

    path1, path2 = map(int, input().split())

    path = dj(path1, path2)
    result1 = dj(1, path1) + path + dj(path2, n)
    result2 = dj(1, path2) + path + dj(path1, n)

    if result1 == float('inf') and result2 == float('inf'):
        print(-1)
    else:
        print(min(result1, result2))
