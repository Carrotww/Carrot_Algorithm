from collections import deque

def solution(bridge_length, weight, truck_weights):
    total_length = deque([0] * bridge_length)
    queue = deque(truck_weights)
    time = 0
    while queue:
        if sum(total_length) + queue[0] <= weight:
            total_length.popleft()
            total_length.append(queue.popleft())
            time += 1
        else:
            total_length.popleft()
            if sum(total_length) + queue[0] < weight:
                total_length.append(queue.popleft())
            else:
                total_length.append(0)
            time += 1

    return time + len(total_length)

print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))