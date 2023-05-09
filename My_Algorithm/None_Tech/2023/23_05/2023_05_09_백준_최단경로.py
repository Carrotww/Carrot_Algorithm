# https://www.acmicpc.net/problem/1753

def solve():
    import sys
    import heapq
    from collections import defaultdict
    # V -> node cnt E -> edge cnt
    V, E = map(int, sys.stdin.readline().split())
    # K -> start node
    K = int(sys.stdin.readline())
    graph = defaultdict(list)
    visited = [float('inf')] * (V + 1)
    visited[K] = 0

    for _ in range(E):
        start, end, w = map(int, sys.stdin.readline().split())
        graph[start].append([end, w])
    
    heap = []
    heapq.heappush(heap, [0, K])

    while heap:
        cur_weight, cur_node = heapq.heappop(heap)
        for n_node, n_weight in graph[cur_node]:
            if cur_weight + n_weight < visited[n_node]:
                visited[n_node] = cur_weight + n_weight
                heapq.heappush(heap, [cur_weight + n_weight, n_node])
    
    for i in range(1, len(visited)):
        if visited[i] == float('inf'):
            print('INF')
        else:
            print(visited[i])

if __name__ == "__main__":
    solve()