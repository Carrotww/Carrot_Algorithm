# https://www.acmicpc.net/problem/14442

if __name__ == "__main__":
    import sys
    from collections import deque
    
    row, col, k = map(int, sys.stdin.readline().split())
    graph = []
    visited = [[[0]*(k+1) for _ in range(col)] for _ in range(row)]
    for _ in range(row):
        graph.append(list(map(int, sys.stdin.readline().strip())))
    
    queue = deque()
    queue.append([0, 0, 1, 0])
    result = 0

    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    while queue:
        cur_row, cur_col, cur_cnt, cur_k = queue.popleft()
        if cur_row == row - 1 and cur_col == col - 1:
            result = cur_cnt
            break
        for i in range(4):
            n_row, n_col = cur_row+dx[i], cur_col+dy[i]
            if (n_row < 0 or n_row >= row) or (n_col < 0 or n_col >= col):
                continue
            if graph[n_row][n_col] == 0 and visited[n_row][n_col][cur_k] == 0:
                visited[n_row][n_col][cur_k] = 1
                queue.append([n_row, n_col, cur_cnt+1, cur_k])
            if cur_k < k and graph[n_row][n_col] == 1 and visited[n_row][n_col][cur_k+1] == 0:
                visited[n_row][n_col][cur_k+1] = 1
                queue.append([n_row, n_col, cur_cnt+1, cur_k+1])
    
    if result == 0:
        print(-1)
    else:
        print(result)