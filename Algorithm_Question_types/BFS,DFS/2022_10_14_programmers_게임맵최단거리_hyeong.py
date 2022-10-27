# https://school.programmers.co.kr/learn/courses/30/lessons/1844
# 푸는 중

def solution(maps):
    from collections import deque
    total_row, total_col = len(maps) - 1, len(maps[0]) - 1
    cnt = 0
    queue = deque()
    queue.append([0, 0])
    visited = [[0]*(total_col + 1) for _ in range(total_row + 1)]
    visited[0][0] = 1
    # 동서남북
    dr, dc = [1, -1, 0, 0], [0, 0, -1, 1]

    while queue:
        current_r, current_c = queue.popleft()
        if current_r == total_row and current_c == total_col:
            return visited[current_r][current_c]

        for i in range(4):
            next_r, next_c = dr[i] + current_r, dc[i] + current_c
            if 0 <= next_r <= total_row and 0 <= next_c <= total_col:
                if maps[next_r][next_c] == 1 and not visited[next_r][next_c]:
                    visited[next_r][next_c] = visited[current_r][current_c] + 1
                    queue.append((next_r, next_c))
    return -1

"""
# 기존 DFS 풀이 근데 이제 DP를 곁들인.
from collections import deque

def solution(maps):
    result = 0
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    q = deque([0, 0])

    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    visited[0][0] = 1
    maps[0][0] = 0
    
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx <= len(maps) and 0 <= ny < len(maps[0]):
                if maps[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
    
    result = -1
    if visited:
        return visited
    return result
"""

print(solution([[1,0], [1,0], [1,0], [1,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))