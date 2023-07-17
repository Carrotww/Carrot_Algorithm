# https://www.acmicpc.net/problem/2667

def solve():
    import sys
    from collections import deque
    
    N = int(sys.stdin.readline())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, sys.stdin.readline().strip())))
    
    visited = [[-1] * N for _ in range(N)]
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    total_cnt = 0
    result = []

    for row in range(N):
        for col in range(N):
            if visited[row][col] == -1 and graph[row][col] == 1:
                queue = deque()
                queue.append([row, col])
                visited[row][col] = 1
                cnt = 0
                while queue:
                    cur_r, cur_c = queue.popleft()
                    cnt += 1
                    for i in range(4):
                        n_r, n_c = dx[i]+cur_r, dy[i]+cur_c
                        if (n_r < 0 or n_r >= N) or (n_c < 0 or n_c >= N) or visited[n_r][n_c] != -1 or graph[n_r][n_c] == 0:
                            continue
                        visited[n_r][n_c] = 1
                        queue.append([n_r, n_c])
                result.append(cnt)
                total_cnt += 1
    
    print(total_cnt)
    for i in sorted(result):
        print(i)

if __name__ == "__main__":
    solve()