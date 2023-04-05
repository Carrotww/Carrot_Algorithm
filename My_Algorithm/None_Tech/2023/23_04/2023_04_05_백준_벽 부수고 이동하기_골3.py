# https://www.acmicpc.net/problem/2206

if __name__ == "__main__":
    import sys
    from collections import deque

    n, m = map(int, sys.stdin.readline().split())
    result = -1
    visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
    graph = []
    
    for _ in range(n):
        row_graph = list(map(int, sys.stdin.readline().strip()))
        graph.append(row_graph)

    queue = deque()
    queue.append([0, 0, 1, 1])

    dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]

    while queue:
        cur_row, cur_col, break_chance, cnt = queue.popleft()
        if cur_row == n-1 and cur_col == m-1:
            result = cnt
            break
        
        for i in range(4):
            n_row, n_col = dx[i]+cur_row, dy[i]+cur_col
            if (n_row < 0 or n_row >= n) or (n_col < 0 or n_col >= m):
                continue
            if break_chance == 1 and graph[n_row][n_col] == 1:
                visited[n_row][n_col][1] = 1
                queue.append([n_row, n_col, break_chance-1, cnt+1])
            elif graph[n_row][n_col] == 0 and visited[n_row][n_col][break_chance] == 0:
                visited[n_row][n_col][break_chance] = 1
                queue.append([n_row, n_col, break_chance, cnt+1])
    
    print(result)