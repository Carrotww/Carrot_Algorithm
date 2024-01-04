# https://www.acmicpc.net/problem/5427

def bfs(r, c):
    from collections import deque

    fire_queue, escape_queue = deque(), deque()
    fire_visited = [[0] * c for _ in range(r)]
    escape_visited = [[0] * c for _ in range(r)]

    dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]

    graph = []
    for _ in range(r):
        graph.append(list(input().rstrip()))

    for i in range(r):
        for j in range(c):
            if graph[i][j] == "@":
                escape_queue.append((i, j))
            elif graph[i][j] == "*":
                fire_queue.append((i, j))

    while fire_queue:
        cur_r, cur_c = fire_queue.popleft()
        for d in range(4):
            n_r, n_c = cur_r + dr[d], cur_c + dc[d]
            if (n_r < 0 or n_r >= r) or (n_c < 0 or n_c >= c):
                continue
            if (graph[n_r][n_c] == "." or graph[n_r][n_c] == "@") and fire_visited[n_r][n_c] == 0:
                fire_visited[n_r][n_c] = fire_visited[cur_r][cur_c] + 1
                fire_queue.append((n_r, n_c))

    while escape_queue:
        cur_r, cur_c = escape_queue.popleft()
        for d in range(4):
            n_r, n_c = cur_r + dr[d], cur_c + dc[d]
            if (n_r < 0 or n_r >= r) or (n_c < 0 or n_c >= c):
                return escape_visited[cur_r][cur_c] + 1
            if graph[n_r][n_c] == "." and escape_visited[n_r][n_c] == 0 and (fire_visited[n_r][n_c] == 0 or escape_visited[cur_r][cur_c] + 1 < fire_visited[n_r][n_c]):
                escape_visited[n_r][n_c] = escape_visited[cur_r][cur_c] + 1
                escape_queue.append((n_r, n_c))

    return -1


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        c, r = map(int, input().split())
        result = bfs(r, c)
        if result == -1:
            print("IMPOSSIBLE")
        else:
            print(result)

