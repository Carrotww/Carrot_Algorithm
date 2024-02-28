# https://www.acmicpc.net/problem/2580

def is_empty():
    for i in range(9):
        for j in range(9):
            if graph[i][j] == 0:
                return (i, j)
    return None

def is_valid(cur_r, cur_c, num):
    if num in graph[cur_r]:
        return False

    if num in [graph[x][cur_c] for x in range(9)]:
        return False

    start_r = cur_r - cur_r % 3
    start_c = cur_c - cur_c % 3
    for i in range(3):
        for j in range(3):
            if graph[i+start_r][j+start_c] == num:
                return False
    return True

def dfs():
    rc = is_empty()
    if not rc:
        return True
    cur_r, cur_c = rc

    for n in range(1, 10):
        if is_valid(cur_r, cur_c, n):
            graph[cur_r][cur_c] = n

            if dfs():
                return True
            graph[cur_r][cur_c] = 0

    return False

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    graph = [list(map(int, input().split())) for _ in range(9)]

    dfs()
    for i in range(9):
        print(' '.join(map(str, graph[i])))









