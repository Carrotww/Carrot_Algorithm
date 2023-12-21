# https://www.acmicpc.net/problem/1766

def topologycal_sort(n, graph, indegree):
    queue = []
    for i in range(1, n+1):
        if i not in indegree:
            queue.append(i)

    result = []
    while queue:
        cur_node = heapq.heappop(queue)
        result.append(cur_node)

        for n_node in graph[cur_node]:
            indegree[n_node] -= 1
            if indegree[n_node] == 0:
                heapq.heappush(queue, n_node)

    return result

if __name__ == "__main__":
    import sys, heapq
    from collections import deque, defaultdict
    input = sys.stdin.readline

    n, m = map(int, input().split())

    indegree = defaultdict(int)
    graph = defaultdict(list)

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    result = topologycal_sort(n, graph, indegree)
    print(' '.join(map(str, result)))

