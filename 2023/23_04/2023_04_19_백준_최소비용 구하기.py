# https://www.acmicpc.net/problem/1916

def solve():
    import sys
    import heapq
    import math
    from collections import defaultdict

    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    graph = defaultdict(list)
    
    for _ in range(M):
        start, end, weight = map(int, sys.stdin.readline().split())
        graph[start].append([end, weight])
    
    start_city, end_city = map(int, sys.stdin.readline().split())
    visited = [math.inf] * (N+1)
    visited[start_city] = 0

    queue = [(0, start_city)]

    while queue:
        weight, cur_node = heapq.heappop(queue)
        if weight > visited[cur_node]:
            continue
        for end, n_weight in graph[cur_node]:
            if visited[end] > n_weight + weight:
                visited[end] = n_weight + weight
                heapq.heappush(queue, (n_weight + weight, end))
    
    print(visited[end_city])

if __name__ == "__main__":
    solve()