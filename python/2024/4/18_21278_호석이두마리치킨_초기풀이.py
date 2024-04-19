# https://www.acmicpc.net/problem/21278

def dj(cur_node):
    import heapq
    visited = [0] * (n + 1)

    heap = [cur_node]
    while heap:
        cur_n = heapq.heappop(heap)
        for n_n in graph[cur_n]:
            if visited[n_n] == 0 and n_n != cur_node:
                heapq.heappush(heap, n_n)
                visited[n_n] = visited[cur_n] + 1
            elif visited[n_n] and visited[n_n] > visited[cur_n] + 1:
                heapq.heapush(heap, n_n)
                visited[n_n] = visited[cur_n] + 1
    return visited

def solve(a, b):
    a_chicken = dj(a)
    b_chicken = dj(b)
    total = 0

    for i in range(1, n+1):
        total += min(a_chicken[i]*2, b_chicken[i]*2)

    return total

if __name__ == "__main__":
    import sys, itertools
    input = sys.stdin.readline

    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        start, end = map(int, input().split())
        if not graph[start]:
            graph[start] = [end]
        else:
            graph[start].append(end)

        if not graph[end]:
            graph[end] = [start]
        else:
            graph[end].append(start)

    result = float('inf')
    a_building = -1
    b_building = -1

    for a, b in itertools.combinations([x for x in range(1, n+1)], 2):
        t = solve(a, b)
        if t < result:
            a_building, b_building, result = a, b, t

    print(a_building, b_building, result)


