from collections import deque

c = 11
b = 2

def catch_me(cony, brown):
    time = 0
    MAX = 200000
    visited = [{} for _ in range(MAX + 1)] # [위치[시간]]
    queue = deque()
    queue.append((time, brown))
    
    while cony <= MAX:
        cony += time
        if time in visited[cony]:
            return time
        
        for _ in range(len(queue)):
            brown_time, brown_lo = queue.popleft()
            
            new_time = brown_time + 1
            new_brown_lo = brown_lo + 1
            if 0 <= new_brown_lo <= MAX and new_time not in visited[new_brown_lo]:
                visited[new_brown_lo][new_time] = True
                queue.append((new_time, new_brown_lo))

            new_brown_lo = brown_lo - 1
            if 0 <= new_brown_lo <= MAX and new_time not in visited[new_brown_lo]:
                queue.append((new_time, new_brown_lo))
                visited[new_brown_lo][new_time] = True

            new_brown_lo = brown_lo * 2
            if 0 <= new_brown_lo <= MAX and new_time not in visited[new_brown_lo]:
                queue.append((new_time, new_brown_lo))
                visited[new_brown_lo][new_time] = True
        
        time += 1
    
    return -1

print(catch_me(c, b)) # 5

print("정답 = 3 / 현재 풀이 값 = ", catch_me(10,3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51,50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550,500))