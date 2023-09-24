# https://www.acmicpc.net/problem/17836

if __name__ == "__main__":
    import sys
    from collections import deque

    input = sys.stdin.readline

    row, col, T = map(int, input().split())

    graph = []
    visited = [[[False] * 2 for _ in range(col)] for _ in range(row)]
    for _ in range(row):
        graph.append(list(map(int, input().split())))

    dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]

    queue = deque([(0, 0, 0, 0)])
    result = 0

    while queue:
        cur_r, cur_c, time, sword = queue.popleft()
        if graph[cur_r][cur_c] == 2:
            sword = 1
        if time > T:
            break
        if (cur_r, cur_c) == (row-1, col-1):
            result = time
            break
        for d in range(4):
            n_r, n_c = cur_r+dr[d], cur_c+dc[d]
            if (n_r < 0 or n_r >= row) or (n_c < 0 or n_c >= col) or visited[n_r][n_c][sword]:
                continue

            if sword == 1 or graph[n_r][n_c] != 1:
                queue.append((n_r, n_c, time+1, sword))
                visited[n_r][n_c][sword] = True

    if result == 0:
        print("Fail")
    else:
        print(result)
