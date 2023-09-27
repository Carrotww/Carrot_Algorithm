# https://www.acmicpc.net/problem/2638

def check_inside():
    queue = deque([(0, 0), (0, col-1), (row-1, 0), (row-1, col-1)])
    out_side = set()
    visited = [[False] * col for _ in range(row)]
    for q in queue:
        visited[q[0]][q[1]] = True
    
    while queue:
        cur_r, cur_c = queue.popleft()
        out_side.add((cur_r, cur_c))
        for d in range(4):
            n_r, n_c = cur_r + dr[d], cur_c + dc[d]
            if (n_r < 0 or n_r >= row) or (n_c < 0 or n_c >= col) or graph[n_r][n_c] == 1 \
                or visited[n_r][n_c] == True:
                continue
            queue.append((n_r, n_c))
            visited[n_r][n_c] = True
    return out_side

if __name__ == "__main__":
    import sys
    from collections import deque
    
    input = sys.stdin.readline

    row, col = map(int, input().split())
    graph = []
    for _ in range(row):
        graph.append(list(map(int, input().split())))

    dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
    result = 0

    while 1:
        cheez = []
        outside_zero = check_inside()

        for r in range(row):
            for c in range(col):
                if graph[r][c] == 1:
                    cnt = 0
                    for d in range(4):
                        n_r, n_c = r + dr[d], c + dc[d]
                        if (n_r < 0 or n_r >= row) or (n_c < 0 or n_c >= col):
                            continue
                        if graph[n_r][n_c] == 0 and (n_r, n_c) in outside_zero:
                            cnt += 1
                    if cnt >= 2:
                        cheez.append((r, c))

        if cheez:
            result += 1
            for r, c in cheez:
                graph[r][c] = 0
        else:
            break
    print(result)
