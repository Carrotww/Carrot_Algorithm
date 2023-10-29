# https://school.programmers.co.kr/learn/courses/30/lessons/169199

def solution(board):
    from collections import deque
    for i in range(board[0]):
        for j in range(board):
            if board[j][i] == 'R':
                start_x, start_y = i, j
                continue
    
    for i in range(board[0]):
        for j in range(board):
            if board[j][i] == 'G':
                end_x, end_y = i, j
                continue
    
    queue = deque()
    queue.append([start_x, start_y])
    
    def bfs(x, y, cnt):
        cur_x, cur_y = queue.popleft()
        if cur_x == end_x and cur_y == end_y:
            return cnt
    
    cnt = bfs(start_x, start_y, 0)