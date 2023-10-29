# https://www.acmicpc.net/problem/1854

def dj(start):
    heap = [(0, start)]
    visited = [[] for _ in range(n + 1)]
    visited[start].append(0)

    while heap:
        cur_dist, cur_node = heapq.heappop(heap)
        for n_node, n_dist in graph[cur_node]:
            dist = cur_dist + n_dist
            if len(visited[n_node]) < k:
                heapq.heappush(heap, (dist, n_node))
                heapq.heappush(visited[n_node], -dist)
            elif dist < -visited[n_node][0]:
                heapq.heappush(heap, (dist, n_node))
                heapq.heappop(visited[n_node])
                heapq.heappush(visited[n_node], -dist)

    return visited


if __name__ == "__main__":
    import sys
    import heapq
    from collections import defaultdict

    input = sys.stdin.readline

    n, m, k = map(int, input().split())
    graph = defaultdict(list)

    for _ in range(m):
        start, end, dist = map(int, input().split())
        graph[start].append((end, dist))

    s = dj(1)

    for i in range(1, n+1):
        if len(s[i]) < k:
            print(-1)
        else:
            print(-s[i][0])
