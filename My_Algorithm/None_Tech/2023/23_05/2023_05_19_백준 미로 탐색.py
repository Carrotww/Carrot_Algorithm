# https://www.acmicpc.net/problem/2178

def solve():
    import sys
    from collections import deque
    
    N, M = map(int, sys.stdin.readline().split())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, str(sys.stdin.readline().strip()))))
    
    queue = deque()
    queue.append([0, 0, 1])

    dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
    visited = [[0] * M for _ in range(N)]

    while queue:
        cur_r, cur_c, cnt = queue.popleft()
        if cur_r == (N - 1) and cur_c == (M - 1):
            print(cnt)
            return
        for i in range(4):
            n_r, n_c = dr[i]+cur_r, dc[i]+cur_c
            if (n_r < 0 or n_r >= N) or (n_c < 0 or n_c >= M) or (graph[n_r][n_c] == 0) or visited[n_r][n_c] == 1:
                continue
            queue.append([n_r, n_c, cnt+1])
            visited[n_r][n_c] = 1

if __name__ == "__main__":
    solve()