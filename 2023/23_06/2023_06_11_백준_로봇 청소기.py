# https://www.acmicpc.net/problem/14503

def solve():
    import sys
    from collections import deque
    
    n, m = map(int, sys.stdin.readline().split())
    r, c, d = map(int, sys.stdin.readline().split())

    # d -> 0 북, 1 동, 2 남, 3 서
    graph = []
    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().split())))
    visited = [[0]*m for _ in range(n)]
    queue = deque()
    direct = [[(0, -1, 3), (1, 0, 2), (0, 1, 1), (-1, 0, 0)], 
              [(-1, 0, 0), (0, -1, 3), (1, 0, 2), (0, 1, 1)],
              [(0, 1, 1), (-1, 0, 0), (0, -1, 3), (1, 0, 2)],
              [(1, 0, 2), (0, 1, 1), (-1, 0, 0), (0, -1, 3)]]
    back_direct = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    queue.append([r, c, d, 1])
    visited[r][c] = 1
    
    while queue:
        cur_r, cur_c, cur_d, cnt = queue.popleft()
        if visited[cur_r][cur_c] == 0:
            visited[cur_r][cur_c] = 1
            cnt += 1
        is_go = False
        for rr, cc, dd in direct[cur_d]:
            n_r, n_c = cur_r+rr, cur_c+cc
            n_d = dd
            if (n_r >= 0 and n_r < n) and (n_c >= 0 and n_c < m) and graph[n_r][n_c] == 0 and visited[n_r][n_c] == 0:
                is_go = True
                break
        if is_go:
            queue.append([n_r, n_c, n_d, cnt])
        else:
            rr, cc = back_direct[cur_d]
            n_r, n_c = cur_r+rr, cur_c+cc
            if (n_r < 0 or n_r >= n) or (n_c < 0 or n_c >= m) or graph[n_r][n_c] == 1:
                print(cnt)
                return
            queue.append([n_r, n_c, cur_d, cnt])

if __name__ == "__main__":
    solve()