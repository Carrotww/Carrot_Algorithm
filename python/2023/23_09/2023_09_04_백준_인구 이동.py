# https://www.acmicpc.net/problem/16234

def check_change():
    queue = deque()
    visited = [[-1] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            for direct in range(4):
                n_r, n_c = r+dr[direct], c+dc[direct]
                if (n_r < 0 or n_r >= N) or (n_c < 0 or n_c >= N):
                    continue
                if L <= abs(graph[n_r][n_c] - graph[r][c]) <= R and visited[n_r][n_c] == -1:
                    queue.append([r, c])
                    visited[r][c] = 1
                    visited[n_r][n_c] = 1
                    break
    if queue:
        return queue
    else:
        return False


def bfs(total):
    visited = [[-1] * N for _ in range(N)]
    while total:
        queue = deque()
        cur_r, cur_c = total.popleft()
        if visited[cur_r][cur_c] == 1:
            continue

        union = [(cur_r, cur_c)]
        queue.append([cur_r, cur_c])
        visited[cur_r][cur_c] = 1

        cnt_sum = graph[cur_r][cur_c]

        while queue:
            cur_r, cur_c = queue.popleft()
            for direct in range(4):
                n_r, n_c = cur_r+dr[direct], cur_c+dc[direct]
                if (n_r < 0 or n_r >= N) or (n_c < 0 or n_c >= N) or visited[n_r][n_c] == 1:
                    continue
                if L <= abs(graph[n_r][n_c] - graph[cur_r][cur_c]) <= R:
                    visited[n_r][n_c] = 1
                    queue.append([n_r, n_c])
                    union.append((n_r, n_c))
                    cnt_sum += graph[n_r][n_c]

        val = cnt_sum // len(union)
        for r, c in union:
            graph[r][c] = val


if __name__ == "__main__":
    import sys
    from collections import deque
    input = sys.stdin.readline

    N, L, R = map(int, input().split())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))

    result = 0
    dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]

    while 1:
        check = check_change()
        if check:
            bfs(check)
            result += 1
        else:
            break
    print(result)
