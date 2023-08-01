# https://www.acmicpc.net/problem/7569

def bfs():
    from collections import deque
    queue = deque(start_list)
    dr, dc = [1, 0, -1, 0], [0, 1, 0, -1]
    global need_change_tomato
    global max_day

    while queue:
        cur_h, cur_r, cur_c, cur_day = queue.popleft()
        for direct in range(4):
            n_h, n_r, n_c = cur_h, dr[direct]+cur_r, dc[direct]+cur_c
            if (n_r < 0 or n_r >= r) or (n_c < 0 or n_c >= c):
                continue
            if graph[n_h][n_r][n_c] == 0:
                graph[n_h][n_r][n_c] = 1
                queue.append((n_h, n_r, n_c, cur_day + 1))
                need_change_tomato -= 1
                max_day = max(cur_day + 1, max_day)
        for i in (-1, 1):
            n_h, n_r, n_c = cur_h+i, cur_r, cur_c
            if (n_h < 0 or n_h >= h):
                continue
            if graph[n_h][n_r][n_c] == 0:
                graph[n_h][n_r][n_c] = 1
                queue.append((n_h, n_r, n_c, cur_day + 1))
                need_change_tomato -= 1
                max_day = max(cur_day + 1, max_day)


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    c, r, h = map(int, input().split())
    start_list = []
    max_day = 0

    graph = [0] * h
    need_change_tomato = 0
    for i in range(h):
        graph[i] = [[0] * c for _ in range(r)]
        for j in range(r):
            graph[i][j] = list(map(int, input().split()))
            for z in range(c):
                if graph[i][j][z] == 1:
                    start_list.append((i, j, z, 0))
                elif graph[i][j][z] == 0:
                    need_change_tomato += 1

    bfs()

    if need_change_tomato == 0:
        print(max_day)
    else:
        print(-1)
