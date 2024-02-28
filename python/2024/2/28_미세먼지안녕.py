# https://www.acmicpc.net/problem/17144

def move(cur_r, cur_c):
    cnt = 0
    for d in range(4):
        n_r, n_c = cur_r+dr[d], cur_c+dc[d]
        if (n_r < 0 or n_r >= r) or (n_c < 0 or n_c >= c):
            continue
        if graph[n_r][n_c] == -1:
            continue
        new_graph[n_r][n_c] += graph[cur_r][cur_c] // 5
        cnt += 1
    return cnt


def dust():
    global new_graph
    new_graph = [[0] * c for _ in range(r)]
    new_graph[ac_up[0]][ac_up[1]] = -1
    new_graph[ac_down[0]][ac_down[1]] = -1
    for i in range(r):
        for j in range(c):
            if graph[i][j] > 4:
                cnt = move(i, j)
                graph[i][j] -= (cnt * (graph[i][j] // 5))
                new_graph[i][j] += graph[i][j]
            elif graph[i][j] != -1 and graph[i][j] <= 4:
                new_graph[i][j] += graph[i][j]

    return new_graph

def start_aircleaner(init_r, init_c, direct, curve):
    cur_r, cur_c = init_r + dr[direct], init_c + dc[direct]
    check_r = init_r + dr[(direct + 2) % 4]
    graph[cur_r][cur_c] = 0
    stack = [(cur_r, cur_c)]
    while stack:
        cur_r, cur_c = stack.pop()
        n_r, n_c = cur_r + dr[direct], cur_c + dc[direct]
        if cur_r == init_r and cur_c == init_c:
            graph[cur_r][cur_c + 1] = 0
            return
        if (n_r < 0 or n_r >= r) or (n_c < 0 or n_c >= c) or (n_r == check_r and n_c == c - 1):
            direct = (direct + curve) % 4
            n_r, n_c = cur_r + dr[direct], cur_c + dc[direct]
        graph[cur_r][cur_c] = graph[n_r][n_c]
        stack.append((n_r, n_c))

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    r, c, t = map(int, input().split())
    graph = []
    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
    for _ in range(r):
        graph.append(list(map(int, input().split())))

    # aircleanrer
    ac_up = [0, 0, 0, 1]
    ac_down = [0, 0, 2, -1]
    
    for i in range(r):
        if graph[i][0] == -1:
            ac_up[0], ac_up[1] = i, 0
            ac_down[0], ac_down[1] = i+1, 0
            break

    for _ in range(t):
        graph = dust()
        start_aircleaner(ac_up[0], ac_up[1], ac_up[2], ac_up[3])
        start_aircleaner(ac_down[0], ac_down[1], ac_down[2], ac_down[3])

    result = 0
    for i in range(r):
        result += sum(graph[i])

    print(result + 2)


