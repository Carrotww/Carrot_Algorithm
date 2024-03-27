# https://www.acmicpc.net/problem/1005

def topologysort(target):
    from collections import deque

    queue = deque()
    result = [0] * (n+1)
    total = 0
    for i in range(1, n+1):
        if indegree[i] == 0:
            queue.append(i)
            result[i] = time[i-1]

    while queue:
        cur_node = queue.popleft()

        for n_node in graph[cur_node]:
            indegree[n_node] -= 1
            result[n_node] = max(result[n_node], result[cur_node]+time[n_node-1])

            if indegree[n_node] == 0:
                queue.append(n_node)
    return result[target]

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n, k = map(int, input().split())
        time = list(map(int, input().split()))

        graph = [[] for _ in range(n+1)]
        indegree = [0] * (n+1)

        for _ in range(k):
            a, b = map(int, input().split())
            indegree[b] += 1
            graph[a].append(b)

        end_node = int(input())
        print(topologysort(end_node))

