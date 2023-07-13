# https://www.acmicpc.net/problem/14940

def bfs():
    from collections import deque
    queue = deque()
    queue.append((start_r, start_c, 0))

    while queue:
        cur_r, cur_c, cur_time = queue.popleft()

        for i in range(4):
            n_r, n_c = dr[i]+cur_r, dc[i]+cur_c
            if (n_r < 0 or n_r >= n) or (n_c < 0 or n_c >= m) or graph[n_r][n_c] == 0:
                continue
            if visited[n_r][n_c] > cur_time + 1:
                visited[n_r][n_c] = cur_time + 1
                queue.append((n_r, n_c, cur_time + 1))


if __name__ == "__main__":
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    graph = []
    start_r, start_c = 0, 0

    for i in range(n):
        line = list(map(int, input().split()))
        if 2 in line:
            start_r = i
            start_c = line.index(2)
        graph.append(line)

    visited = [[float('inf')]*m for _ in range(n)]
    visited[start_r][start_c] = 0

    dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]

    bfs()
    for i in range(n):
        for j in range(m):
            if visited[i][j] == float('inf') and graph[i][j] == 0:
                visited[i][j] = 0
            elif visited[i][j] == float('inf'):
                visited[i][j] = -1
    for i in range(n):
        print(' '.join([str(x) for x in visited[i]]))
