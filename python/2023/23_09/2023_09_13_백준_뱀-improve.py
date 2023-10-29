# https://www.acmicpc.net/problem/3190

if __name__ == "__main__":
    import sys
    from collections import deque
    
    input = sys.stdin.readline
    
    N = int(input())
    apple_cnt = int(input())

    graph = [[0] * N for _ in range(N)]

    for _ in range(apple_cnt):
        temp = list(map(lambda x: int(x)-1, input().split()))
        graph[temp[0]][temp[1]] = 1
    
    turn_cnt = int(input())
    turn_queue = deque()
    for _ in range(turn_cnt):
        temp = input().split()
        time = int(temp[0])
        direct = temp[1]
        if direct == 'D':
            turn_queue.append((time+1, 1))
        else:
            turn_queue.append((time+1, -1))
    
    dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
    snake = deque([(0, 0)])
    time = 1
    direct = 0
    while 1:
        cur_r, cur_c = snake[0]

        if turn_queue and turn_queue[0][0] == time:
            direct = (direct + turn_queue[0][1]) % 4
            turn_queue.popleft()
        
        n_r, n_c = cur_r + dr[direct], cur_c + dc[direct]
        if (n_r < 0 or n_r >= N) or (n_c < 0 or n_c >= N) or (n_r, n_c) in snake:
            break
        
        if graph[n_r][n_c] == 1:
            graph[n_r][n_c] = 0
        else:
            snake.pop()
        snake.appendleft((n_r, n_c))
        time += 1
    print(time)