# https://www.acmicpc.net/problem/1766

def topologysort():
    from collections import deque
    import heapq

    heap = []
    result = []
    for i in range(1, n+1):
        if indegree[i] == 0:
            heap.append(i)

    while heap:
        cur_node = heapq.heappop(heap)
        result.append(cur_node)
        for n_node in graph[cur_node]:
            indegree[n_node] -= 1
            if indegree[n_node] == 0:
                heapq.heappush(heap, n_node)
    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split())
    indegree = [0] * (n + 1)
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        indegree[b] += 1
        graph[a].append(b)

    result = topologysort()
    print(' '.join([str(x) for x in result]))


