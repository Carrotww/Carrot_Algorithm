# https://www.acmicpc.net/problem/1926

import sys
import copy

def bfs(x, y):
    from collections import deque
    
    queue = deque()
    queue.append([x, y])
    cnt = 1
    while queue:
        i, j = queue.popleft()
        for direct in range(4):
            n_i = i+dy[direct]
            n_j = j+dx[direct]
            if (n_i < 0 or n_i >= n) or (n_j < 0 or n_j >= m) or visited[n_i][n_j] != 0 or graph[n_i][n_j] != 1:
                continue
            visited[n_i][n_j] = 1
            queue.append([n_i, n_j])
            cnt += 1
    result.append(cnt)
    
if __name__ == "__main__":
    from collections import deque

    n, m = map(int, sys.stdin.readline().split())
    graph = [[0]*m for _ in range(n)]
    visited = copy.deepcopy(graph)
    queue = deque()
    queue.append([0, 0])

    for i in range(n):
        n_list = list(map(int, sys.stdin.readline().split()))
        for j in range(len(n_list)):
            if n_list[j] == 1:
                graph[i][j] = 1
    
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    result = [0]

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and visited[i][j] == 0:
                visited[i][j] = 1
                bfs(i, j)

    print(len(result) - 1)
    print(max(result))