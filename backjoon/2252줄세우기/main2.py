import sys

if __name__ == "__main__":
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)

    for _ in range(m):
        a, b = map(int, input().split())
        indegree[b] += 1
        graph[a].append(b)

    from collections import deque

    queue = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)

    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for n_node in graph[node]:
            indegree[n_node] -= 1
            if indegree[n_node] == 0:
                queue.append(n_node)

    print(' '.join(map(str, result)))
