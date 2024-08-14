# https://www.acmicpc.net/problem/24444

def bfs(node):
    from collections import deque

    queue = deque()
    queue.append(node)
    visited[node] = 1
    cnt = 1

    while queue:
        cur_node = queue.popleft()
        
        for n_node in graph[cur_node]:
            if visited[n_node] == 0:
                visited[n_node] = cnt + 1
                cnt += 1
                queue.append(n_node)

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n, m, r = map(int, input().split())
    graph = [[] * (n + 1) for _ in range(n + 1)]

    for _ in range(m):
        start, end = map(int ,input().split())
        graph[start].append(end)
        graph[end].append(start)

    for i in range(n+1):
        graph[i].sort()

    visited = [0] * (n + 1)

    bfs(r)

    for i in range(1, n+1):
        print(visited[i])

