# https://www.acmicpc.net/problem/3190

def turn(cur_direct, turn_direct):
    return (cur_direct + turn_direct) % 4

if __name__ == "__main__":
    import sys
    from collections import deque

    input = sys.stdin.readline

    N = int(input())
    graph = [[0] * N for _ in range(N)]

    # apple cnt
    apple_cnt = int(input())
    apple_list = []
    for _ in range(apple_cnt):
        apple_r, apple_c = list(map(lambda x: int(x)-1, input().split()))
        apple_list.append([apple_r, apple_c])
        graph[apple_r][apple_c] = 1

    turn_cnt = int(input())
    turn_dict = dict()
    for _ in range(turn_cnt):
        temp = list(input().split())
        time = int(temp[0])
        direct = temp[1]
        if direct == 'L':
            turn_dict[time+1] = -1
        else:
            turn_dict[time+1] = 1

    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]

    # 0 -> up 1 -> right 2 -> down 3 -> left
    # r, c, direct
    snake = [0, 0, 1, 1]
    snake_body = deque([(0, 0)])
    snake_body_check = {(0, 0)}
    snake_tail = (0, 0)

    while 1:
        s_r, s_c, s_d, time = snake
        # if cur_time is need to turn -> change direct
        if time in turn_dict:
            s_d = turn(s_d, turn_dict[time])

        n_s_r, n_s_c = dr[s_d]+s_r, dc[s_d]+s_c
        if (n_s_r < 0 or n_s_r >= N) or (n_s_c < 0 or n_s_c >= N) or (n_s_r, n_s_c) in snake_body_check:
            break
        if graph[n_s_r][n_s_c] == 1:
            graph[n_s_r][n_s_c] = 0
        else:
            tail = snake_body.pop()
            snake_body_check.remove(tail)

        snake_body.appendleft((n_s_r, n_s_c))
        snake_body_check.add((n_s_r, n_s_c))

        snake = [n_s_r, n_s_c, s_d, time+1]

    print(time)
