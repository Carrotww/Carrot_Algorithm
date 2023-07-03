# https://www.acmicpc.net/problem/14500

def dfs(r, c, cnt, total):
    global max_val

    if cnt == 3:
        max_val = max(max_val, total)
        return
    if max_val >= (max_input * (3-cnt) + total):
        return
    for i in range(4):
        n_r, n_c = dr[i]+r, dc[i]+c
        if check(n_r, n_c):
            if cnt == 1:
                visited[n_r][n_c] = 1
                dfs(r, c, cnt+1, total+graph[n_r][n_c])
                visited[n_r][n_c] = 0
            visited[n_r][n_c] = 1
            dfs(n_r, n_c, cnt+1, total+graph[n_r][n_c])
            visited[n_r][n_c] = 0


def check(r, c):
    if (r < 0 or r >= n) or (c < 0 or c >= m) or (visited[r][c] == 1):
        return False
    return True


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split())
    graph = []
    max_input = 0
    for _ in range(n):
        temp = list(map(int, input().split()))
        max_input = max(max(temp), max_input)
        graph.append(temp)

    dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
    max_val = 0
    visited = [[0 for _ in range(m)] for _ in range(n)]

    for r in range(n):
        for c in range(m):
            visited[r][c] = 1
            dfs(r, c, 0, graph[r][c])
            visited[r][c] = 0

    print(max_val)
