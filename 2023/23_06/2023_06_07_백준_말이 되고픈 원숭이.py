# https://www.acmicpc.net/problem/1600

def solve():
    import sys
    from collections import deque
    K = int(sys.stdin.readline())
    c, r = map(int, sys.stdin.readline().split())
    graph = []
    for _ in range(r):
        graph.append(list(map(int, sys.stdin.readline().split())))

    queue = deque()
    queue.append([0, 0, 0, 0])
    visited = [[[False] * (K + 1) for _ in range(c)] for _ in range(r)]
    dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
    hr, hc = [2, 2, -2, -2, 1, -1, 1, -1], [-1, 1, -1, 1, 2, 2, -2, -2]

    while queue:
        cur_r, cur_c, cnt, jump = queue.popleft()
        if cur_r == r - 1 and cur_c == c - 1:
            print(cnt)
            return
        for direct in range(4):
            n_r, n_c = cur_r + dr[direct], cur_c + dc[direct]
            if (n_r < 0 or n_r >= r) or (n_c < 0 or n_c >= c) or graph[n_r][n_c] == 1 or visited[n_r][n_c][jump]:
                continue
            visited[n_r][n_c][jump] = True
            queue.append([n_r, n_c, cnt+1, jump])
        if jump < K:
            for direct in range(8):
                n_r, n_c = cur_r + hr[direct], cur_c + hc[direct]
                if (n_r < 0 or n_r >= r) or (n_c < 0 or n_c >= c) or graph[n_r][n_c] == 1 or visited[n_r][n_c][jump+1]:
                    continue
                visited[n_r][n_c][jump+1] = True
                queue.append([n_r, n_c, cnt+1, jump+1])

    print(-1)
    return

if __name__ == "__main__":
    solve()