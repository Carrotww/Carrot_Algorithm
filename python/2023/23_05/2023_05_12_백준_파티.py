# https://www.acmicpc.net/problem/1238

def solve():
    import sys, heapq
    from collections import defaultdict, deque
    
    N, M, X = map(int, sys.stdin.readline().split())
    graph = defaultdict(list)
    visited = [float('inf')] * (N+1)
    visited[X] = 0

    for _ in range(M):
        start, end, weight = map(int, sys.stdin.readline().split())
        graph[start].append([end, weight])
    
    for i in range(1, N+1):
        if i == X:
            continue
        heap = []
        heapq.heappush(heap, [0, i])
        t_visited = [float('inf')] * (N+1)
        t_visited[i] = 0
        while heap:
            cnt, cur_node = heapq.heappop(heap)
            for n_node, n_cnt in graph[cur_node]:
                if t_visited[n_node] > n_cnt + cnt:
                    t_visited[n_node] = n_cnt + cnt
                    heapq.heappush(heap, [cnt+n_cnt, n_node])
        visited[i] = t_visited[X]
    
    x_visited = [float('inf')] * (N+1)
    heap = []
    heapq.heappush(heap, [0, X])
    while heap:
        cnt, cur_node = heapq.heappop(heap)
        for n_node, n_cnt in graph[cur_node]:
            if x_visited[n_node] > cnt + n_cnt:
                x_visited[n_node] = cnt + n_cnt
                heapq.heappush(heap, [cnt+n_cnt, n_node])
    
    result = 0
    for a, b in zip(x_visited[1::], visited[1::]):
        result = max(result, a+b)
    
    print(result)

if __name__ == "__main__":
    solve()