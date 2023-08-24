# https://www.acmicpc.net/problem/4179

def bfs():
    from collections import deque
    queue = deque(fire_start + j_start)
    dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]

    while queue:
        cur_r, cur_c, time, is_fire = queue.popleft()
        if not is_fire and (cur_r == 0 or cur_r == R - 1 or cur_c == 0 or cur_c == C-1):
            return time + 1
        for direct in range(4):
            n_r, n_c = cur_r+dr[direct], cur_c+dc[direct]
            if (n_r < 0 or n_r >= R or n_c < 0 or n_c >= C) or graph[n_r][n_c][0] == '#':
                continue

            # 불일때
            if is_fire and graph[n_r][n_c][1] == 0:
                queue.append([n_r, n_c, time+1, is_fire])
                graph[n_r][n_c][1] = 1
            if not is_fire and graph[n_r][n_c][1] == 0 and graph[n_r][n_c][0] == '.':
                queue.append([n_r, n_c, time+1, is_fire])
                graph[n_r][n_c][1] = 1

    return -1


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    R, C = map(int, input().split())

    graph = []
    j_start = []
    fire_start = []
    for r in range(R):
        row = list(input().rstrip())
        for c in range(C):
            if row[c] == "J":
                j_start.append([r, c, 0, False])
            elif row[c] == "F":
                fire_start.append([r, c, 0, True])
        row = [[val, 0] for val in row]
        graph.append(row)

    result = bfs()

    if result == -1:
        print("IMPOSSIBLE")
    else:
        print(result)
