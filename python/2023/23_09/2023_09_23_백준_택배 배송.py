# https://www.acmicpc.net/problem/5972

if __name__ == "__main__":
    import sys
    import heapq
    from collections import defaultdict

    input = sys.stdin.readline

    N, M = map(int, input().split())
    graph = defaultdict(list)

    for _ in range(M):
        start, end, dist = map(int, input().split())
        graph[start].append((end, dist))
        graph[end].append((start, dist))

    heap = [(0, 1)]
    visited = [float('inf')] * (N + 1)
    visited[1] = 0

    result = 0

    while heap:
        dist, node = heapq.heappop(heap)
        if node == N:
            result = dist
            break
        for next, n_dist in graph[node]:
            if visited[next] > n_dist + dist:
                heapq.heappush(heap, (dist + n_dist, next))
                visited[next] = dist + n_dist

    print(result)