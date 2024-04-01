
def dfs(cur_r, cur_c, cur_direct):
    if (cur_r, cur_c) == (n-1, n-1):
        return 1

    result = 0

    if cur_direct == 0 or cur_direct == 2:
        if cur_c + 1 < n and graph[cur_r][cur_c + 1] == 0:
            result += dfs(cur_r, cur_c+1, 0)

    if cur_direct == 1 or cur_direct == 2:
        if cur_r + 1 < n and graph[cur_r + 1][cur_c] == 0:
            result += dfs(cur_r+1, cur_c, 1)

    if cur_r + 1 < n and cur_c + 1 < n and graph[cur_r + 1][cur_c] == 0 and graph[cur_r][cur_c + 1] == 0 and graph[cur_r + 1][cur_c + 1] == 0:
        result += dfs(cur_r+1, cur_c+1, 2)

    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    result = 0
    if graph[n-1][n-1] == 0:
        result = dfs(0, 1, 0)
    print(result)

