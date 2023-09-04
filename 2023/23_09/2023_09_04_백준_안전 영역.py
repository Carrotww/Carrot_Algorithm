# https://www.acmicpc.net/problem/2468

def bfs(height):
    queue = deque()
    visited = [[-1] * N for _ in range(N)]
    dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
    safe_zone = 0

    for i in range(N):
        for j in range(N):
            if visited[i][j] != -1 or graph[i][j] <= height:
                continue
            visited[i][j] = 1
            queue.append([i, j])
            while queue:
                cur_r, cur_c = queue.popleft()
                for direct in range(4):
                    n_r, n_c = cur_r+dr[direct], cur_c+dc[direct]
                    if (n_r < 0 or n_r >= N) or (n_c < 0 or n_c >= N) \
                            or visited[n_r][n_c] == 1 or graph[n_r][n_c] <= height:
                        continue
                    visited[n_r][n_c] = 1
                    queue.append([n_r, n_c])
            safe_zone += 1
    return safe_zone


if __name__ == "__main__":
    import sys
    from collections import deque

    input = sys.stdin.readline

    result = 0
    max_height = 0

    N = int(input())
    graph = []
    for _ in range(N):
        temp = list(map(int, input().split()))
        max_height = max(max_height, max(temp))
        graph.append(temp)

    for h in range(max_height):
        result = max(result, bfs(h))

    print(result)
