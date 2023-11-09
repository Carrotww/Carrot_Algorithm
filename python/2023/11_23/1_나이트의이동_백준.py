# https://www.acmicpc.net/problem/7562

def bfs(r, c):
    from collections import deque
    if r == target_r and c == target_c:
        return 0
    queue = deque([(r, c)])
    visited = [[-1] * n for _ in range(n)]
    visited[r][c] = 0
    move = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
    while queue:
        cur_r, cur_c = queue.popleft()
        for m in move:
            n_r, n_c = cur_r + m[0], cur_c + m[1]
            if (n_r < 0 or n_r >= n) or (n_c < 0 or n_c >= n) or visited[n_r][n_c] != -1:
                continue
            if target_r == n_r and target_c == n_c:
                return visited[cur_r][cur_c] + 1
            queue.append((n_r, n_c))
            visited[n_r][n_c] = visited[cur_r][cur_c] + 1

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    t = int(input())
    for _ in range(t):
        n = int(input())
        cur_r, cur_c = map(int, input().split())
        target_r, target_c = map(int, input().split())

        print(bfs(cur_r, cur_c))
