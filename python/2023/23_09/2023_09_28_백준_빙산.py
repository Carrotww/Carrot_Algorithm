# https://www.acmicpc.net/problem/2573

def check():
    cnt = 0
    visited = [[False] * m for _ in range(n)]

    for r in range(n):
        for c in range(m):
            if graph[r][c] > 0 and visited[r][c] == False:
                cnt += 1
                if cnt > 0:
                    return cnt
                queue = deque([(r, c)])
                visited[r][c] = True
                while queue:
                    cur_r, cur_c = queue.popleft()
                    for d in range(4):
                        n_r, n_c = cur_r + dr[d], cur_c + dc[d]
                        if (n_r < 0 or n_r >= n) or (n_c < 0 or n_c >= m):
                            continue
                        if graph[n_r][n_c] > 0 and visited[n_r][n_c] == False:
                            visited[n_r][n_c] = True
                            queue.append((n_r, n_c))

    return cnt


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    from collections import deque

    n, m = map(int, input().split())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
    queue = [(0, 0), (n-1, m-1)]

    result = 0
    while 1:
        melt = []
        for r in range(n):
            for c in range(m):
                if graph[r][c] > 0:
                    sea_cnt = 0
                    for d in range(4):
                        n_r, n_c = r+dr[d], c+dc[d]
                        if (n_r < 0 or n_r >= n) or (n_c < 0 or n_c >= m):
                            continue
                        if graph[n_r][n_c] == 0:
                            sea_cnt += 1
                    if sea_cnt > 0:
                        melt.append((r, c, sea_cnt))
        for r, c, cnt in melt:
            graph[r][c] = max(graph[r][c] - cnt, 0)

        result += 1
        cnt = check()
        if cnt > 1:
            break
        elif cnt == 0:
            result = 0
            break

    print(result)
