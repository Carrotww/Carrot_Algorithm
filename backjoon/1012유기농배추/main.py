
def bfs(r, c, cur_r, cur_c, visited, graph):
    from collections import deque

    queue = deque([(cur_r, cur_c)])
    dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
    visited[cur_r][cur_c] = 1

    while queue:
        cur_r, cur_c = queue.popleft()
        for d in range(4):
            n_r = cur_r + dr[d]
            n_c = cur_c + dc[d]

            if n_r < 0 or n_r >= r or n_c < 0 or n_c >= c:
                continue
            if graph[n_r][n_c] == 1 and not visited[n_r][n_c]:
                queue.append((n_r, n_c))
                visited[n_r][n_c] = 1

def solve():
    c, r, k = map(int, input().split())
    graph = [[0] * c for _ in range(r)]
    visited = [[0] * c for _ in range(r)]

    for _ in range(k):
        cur_c, cur_r = map(int, input().split())
        graph[cur_r][cur_c] = 1

    cnt = 0

    for i in range(r):
        for j in range(c):
            if not visited[i][j] and graph[i][j] == 1:
                bfs(r, c, i, j, visited, graph)
                cnt += 1

    result.append(cnt)

if __name__ == "__main__":
    import sys

    input = sys.stdin.readline

    t = int(input())
    result = []

    for _ in range(t):
        solve()

    print(' '.join(map(str, result)))

