# https://school.programmers.co.kr/learn/courses/30/lessons/42898

# 첫 번째 풀이 - 시간 초과
def solution(m, n, puddles):
    from collections import deque
    dp = [[10001 for _ in range(n)] for _ in range(m)]
    path = dp[:]
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    for pu in puddles:
        x, y = pu
        path[x-1][y-1] = -1
    
    fast_cnt = 10001
    result = 0
    queue = deque()
    queue.append([0, 0, 0])
    while queue:
        cur_x, cur_y, cnt = queue.popleft()
        for i in range(4):
            n_x, n_y = cur_x + dx[i], cur_y + dy[i]
            if (n_x >= 0 and n_x < m) and (n_y >= 0 and n_y < n) and path[n_x][n_y] != -1:
                if n_x == m - 1 and n_y == n - 1 and (cnt + 1 <= fast_cnt):
                    fast_cnt = cnt + 1
                    result += 1
                    break
                if cnt + 1 <= dp[n_x][n_y]:
                    dp[n_x][n_y] = cnt + 1
                    queue.append([n_x, n_y, cnt + 1])
    
    return result % 1000000007