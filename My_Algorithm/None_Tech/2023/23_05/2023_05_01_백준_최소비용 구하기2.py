# https://www.acmicpc.net/problem/11779

def solve():
    import sys
    import heapq
    from collections import defaultdict
    
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    graph = defaultdict(list)

    for _ in range(m):
        start, end, cost = map(int, sys.stdin.readline().split())
        graph[start].append([end, cost])
        
    start, end = map(int, sys.stdin.readline().split())
    visited = [float('inf') for _ in range(n+1)]
    visited[start] = 0
    path = [-1] * (n+1)

    heap = []
    heapq.heappush(heap, [0, start])

    while heap:
        cur_cost, cur_city = heapq.heappop(heap)
        if visited[cur_city] < cur_cost:
            continue
        for n_city, cost in graph[cur_city]:
            n_cost = cur_cost + cost
            if n_cost < visited[n_city]:
                visited[n_city] = n_cost
                path[n_city] = cur_city
                heapq.heappush(heap, [n_cost, n_city])
    
    result = []
    print(visited[end])

    while start != end:
        result.append(end)
        end = path[end]
    result.append(start)

    print(len(result))
    print(' '.join([str(x) for x in result[::-1]]))

if __name__ == "__main__":
    solve()