# https://school.programmers.co.kr/learn/courses/30/lessons/172928?language=python3

def solution(park, routes):
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                cur_x, cur_y = j, i
                continue
    
    def check(x, y):
        if (0 > x or x >= len(park[0])) or (0 > y or y >= len(park)) or park[y][x] == 'X':
            return False
        return True
    
    for route in routes:
        direct, move = route.split(' ')
        move = int(move)
        if direct == 'E':
            n_x = cur_x + move
            for t_x in range(cur_x, n_x + 1):
                if check(t_x, cur_y) == False:
                    break
            else:
                cur_x = n_x
        elif direct == 'W':
            n_x = cur_x - move
            for t_x in range(n_x, cur_x + 1):
                if check(t_x, cur_y) == False:
                    break
            else:
                cur_x = n_x
        elif direct == 'N':
            n_y = cur_y - move
            for t_y in range(n_y, cur_y + 1):
                if check(cur_x, t_y) == False:
                    break
            else:
                cur_y = n_y
        elif direct == 'S':
            n_y = cur_y + move
            for t_y in range(cur_y, n_y + 1):
                if check(cur_x, t_y) == False:
                    break
            else:
                cur_y = n_y
        
    return [cur_y, cur_x]