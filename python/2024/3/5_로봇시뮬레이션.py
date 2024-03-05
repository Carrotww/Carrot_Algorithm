# https://www.acmicpc.net/problem/2174

def error1(x):
    return f"Robot {x} crashes into the wall"

def error2(x, y):
    return f"Robot {x} crashes into robot {y}"

def move(robot_num, direct, repeat):
    cur_r, cur_c, cur_direct = robot_position[robot_num]
    if direct != 0:
        # cur_direct = (cur_direct + repeat * direct) % 4
        rotation = repeat * direct + cur_direct
        if rotation < 0:
            rotation += (abs(rotation) // 4 + 1) * 4
        cur_direct = rotation % 4

        robot_position[robot_num] = [cur_r, cur_c, cur_direct]
    else:
        for i in range(1, repeat+1):
            n_r, n_c = cur_r + dr[cur_direct] * i, cur_c + dc[cur_direct] * i
            if (n_r < 0 or n_r >= r) or (n_c < 0 or n_c >= c):
                result.append(error1(robot_num))
                return
            if graph[n_r][n_c] != 0:
                result.append(error2(robot_num, graph[n_r][n_c]))
                return
        robot_position[robot_num] = [n_r, n_c, cur_direct]
        graph[cur_r][cur_c] = 0
        graph[n_r][n_c] = robot_num

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    c, r = map(int, input().split())
    n, m = map(int, input().split())

    graph = [[0] * c for _ in range(r)]
    robot_position = {}
    robot_num = 1
    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
    check_direct = {'N':0,'E':1,'S':2,'W':3}
    change_direct = {'F':0,'R':1,'L':-1}
    result = []
    for _ in range(n):
        x, y, direct_alpa = input().split()
        r_r, r_c = r-int(y), int(x)-1
        direct = check_direct[direct_alpa]
        robot_position[robot_num] = [r_r, r_c, direct]
        graph[r_r][r_c] = robot_num
        robot_num += 1
    for i in range(m):
        robot_num, direct_alpa, repeat = input().split()
        if not result:
            move(int(robot_num), change_direct[direct_alpa], int(repeat))
        else:
            break

    if not result:
        print('OK')
    else:
        for r in result:
            print(r)

