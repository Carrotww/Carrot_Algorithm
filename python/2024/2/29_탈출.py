# https://www.acmicpc.net/problem/3055

def escape():
    queue = deque(start)
    visited = [[float("inf")] * c for _ in range(r)]
    visited[queue[0][0]][queue[0][1]] = 0
    while queue:
        cur_r, cur_c = queue.popleft()
        for d in range(4):
            n_r, n_c = cur_r+dr[d], cur_c+dc[d]
            if (n_r < 0 or n_r >= r) or (n_c < 0 or n_c >= c):
                continue
            if graph[n_r][n_c] == "D":
                return visited[cur_r][cur_c] + 1
            cur_cnt = visited[cur_r][cur_c]
            if graph[n_r][n_c] != "X" and cur_cnt + 1 < water_visited[n_r][n_c] and cur_cnt + 1 < visited[n_r][n_c]:
                visited[n_r][n_c] = visited[cur_r][cur_c] + 1
                queue.append((n_r, n_c))
    return 0

def over_water():
    queue = deque(water)
    visited = [[float("inf")] * c for _ in range(r)]
    for i, j in water:
        visited[i][j] = 0
    while queue:
        cur_r, cur_c = queue.popleft()
        for d in range(4):
            n_r, n_c = cur_r + dr[d], cur_c + dc[d]
            if (n_r < 0 or n_r >= r) or (n_c < 0 or n_c >= c):
                continue
            if visited[n_r][n_c] > visited[cur_r][cur_c] + 1 and (graph[n_r][n_c] == "." or graph[n_r][n_c] == "S"):
                visited[n_r][n_c] = visited[cur_r][cur_c] + 1
                queue.append((n_r, n_c))
    return visited

if __name__ == "__main__":
    import sys
    from collections import deque
    input = sys.stdin.readline

    r, c = map(int, input().split())
    graph = []
    for _ in range(r):
        graph.append(list(input().rstrip()))

    dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
    start = []
    water = []
    for i in range(r):
        for j in range(c):
            if graph[i][j] == "S":
                start.append((i, j))
            elif graph[i][j] == "*":
                water.append((i, j))
    water_visited = over_water()
    result = escape()
    if result == 0:
        print("KAKTUS")
    else:
        print(result)



