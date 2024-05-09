# https://www.acmicpc.net/problem/3187

def bfs(input_r, input_c):
    from collections import deque

    cur_v, cur_k = 0, 0
    queue = deque([[input_r, input_c]])
    dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
    if graph[input_r][input_c] == 'v':
        cur_v += 1
    elif graph[input_r][input_c] == 'k':
        cur_k += 1
    visited[input_r][input_c] = 1

    while queue:
        cur_r, cur_c = queue.popleft()
        for d in range(4):
            n_r, n_c = dr[d] + cur_r, dc[d] + cur_c
            if (n_r < 0 or n_r >= r) or (n_c < 0 or n_c >= c) or graph[n_r][n_c] == '#':
                continue
            if visited[n_r][n_c] == 1:
                continue
            if graph[n_r][n_c] == 'v':
                cur_v += 1
            elif graph[n_r][n_c] == 'k':
                cur_k += 1
            visited[n_r][n_c] = 1
            queue.append([n_r, n_c])
    if cur_v >= cur_k:
        cur_k = 0
    else:
        cur_v = 0
    return cur_v, cur_k

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    r, c = map(int, input().split())
    result_v, result_k = 0, 0

    graph = []
    for _ in range(r):
        graph.append(list(input().strip()))

    visited = [[0] * c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if visited[i][j] == 1 or graph[i][j] == '#':
                continue
            v, k = bfs(i, j)
            result_v += v
            result_k += k

    print(result_k, result_v)

