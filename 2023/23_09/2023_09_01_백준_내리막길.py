# https://www.acmicpc.net/problem/1520

# def dfs(r, c):
#     global result

#     if r == R - 1 and c == C - 1:
#         result += 1
#         return
#     for direct in range(4):
#         n_r, n_c = r+dr[direct], c+dc[direct]
#         if (n_r < 0 or n_r >= R) or (n_c < 0 or n_c >= C) or visited[n_r][n_c] == True \
#             or graph[n_r][n_c] >= graph[r][c]:
#             continue
#         visited[n_r][n_c] = True
#         dfs(n_r, n_c)
#         visited[n_r][n_c] = False

# if __name__ == "__main__":
#     import sys
#     input = sys.stdin.readline

#     R, C = map(int, input().split())
#     result = 0
    
#     graph = []
#     for _ in range(R):
#         graph.append(list(map(int, input().split())))
    
#     visited = [[False] * C for _ in range(R)]
#     dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]

#     dfs(0, 0)
#     print(result)


def dfs(r, c):
    if r == R - 1 and c == C - 1:
        return 1
    if dp[r][c] != -1:
        return dp[r][c]
    
    dp[r][c] = 0
    
    for direct in range(4):
        n_r, n_c = r + dr[direct], c + dc[direct]
        if (n_r < 0 or n_r >= R) or (n_c < 0 or n_c >= C) \
            or graph[n_r][n_c] >= graph[r][c]:
            continue
        dp[r][c] += dfs(n_r, n_c)
    
    return dp[r][c]

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    R, C = map(int, input().split())
    result = 0
    
    graph = []
    for _ in range(R):
        graph.append(list(map(int, input().split())))
    dp = [[-1] * C for _ in range(R)]
    
    dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
    dfs(0, 0)
    print(dp[0][0])