# https://www.acmicpc.net/problem/6087

def draw(x1, y1, x2, y2):
    y1, y2 = row - y1, row - y2

    for r in range(y2, y1):
        for c in range(x1, x2):
            graph[r][c] = 1


def bfs(r, c):
    queue = deque([(r, c)])
    graph[r][c] = 1
    total_size = 1
    while queue:
        cur_r, cur_c = queue.popleft()
        for d in range(4):
            n_r, n_c = cur_r + dr[d], cur_c + dc[d]
            if (n_r < 0 or n_r >= row) or (n_c < 0 or n_c >= col) or graph[n_r][n_c] == 1:
                continue
            total_size += 1
            graph[n_r][n_c] = 1
            queue.append((n_r, n_c))
    return total_size

if __name__ == "__main__":
    import sys
    from collections import deque

    input = sys.stdin.readline

    row, col, k = map(int, input().split())
    graph = [[0] * col for _ in range(row)]
    dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]

    for _ in range(k):
        x1, y1, x2, y2 = map(int, input().split())
        draw(x1, y1, x2, y2)
    
    size = []
    for r in range(row):
        for c in range(col):
            if graph[r][c] == 0:
                size.append(bfs(r, c))
    
    size.sort()
    print(len(size))
    print(' '.join([str(x) for x in size]))