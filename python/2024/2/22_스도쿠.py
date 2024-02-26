# https://www.acmicpc.net/problem/2580
# 빈곳이 담긴 리스트를 돌면서 조건에 맞는 부분들을 넣어준다.
# 가로 세로로 채울수 없다면( 나 빼고 빈곳이 있다면 가로 세로에)
# 내가 속한 사각형에 나만 빈칸이라면 ( 채운다 ) 
# 가로 세로 줄을 보면서 채울 수 없다면 다음걸로 넘어간다 queue에 넣어주고

def square(cur_r, cur_c):
    cnt = 0
    start_r, start_c = 0, 0
    if cur_r < 3:
        start_r = 0
    elif 3 <= cur_r < 6:
        start_r = 3
    else:
        start_r = 6

    if cur_c < 3:
        start_c = 0
    elif 3 <= cur_c < 6:
        start_c = 3
    else:
        start_c = 6
    total = []

    for i in range(start_r, start_r+3):
        for j in range(start_c, start_c+3):
            if graph[i][j] != 0:
                total.append(graph[i][j])
    if len(total) >= 8:
        graph[cur_r][cur_c] = 45 - sum(total)
        return True
    return False

def width(cur_r, cur_c):
    r_total = []
    for i in graph[cur_r]:
        if i != 0:
            r_total.append(i)
    if len(r_total) >= 8:
        graph[cur_r][cur_c] = 45 - sum(r_total)
        return True
    else:
        return False

def length(cur_r, cur_c):
    c_total = []
    for i in [graph[x][cur_c] for x in range(9)]:
        if i != 0:
            c_total.append(i)
    if len(c_total) >= 8:
        graph[cur_r][cur_c] = 45 - sum(c_total)
        return True
    else:
        return False

if __name__ == "__main__":
    import sys
    from collections import deque
    input = sys.stdin.readline

    r, c = 9, 9
    graph = [list(map(int, input().split())) for _ in range(r)]

    empty = deque()
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 0:
                empty.append((i, j))

    while empty:
        cur_r, cur_c = empty.popleft()
        if width(cur_r, cur_c) or length(cur_r, cur_c) or square(cur_r, cur_c):
            continue
        else:
            empty.append((cur_r, cur_c))

    for i in range(r):
        print(' '.join(map(str, graph[i])))






