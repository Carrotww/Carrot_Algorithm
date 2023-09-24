# https://www.acmicpc.net/problem/14938

if __name__ == "__main__":
    import sys
    import heapq
    from collections import defaultdict

    input = sys.stdin.readline

    n, m, r = map(int, input().split())
    graph = defaultdict(list)
    items = [0] + list(map(int, input().split()))

    for _ in range(r):
        start, end, dist = map(int, input().split())
        graph[start].append((end, dist))
        graph[end].append((start, dist))

    def dj(node):
        heap = [(0, node)]
        total_score = 0
        visited = [float('inf')] * (n + 1)
        visited[node] = 0
        while heap:
            dist, cur_node = heapq.heappop(heap)
            for n_node, n_dist in graph[cur_node]:
                if visited[n_node] > dist + n_dist and dist + n_dist <= m:
                    visited[n_node] = dist + n_dist
                    heapq.heappush(heap, (dist+n_dist, n_node))
        for i in range(1, n+1):
            if visited[i] == float('inf'):
                continue
            total_score += items[i]

        return total_score

    result = 0
    for node in range(1, n+1):
        result = max(result, dj(node))
    print(result)
