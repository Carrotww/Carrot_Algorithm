# https://www.acmicpc.net/problem/2146

def checkisland(r, c, cnt):
    queue = deque([(r, c)])
    island_cnt[r][c] = cnt
    while queue:
        cur_r, cur_c = queue.popleft()
        for d in range(4):
            n_r, n_c = cur_r + dr[d], cur_c + dc[d]
            if (n_r < 0 or n_r >= n) or (n_c < 0 or n_c >= n):
                continue
            if graph[n_r][n_c] == 1 and island_cnt[n_r][n_c] == 0:
                island_cnt[n_r][n_c] = cnt
                queue.append((n_r, n_c))


def checkbridge(r, c, island_num):
    queue = deque([(r, c)])
    visited = [[0] * n for _ in range(n)]
    visited[r][c] = 1
    while queue:
        cur_r, cur_c = queue.popleft()
        for d in range(4):
            n_r, n_c = cur_r + dr[d], cur_c + dc[d]
            if (n_r < 0 or n_r >= n) or (n_c < 0 or n_c >= n):
                continue
            if graph[n_r][n_c] == 0 and visited[n_r][n_c] == 0:
                queue.append((n_r, n_c))
                visited[n_r][n_c] = visited[cur_r][cur_c] + 1
            elif graph[n_r][n_c] == 1 and island_cnt[n_r][n_c] != island_num:
                return visited[cur_r][cur_c]
    return float('inf')


if __name__ == "__main__":
    import sys
    from collections import deque
    input = sys.stdin.readline

    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]

    island_cnt = [[0] * n for _ in range(n)]
    cnt = 1
    for r in range(n):
        for c in range(n):
            if graph[r][c] == 1 and island_cnt[r][c] == 0:
                checkisland(r, c, cnt)
                cnt += 1

    result = float('inf')

    for r in range(n):
        for c in range(n):
            if graph[r][c] == 1:
                for d in range(4):
                    n_r, n_c = r + dr[d], c + dc[d]
                    if (n_r < 0 or n_r >= n) or (n_c < 0 or n_c >= n) or graph[n_r][n_c] == 1:
                        continue
                    need_bridge = checkbridge(n_r, n_c, island_cnt[r][c])
                    result = min(result, need_bridge)

    print(result)
