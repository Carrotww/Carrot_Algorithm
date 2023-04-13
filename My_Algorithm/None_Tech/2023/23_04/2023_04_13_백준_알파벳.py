# https://www.acmicpc.net/problem/1987

if __name__ == "__main__":
    import sys
    
    row, col = map(int, sys.stdin.readline().split())
    graph = []

    for _ in range(row):
        graph.append(list(sys.stdin.readline().strip()))
    
    dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]

    queue = set()
    queue.add((0, 0, graph[0][0]))
    
    max_val = 1

    while queue:
        cur_row, cur_col, total = queue.pop()

        for i in range(4):
            n_row, n_col = cur_row+dx[i], cur_col+dy[i]
            if n_row < 0 or n_row >= row or n_col < 0 or n_col >= col or graph[n_row][n_col] in total:
                continue
            max_val = max(max_val, len(total) + 1)
            queue.add((n_row, n_col, graph[n_row][n_col]+total))
    
    print(max_val)