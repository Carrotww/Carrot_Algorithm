# https://www.acmicpc.net/problem/1726

def solve():
    import sys
    from collections import deque

    row, col = map(int, sys.stdin.readline().split())
    # 0 -> 동, 1 -> 서, 2 -> 남, 3 -> 북
    dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
    change_direct = [[2, 3], [2, 3], [0, 1], [0, 1]]
    visited = [[[0]*4 for _ in range(col)] for _ in range(row)]
    graph = []
    
    for _ in range(row):
        graph.append(list(map(int, sys.stdin.readline().split())))
    
    start_r, start_c, start_direct = map(lambda x:int(x)-1, sys.stdin.readline().split())
    end_r, end_c, end_direct = map(lambda x:int(x)-1, sys.stdin.readline().split())
    visited[start_r][start_c][start_direct] = 1

    queue = deque()
    queue.append([start_r, start_c, start_direct, 0])

    while queue:
        cur_r, cur_c, cur_direct, cnt = queue.popleft()
        if cur_r == end_r and cur_c == end_c and cur_direct == end_direct:
            print(cnt)
            break

        for k in range(1, 4):
            n_d = cur_direct
            n_r, n_c = dr[n_d]*k + cur_r, dc[n_d]*k + cur_c
            if (n_r < 0 or n_r >= row) or (n_c < 0 or n_c >= col) or graph[n_r][n_c] == 1:
                break
            if visited[n_r][n_c][cur_direct] == 1:
                continue
            queue.append([n_r, n_c, n_d, cnt+1])
            visited[n_r][n_c][n_d] = 1
        
        for n_direct in change_direct[cur_direct]:
            if visited[cur_r][cur_c][n_direct] == 1:
                continue
            queue.append([cur_r, cur_c, n_direct, cnt+1])
            visited[cur_r][cur_c][n_direct] = 1

if __name__ == "__main__":
    solve()