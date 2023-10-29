# https://www.acmicpc.net/problem/13460

def can_move_red(r, c, d):
    n_r, n_c = r+dr[d], c+dc[d]
    if (n_r, n_c) == (n_blue_r, n_blue_c):
        return False
    if graph[n_r][n_c] == '.' or graph[n_r][n_c] == 'O':
        return True
    return False

def can_move_blue(r, c, d):
    n_r, n_c = r+dr[d], c+dc[d]
    if (n_r, n_c) == (n_red_r, n_red_c):
        return False
    if graph[n_r][n_c] == '.' or graph[n_r][n_c] == 'O':
        return True
    return False

def move_red(r, c, d):
    if (r, c) == goal:
        return (r, c)
    n_r, n_c = r+dr[d], c+dc[d]
    if graph[n_r][n_c] == 'O' or graph[n_r][n_c] == '.':
        return (n_r, n_c)
    return (r, c)

def move_blue(r, c, d):
    if (r, c) == goal:
        return (r, c)
    n_r, n_c = r+dr[d], c+dc[d]
    if graph[n_r][n_c] == 'O' or graph[n_r][n_c] == '.':
        return (n_r, n_c)
    return (r, c)

if __name__ == "__main__":
    import sys
    from collections import deque

    input = sys.stdin.readline

    row, col = map(int, input().split())
    graph = []
    red, blue, goal = (), (), ()

    for r in range(row):
        temp = list(input().rstrip())
        for c in range(col):
            if temp[c] == 'R':
                red = (r, c)
            elif temp[c] == 'B':
                blue = (r, c)
            elif temp[c] == 'O':
                goal = (r, c)
        graph.append(temp)
    
    dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
    result = -1

    queue = deque([(red[0], red[1], blue[0], blue[1], 0)])

    while queue:
        red_r, red_c, blue_r, blue_c, cnt = queue.popleft()
        if cnt > 10 or (blue_r, blue_c) == goal:
            continue
        if (red_r, red_c) == goal:
            result = cnt
        
        n_red_r, n_red_c, n_blue_r, n_blue_c = red_r, red_c, blue_r, blue_c
            
        for d in range(4):
            if d == 0:
                # down
                if n_red_r < n_blue_r:
                    while can_move_red(n_red_r, n_red_c, d) or can_move_blue(n_blue_r, n_blue_c, d):
                        n_blue_r, n_blue_c = move_blue(n_blue_r, n_blue_c, d)
                        n_red_r, n_red_c = move_red(n_red_r, n_red_c, d)
                else:
                    while can_move_red(n_red_r, n_red_c, d) or can_move_blue(n_blue_r, n_blue_c, d):
                        n_red_r, n_red_c = move_red(n_red_r, n_red_c, d)
                        n_blue_r, n_blue_c = move_blue(n_blue_r, n_blue_c, d)
            elif d == 1:
                # up
                if n_red_r < n_blue_r:
                    while can_move_red(n_red_r, n_red_c, d) or can_move_blue(n_blue_r, n_blue_c, d):
                        n_red_r, n_red_c = move_red(n_red_r, n_red_c, d)
                        n_blue_r, n_blue_c = move_blue(n_blue_r, n_blue_c, d)
                else:
                    while can_move_red(n_red_r, n_red_c, d) or can_move_blue(n_blue_r, n_blue_c, d):
                        n_blue_r, n_blue_c = move_blue(n_blue_r, n_blue_c, d)
                        n_red_r, n_red_c = move_red(n_red_r, n_red_c, d)
            elif d == 2:
                # right
                if n_red_c < n_blue_c:
                    while can_move_red(n_red_r, n_red_c, d) or can_move_blue(n_blue_r, n_blue_c, d):
                        n_blue_r, n_blue_c = move_blue(n_blue_r, n_blue_c, d)
                        n_red_r, n_red_c = move_red(n_red_r, n_red_c, d)
                else:
                    while can_move_red(n_red_r, n_red_c, d) or can_move_blue(n_blue_r, n_blue_c, d):
                        n_red_r, n_red_c = move_red(n_red_r, n_red_c, d)
                        n_blue_r, n_blue_c = move_blue(n_blue_r, n_blue_c, d)
            elif d == 3:
                # left
                if n_red_c < n_blue_c:
                    while can_move_red(n_red_r, n_red_c, d) or can_move_blue(n_blue_r, n_blue_c, d):
                        n_red_r, n_red_c = move_red(n_red_r, n_red_c, d)
                        n_blue_r, n_blue_c = move_blue(n_blue_r, n_blue_c, d)
                else:
                    while can_move_red(n_red_r, n_red_c, d) or can_move_blue(n_blue_r, n_blue_c, d):
                        n_blue_r, n_blue_c = move_blue(n_blue_r, n_blue_c, d)
                        n_red_r, n_red_c = move_red(n_red_r, n_red_c, d)
            if (red_r, red_c) == (n_red_r, n_red_c) and (blue_r, blue_c) == (n_blue_r, n_blue_c):
                continue
            queue.append((n_red_r, n_red_c, n_blue_r, n_blue_c, cnt + 1))
    print(result)