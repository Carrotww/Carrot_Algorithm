# https://www.acmicpc.net/problem/1987

def dfs(cur_r, cur_c, cnt):
    global max_val
    max_val = max(max_val, cnt)

    for d in range(4):
        n_r, n_c = cur_r+dr[d], cur_c+dc[d]
        if (n_r < 0 or n_r >= r) or (n_c < 0 or n_c >= c):
            continue
        if graph[n_r][n_c] not in global_set:
            global_set.add(graph[n_r][n_c])
            dfs(n_r, n_c, cnt+1)
            global_set.remove(graph[n_r][n_c])


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    r, c = map(int, input().split())
    graph = []
    for _ in range(r):
        graph.append(list(input().rstrip()))

    dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
    global_set = set()
    global_set.add(graph[0][0])
    max_val = 0
    result = dfs(0, 0, 1)

    print(max_val)
