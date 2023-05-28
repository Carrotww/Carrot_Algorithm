# https://www.acmicpc.net/problem/1504

def solve():
    import sys, heapq
    from collections import defaultdict
    N, E = map(int, sys.stdin.readline().split())
    graph = defaultdict(list)

    for _ in range(E):
        start, end, time = map(int, sys.stdin.readline().split())
        graph[start].append([end, time])
        graph[end].append([start, time])
    v1, v2 = map(int, sys.stdin.readline().split())

    def dj(node, target_node):
        queue = [(0, node)]
        visited = [float('inf')] * (N + 1)
        visited[node] = 0
        while queue:
            cur_time, cur_node = heapq.heappop(queue)
            for n_node, n_time in graph[cur_node]:
                if visited[n_node] > cur_time + n_time:
                    visited[n_node] = cur_time + n_time
                    heapq.heappush(queue, [cur_time+n_time, n_node])
        return visited[target_node]

    result = dj(1, v1) + dj(v1, v2) + dj(v2, N)
    result2 = dj(1, v2) + dj(v2, v1) + dj(v1, N)
    temp = min(result, result2)
    if temp == float('inf'):
        print(-1)
    else:
        print(temp)

if __name__ == "__main__":
    solve()