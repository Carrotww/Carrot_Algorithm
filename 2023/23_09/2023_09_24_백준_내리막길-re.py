# https://www.acmicpc.net/problem/1520

def dfs(cur_r, cur_c):
    if cur_r == r - 1 and cur_c == c - 1:
        return 1

    if dp[cur_r][cur_c] != -1:
        return dp[cur_r][cur_c]

    dp[cur_r][cur_c] = 0

    for d in range(4):
        n_r, n_c = cur_r + dr[d], cur_c + dc[d]
        if (n_r < 0 or n_r >= r) or (n_c < 0 or n_c >= c):
            continue
        if graph[n_r][n_c] < graph[cur_r][cur_c]:
            dp[cur_r][cur_c] += dfs(n_r, n_c)

    return dp[cur_r][cur_c]


if __name__ == "__main__":
    import sys

    input = sys.stdin.readline

    r, c = map(int, input().split())
    graph = []
    for _ in range(r):
        graph.append(list(map(int, input().split())))

    dp = [[-1] * c for _ in range(r)]
    dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]

    dp[0][0] = dfs(0, 0)
    print(dp[0][0])
