import sys
from collections import deque

def solve(n):
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    visited = [[0] * n for _ in range(n)]
    visited[0][0] = graph[0][0]
    q = deque([[0, 0]])
    dr, dc = [1, 0, -1, 0], [0, 1, 0, -1]

    while q:
        cur_r, cur_c = q.popleft()
        for d in range(4):
            n_r = cur_r + dr[d]
            n_c = cur_c + dc[d]
            if (n_r < 0 or n_r >= n or n_c < 0 or n_c >= n):
                continue
            if (visited[n_r][n_c] == 0 or visited[n_r][n_c] > visited[cur_r][cur_c] + graph[n_r][n_c]):
                visited[n_r][n_c] = visited[cur_r][cur_c] + graph[n_r][n_c]
                q.append([n_r, n_c])

    result.append(visited[n-1][n-1])

if __name__ == "__main__":
    import sys

    input = sys.stdin.readline
    result = []

    while True:
        n = int(input())
        if n != 0:
            solve(n)
        else:
            break

    for i in range(len(result)):
        print(f"Problem {i+1} : {result[i]}")
