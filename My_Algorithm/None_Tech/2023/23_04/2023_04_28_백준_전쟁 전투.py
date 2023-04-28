# https://www.acmicpc.net/problem/1303

def solve():
    import sys
    from collections import deque

    col, row = map(int, sys.stdin.readline().split())
    graph = []
    for _ in range(row):
        graph.append(list(sys.stdin.readline().strip()))
    
    visited_B = set()
    visited_W = set()

    result_B = []
    result_W = []

    dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]

    def dfs_B(r, c):
        queue = deque()
        queue.append((r, c))
        visited_B.add((r, c))
        cnt = 1

        while queue:
            cur_r, cur_c = queue.popleft()
            for di in range(4):
                n_r, n_c = cur_r+dr[di], cur_c+dc[di]
                if (n_r < 0 or n_r >= row) or (n_c < 0 or n_c >= col) or ((n_r, n_c) in visited_B) or (graph[n_r][n_c] != "B"):
                    continue
                visited_B.add((n_r, n_c))
                queue.append((n_r, n_c))
                cnt += 1
        
        result_B.append(cnt**2)
    
    def dfs_W(r, c):
        queue = deque()
        queue.append((r, c))
        visited_W.add((r, c))
        cnt = 1

        while queue:
            cur_r, cur_c = queue.popleft()
            for di in range(4):
                n_r, n_c = cur_r+dr[di], cur_c+dc[di]
                if (n_r < 0 or n_r >= row) or (n_c < 0 or n_c >= col) or ((n_r, n_c) in visited_W) or (graph[n_r][n_c] != "W"):
                    continue
                visited_W.add((n_r, n_c))
                queue.append((n_r, n_c))
                cnt += 1
        
        result_W.append(cnt**2)
    
    for r in range(row):
        for c in range(col):
            if (r, c) not in visited_B and graph[r][c] == "B":
                dfs_B(r, c)
            
            if (r, c) not in visited_W and graph[r][c] == "W":
                dfs_W(r, c)
    
    print(sum(result_W), end=' ')
    print(sum(result_B))

if __name__ == "__main__":
    solve()