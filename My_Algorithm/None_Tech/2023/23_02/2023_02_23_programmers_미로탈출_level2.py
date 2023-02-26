# https://school.programmers.co.kr/learn/courses/30/lessons/159993

def solution(maps):
    from collections import deque
    dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
    
    queue1 = deque()
    queue2 = deque()
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                start_node = (i, j, 0)
            elif maps[i][j] == 'L':
                lever_node = (i, j, 0)
    
    def bfs(path, end_node):
        cnt = 0
        visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
        visited[path[0][0]][path[0][1]] = 1
        
        while path:
            x, y, cnt = path.popleft()
            for i in range(4):
                n_x, n_y = dx[i] + x, dy[i] + y
                if (n_x >= 0 and n_x < len(maps)) and (n_y >= 0 and n_y < len(maps[0])):
                    if maps[n_x][n_y] == end_node:
                        return cnt + 1
                    elif not maps[n_x][n_y] == 'X' and visited[n_x][n_y] == 0:
                        path.append((n_x, n_y, cnt + 1))
                        visited[n_x][n_y] = 1
        return -1
    
    queue1.append(start_node)
    queue2.append(lever_node)
    to_L = bfs(queue1, 'L')
    to_E = bfs(queue2, 'E')
    
    if to_L == -1 or to_E == -1:
        return -1
    return to_L + to_E