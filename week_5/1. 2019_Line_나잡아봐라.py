# https://www.notion.so/5-f51f57c84aef4626b580a5937adabca9#b9d162f860734c48aad924aed7ec71fb

from collections import deque

c = 11
b = 2


def catch_me(cony, brown):
    MAX = 200000
    time = 0
    queue = deque()
    queue.append((brown, 0))
    visited = [{} for _ in range(MAX + 1)]
    
    while cony <= MAX:
        cony += time
        if time in visited[cony]:
            return time
        for i in range(0, len(queue)):
            current_position, current_time = queue.popleft()

            new_position = current_position - 1
            new_time = current_time + 1
            if new_position >= 0 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position + 1
            if new_position < 200001 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position * 2
            if new_position < 200001 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

        time += 1

    return -1


print(catch_me(c, b))  # 5가 나와야 합니다!
print("정답 = 3 / 현재 풀이 값 = ", catch_me(10,3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51,50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550,500))