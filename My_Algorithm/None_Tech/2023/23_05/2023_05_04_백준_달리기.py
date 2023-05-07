# https://www.acmicpc.net/problem/16930

def solve2():
    import sys
    from collections import deque
    
    N, M, K = map(int, sys.stdin.readline().split())
    graph = []
    for _ in range(N):
        graph.append(list(sys.stdin.readline().strip()))
    
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1

    path = [[False] * M for _ in range(N)]
    visited = [[-1] * M for _ in range(N)]
    visited[x1][y1] = 1
    queue = deque()
    queue.append([x1, y1, 0])
    dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
    result_cnt = 0

    while queue:
        cur_r, cur_c, cnt = queue.popleft()
        if cur_r == x2 and cur_c == y2:
            result_cnt = cnt
            break
        for i in range(4):
            n_r, n_c = cur_r+dr[i], cur_c+dc[i]
            if (n_r < 0 or n_r >= N) or (n_c < 0 or n_c >= M) or graph[n_r][n_c] != '.' or visited[n_r][n_c] != -1:
                continue
            visited[n_r][n_c] = 1
            path[n_r][n_c] = [cur_r, cur_c]
            queue.append([n_r, n_c, cnt+1])
    
    if result_cnt == 0:
        print(-1)
    else:
        path_check = [[x2, y2]]
        while (x1 != x2) or (y1 != y2):
            t1, t2 = path[x2][y2]
            path_check.append([t1, t2])
            x2, y2 = t1, t2
        
        cnt = 0
        k_cnt = 0
        pre_direct = None

        for i in range(len(path_check) - 1):
            x1, y1 = path_check[i]
            x2, y2 = path_check[i+1]

            if x1 == x2:
                direct = "W"
            elif y1 == y2:
                direct = "H"
            
            if pre_direct and pre_direct == direct and cnt < K:
                cnt += 1
            else:
                pre_direct = direct
                cnt = 1
                k_cnt += 1
        
        print(k_cnt)

def solve():
    import sys
    from collections import deque

    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    N, M, K = map(int, sys.stdin.readline().split())
    graph = []
    for _ in range(N):
        graph.append(list(sys.stdin.readline().strip()))
    
    x1, y1, x2, y2 = map(lambda x:int(x)-1, sys.stdin.readline().split())
    visited = [[float('inf')] * M for _ in range(N)]

    queue = deque()
    queue.append([x1, y1])
    visited[x1][y1] = 0
    
    while queue:
        cur_r, cur_c = queue.popleft()
        for i in range(4):
            n_r, n_c = cur_r+dx[i], cur_c+dy[i]
            cnt = 1
            while cnt <= K and (0 <= n_r < N) and (0 <= n_c < M) and graph[n_r][n_c] != '#' and visited[n_r][n_c] > visited[cur_r][cur_c]:
                if visited[n_r][n_c] == float('inf'):
                    queue.append([n_r, n_c])
                    visited[n_r][n_c] = visited[cur_r][cur_c] + 1
                n_r += dx[i]
                n_c += dy[i]
                cnt += 1
    
    if visited[x2][y2] == float('inf'):
        print(-1)
    else:
        print(visited[x2][y2])

if __name__ == "__main__":
    solve()