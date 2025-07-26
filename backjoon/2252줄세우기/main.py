import sys
from collections import deque

if __name__ == "__main__":
    input = sys.stdin.readline

    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    result = []

    while q:
        node = q.popleft()
        result.append(node)

        for n_node in graph[node]:
            indegree[n_node] -= 1
            if indegree[n_node] == 0:
                q.append(n_node)

    print(' '.join(map(str, result)))
