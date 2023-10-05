# https://www.acmicpc.net/problem/4963

def bfs(row, col):
    dr, dc = [1, -1, 0, 0, 1, 1, -1, -1], [0, 0, 1, -1, 1, -1, 1, -1]
    queue = deque([(row, col)])
    visited[row][col] = True

    while queue:
        cur_r, cur_c = queue.popleft()
        for d in range(8):
            n_r, n_c = cur_r + dr[d], cur_c + dc[d]
            if (n_r < 0 or n_r >= r) or (n_c < 0 or n_c >= c):
                continue
            if graph[n_r][n_c] == 1 and visited[n_r][n_c] == False:
                queue.append((n_r, n_c))
                visited[n_r][n_c] = True

if __name__ == "__main__":
    import sys
    from collections import deque

    input = sys.stdin.readline
    
    while 1:
        c, r = map(int, input().split())
        if c == 0 and r == 0:
            break
        graph = []
        for _ in range(r):
            graph.append(list(map(int, input().split())))
        
        visited = [[False] * c for _ in range(r)]
        
        cnt = 0
        
        for i in range(r):
            for j in range(c):
                if visited[i][j] == False and graph[i][j] == 1:
                    cnt += 1
                    bfs(i, j)
        
        print(cnt)