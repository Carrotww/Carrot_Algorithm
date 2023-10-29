# https://www.acmicpc.net/problem/7576

def solve():
    import sys
    from collections import deque

    # N - row, M - col
    M, N = map(int, sys.stdin.readline().split())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, sys.stdin.readline().split())))
    
    dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
    queue = deque()

    all_clean = True
    for r in range(N):
        for c in range(M):
            if graph[r][c] == 0:
                all_clean = False
            elif graph[r][c] == 1:
                queue.append([r, c])
    if all_clean:
        print(0)
        return
    
    result = 0
    while queue:
        cur_r, cur_c = queue.popleft()
        for i in range(4):
            n_r, n_c = dr[i]+cur_r, dc[i]+cur_c
            if (n_r < 0 or n_r >= N) or (n_c < 0 or n_c >= M) or (graph[n_r][n_c] == -1 or graph[n_r][n_c] != 0):
                continue
            graph[n_r][n_c] = graph[cur_r][cur_c] + 1
            result = max(result, graph[n_r][n_c])
            queue.append([n_r, n_c])
    
    for r in range(N):
        if 0 in graph[r]:
            print(-1)
            return
            
    print(result - 1)

if __name__ == "__main__":
    solve()