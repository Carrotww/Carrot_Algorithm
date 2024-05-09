# https://www.acmicpc.net/problem/7682

def checkbingo(player, graph):
    # 가로 체크
    for i in range(3):
        cnt = 0
        for j in range(3):
            if graph[i][j] == player:
                cnt += 1
        if cnt == 3:
            return True

    # 세로 체크
    for i in range(3):
        cnt = 0
        for j in range(3):
            if graph[j][i] == player:
                cnt += 1
        if cnt == 3:
            return True

    # 대각선 체크
    start_r, start_c = 0, 0
    cnt = 0
    for i in range(3):
        if graph[start_r + i][start_c + i] == player:
            cnt += 1
    if cnt == 3:
        return True

    start_r, start_c = 0, 2
    cnt = 0
    for i in range(3):
        if graph[start_r + i][start_c - i] == player:
            cnt += 1
    if cnt == 3:
        return True

    return False


def solve(t):
    graph = []
    start = 0
    for _ in range(3):
        graph.append(t[start:start + 3])
        start += 3

    cur_o, cur_x, cur_b = 0, 0, 0
    for i in range(3):
        for j in range(3):
            if graph[i][j] == 'O':
                cur_o += 1
            elif graph[i][j] == 'X':
                cur_x += 1
            else:
                cur_b += 1

    is_x_win = checkbingo('X', graph)
    is_o_win = checkbingo('O', graph)

    if is_x_win and not is_o_win:
        if cur_x == cur_o + 1:
            return True

    if is_o_win and not is_x_win:
        if cur_x == cur_o:
            return True

    if not is_x_win and not is_o_win and cur_x == 5 and cur_o == 4:
        return True

    return False


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    graph = []
    result = []

    while True:
        t = list(input().strip())
        if t[0] == 'e':
            break
        if solve(t):
            result.append('valid')
        else:
            result.append('invalid')

    for r in result:
        print(r)

