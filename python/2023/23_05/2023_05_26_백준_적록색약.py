# https://www.acmicpc.net/problem/10026

def solve():
    import sys
    from collections import deque

    N = int(sys.stdin.readline())
    graph = []
    for _ in range(N):
        graph.append(list(sys.stdin.readline().strip()))
    mix_graph = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if graph[r][c] == 'R':
                mix_graph[r][c] = 'G'
            else:
                mix_graph[r][c] = graph[r][c]
    
    color_man, not_color_man = 0, 0
    visited_color = [[0]*N for _ in range(N)]
    visited_not_color = [[0]*N for _ in range(N)]
    dr, dc = [1, -1, 0, 0], [0, 0, -1, 1]

    for r in range(N):
        for c in range(N):
            if visited_color[r][c] == 0:
                visited_color[r][c] = 1
                queue = deque()
                color = graph[r][c]
                queue.append([r, c, color])
                while queue:
                    cur_r, cur_c, cur_color = queue.popleft()
                    for di in range(4):
                        n_r, n_c = cur_r+dr[di], cur_c+dc[di]
                        if (n_r < 0 or n_r >= N) or (n_c < 0 or n_c >= N) or visited_color[n_r][n_c] == 1 or graph[n_r][n_c] != cur_color:
                            continue
                        queue.append([n_r, n_c, cur_color])
                        visited_color[n_r][n_c] = 1
                color_man += 1
    
    for r in range(N):
        for c in range(N):
            if visited_not_color[r][c] == 0:
                visited_not_color[r][c] = 1
                queue = deque()
                color = mix_graph[r][c]
                queue.append([r, c, color])
                while queue:
                    cur_r, cur_c, cur_color = queue.popleft()
                    for di in range(4):
                        n_r, n_c = cur_r+dr[di], cur_c+dc[di]
                        if (n_r < 0 or n_r >= N) or (n_c < 0 or n_c >= N) or visited_not_color[n_r][n_c] == 1 or mix_graph[n_r][n_c] != cur_color:
                            continue
                        queue.append([n_r, n_c, cur_color])
                        visited_not_color[n_r][n_c] = 1
                not_color_man += 1
    
    print(f'{color_man} {not_color_man}')

if __name__ == "__main__":
    solve()