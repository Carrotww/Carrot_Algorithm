# https://www.acmicpc.net/problem/16930

def solve():
    import sys
    from collections import deque
    
    N, M, K = map(int, sys.stdin.readline().split())
    graph = []
    for _ in range(N):
        graph.append(list(sys.stdin.readline().strip()))
    
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1

    path = [[-1] * M for _ in range(N)]
    visited = [[-1] * M for _ in range(N)]
    queue = deque()
    queue.append([x1, y1])
    dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]

    while queue:
        cur_r, cur_c = queue.popleft()
        if cur_r == x2 and cur_c == y2:
            break
        for i in range(4):
            n_r, n_c = cur_r+dr[i], cur_c+dc[i]

if __name__ == "__main__":
    solve()