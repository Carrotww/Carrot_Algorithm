# https://www.acmicpc.net/problem/1012

def dfs(col, row):
    dc, dr = [0, 0, -1, 1], [1, -1, 0, 0]
    for direct in range(4):
        n_col, n_row = col+dc[direct], row+dr[direct]
        if (n_col < 0 or n_col >= n) or (n_row < 0 or n_row >= m) or visited[n_col][n_row] == 1 or graph[n_col][n_row] == 0:
            continue
        visited[n_col][n_row] = 1
        dfs(n_col, n_row)

if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(10000000)
    
    N = int(sys.stdin.readline())
    result = []

    for _ in range(N):
        m, n, cabbage_cnt = map(int, sys.stdin.readline().split())
        graph = [[0]*m for _ in range(n)]
        visited = [[0]*m for _ in range(n)]
        cnt = 0
        
        for _ in range(cabbage_cnt):
            x, y = map(int, sys.stdin.readline().split())
            graph[y][x] = 1
        
        for col in range(n):
            for row in range(m):
                if visited[col][row] == 0 and graph[col][row] == 1:
                    visited[col][row] = 1
                    dfs(col, row)
                    cnt += 1
        
        result.append(cnt)
        
    for i in result:
        print(i)