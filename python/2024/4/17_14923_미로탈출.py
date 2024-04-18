# https://www.acmicpc.net/problem/14923

if __name__ == "__main__":
    import sys
    from collections import deque
    input = sys.stdin.readline

    r, c = map(int, input().split())
    start_r, start_c = map(int, input().split())
    target_r, target_c = map(int, input().split())

    graph = []
    for _ in range(r):
        graph.append(list(map(int, input().split())))

    visited = [[[0]*2 for _ in range(c)] for _ in range(r)]
    visited[start_r-1][start_c-1][0] = 1
    dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
    result = float('inf')

    queue = deque([(start_r-1, start_c-1, 0, 0)])
    while queue:
        cur_r, cur_c, is_broke, cnt = queue.popleft()
        if (cur_r, cur_c) == (target_r-1, target_c-1):
            result = cnt
            break
        for d in range(4):
            n_r, n_c = dr[d]+cur_r, dc[d]+cur_c
            if (n_r < 0 or n_r >= r) or (n_c < 0 or n_c >= c):
                continue
            if visited[n_r][n_c][is_broke] == 1:
                continue
            if graph[n_r][n_c] == 1 and not is_broke:
                queue.append((n_r, n_c, 1, cnt+1))
                visited[n_r][n_c][1] = 1
            elif graph[n_r][n_c] == 0:
                queue.append((n_r, n_c, is_broke, cnt+1))
                visited[n_r][n_c][is_broke] = 1
    if result == float('inf'):
        print(-1)
    else:
        print(result)

