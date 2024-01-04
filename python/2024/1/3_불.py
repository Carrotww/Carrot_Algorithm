# https://www.acmicpc.net/problem/5427

def escape():
    escape_visited = [[True] * c for _ in range(r)]
    escape_visited[queue[0][0]][queue[0][1]] = 0

    while queue:
        cur_r, cur_c, cnt = queue.popleft()
        for d in range(4):
            n_r, n_c = cur_r+dr[d], cur_c+dc[d]
            if (n_r < 0 or n_r >= r) or (n_c < 0 or n_c >= c):
                return cnt + 1
            if graph[n_r][n_c] == "." and escape_visited[n_r][n_c] and (visited[n_r][n_c] == 0 or cnt + 1 < visited[n_r][n_c]):
                escape_visited[n_r][n_c] = False
                queue.append([n_r, n_c, cnt+1])
   
    return -1

def gofire():
    while fire_queue:
        cur_r, cur_c = fire_queue.popleft()
        for d in range(4):
            n_r, n_c = cur_r+dr[d], cur_c+dc[d]
            if (n_r < 0 or n_r >= r) or (n_c < 0 or n_c >= c):
                continue
            if (graph[n_r][n_c] == "." or graph[n_r][n_c] == "@") and visited[n_r][n_c] == 0:
                visited[n_r][n_c] = visited[cur_r][cur_c] + 1
                fire_queue.append([n_r, n_c])

if __name__ == "__main__":
    import sys
    from collections import deque
    input = sys.stdin.readline

    # 불이 옮겨오는 동시에 움직일 수 있음
    # 불이 옮겨오는 곳으로 움직일 수 없음

    t = int(input())
    for _ in range(t):
        c, r = map(int, input().split())
        graph = []
        visited = [[0] * c for _ in range(r)]
        for _ in range(r):
            graph.append(list(input().rstrip()))
        queue = deque()
        fire_queue = deque()

        for i in range(r):
            for j in range(c):
                if graph[i][j] == "@":
                    queue.append([i, j, 0])
                elif graph[i][j] == "*":
                    fire_queue.append([i, j])

        dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]

        gofire()
        result = -1
        if queue:
            result = escape()
        if result == -1:
            print("IMPOSSIBLE")
        else:
            print(result)

