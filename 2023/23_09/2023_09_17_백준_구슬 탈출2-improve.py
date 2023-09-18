def move(r, c, d):
    while True:
        n_r, n_c = r + dr[d], c + dc[d]
        if graph[n_r][n_c] == '#':
            return r, c
        if (n_r, n_c) == goal:
            return n_r, n_c
        r, c = n_r, n_c


if __name__ == "__main__":
    from collections import deque

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

        if cnt > 10:
            break

        if (blue_r, blue_c) == goal:
            continue

        if (red_r, red_c) == goal:
            result = cnt
            break

        for d in range(4):
            if (d == 0 and red_r > blue_r) or (d == 1 and red_r < blue_r) or (d == 2 and red_c > blue_c) or (d == 3 and red_c < blue_c):
                new_red_r, new_red_c = move(red_r, red_c, d)
                new_blue_r, new_blue_c = move(blue_r, blue_c, d)
            else:
                new_blue_r, new_blue_c = move(blue_r, blue_c, d)
                new_red_r, new_red_c = move(red_r, red_c, d)

            if (red_r, red_c, blue_r, blue_c) != (new_red_r, new_red_c, new_blue_r, new_blue_c):
                queue.append(
                    (new_red_r, new_red_c, new_blue_r, new_blue_c, cnt + 1))

    print(result)
