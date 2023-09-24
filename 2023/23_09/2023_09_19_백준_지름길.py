# https://www.acmicpc.net/problem/1446

if __name__ == "__main__":
    import sys, heapq
    
    input = sys.stdin.readline
    
    N, D = map(int, input().split())
    graph = [[] for _ in range(D + 1)]
    distance = [float('inf')] * (D + 1)

    for i in range(D):
        graph[i].append((i+1, 1))
    
    for _ in range(N):
        start, end, time = map(int, input().split())
        if end > D:
            continue
        graph[start].append((end, time))
    
    heap = []
    heapq.heappush(heap, (0, 0))
    distance[0] = 0
    
    while heap:
        dist, now = heapq.heappop(heap)

        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))
    
    print(distance[D])