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
    n, m = map(int, sys.stdin.readline().split())
    graph = [[0]*m for _ in range(n)]
    visited = copy.deepcopy(graph)

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

import sys
sys.setrecursionlimit(10000000)

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    graph = []
    for i in range(n):
        n_list = list(map(int, sys.stdin.readline().split()))
        graph.append(n_list)
    
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    result = [0]

    visited = [[0]*m for _ in range(n)]

    def dfs(x, y, cnt):
        for direct in range(4):
            n_x, n_y = dx[direct] + x, dy[direct] + y
            if (n_x < 0 or n_x >= n) or (n_y < 0 or n_y >= m) or visited[n_x][n_y] == 1 or graph[n_x][n_y] == 0:
                continue
            visited[n_x][n_y] = 1
            cnt += dfs(n_x, n_y, 1)
        
        return cnt
    
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and graph[i][j] == 1:
                visited[i][j] = 1
                result.append(dfs(i, j, 1))
    
    print(len(result) - 1)
    print(max(result))