# https://www.acmicpc.net/problem/1238

def dj(start_node):
    heap = [[0, start_node]]
    visited = [float('inf')] * (n + 1)
    visited[start_node] = 0

    while heap:
        cur_time, cur_node = heapq.heappop(heap)
        for n_time, n_node in graph[cur_node]:
            if visited[n_node] > n_time + cur_time:
                heapq.heappush(heap, [cur_time + n_time, n_node])
                visited[n_node] = cur_time + n_time

    return visited

if __name__ == "__main__":
    import sys, heapq
    input = sys.stdin.readline

    n, m, x = map(int, input().split())
    graph = dict()
    for _ in range(m):
        start, end, time = map(int, input().split())
        if start not in graph:
            graph[start] = [[time, end]]
        else:
            graph[start].append([time, end])

    result = [0] * (n + 1)
    for i in range(1, n+1):
        cur_dj = dj(i)
        if i == x:
            for i in range(1, n+1):
                result[i] += cur_dj[i]
        result[i] += cur_dj[x]

    print(max(result[1:]))

