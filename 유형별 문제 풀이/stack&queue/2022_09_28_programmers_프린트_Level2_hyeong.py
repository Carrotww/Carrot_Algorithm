# 내 최신 풀이
def solution(priorities, location):
    from collections import deque
    temp = [(num, pr) for num, pr in enumerate(priorities)]
    temp = deque(temp)

    cnt = 0
    while temp:
        pr_job = temp.popleft()
        if temp and int(pr_job[1]) < max(temp, key=lambda x:x[1])[1]:
            temp.append(pr_job)
        else:
            cnt += 1
            if pr_job[0] == location:
                return cnt


"""
from collections import deque

def solution(priorities, location):
    stack = []
    queue = deque([(x, y) for x, y in enumerate(priorities)])
    cnt = 0

    while 1:
        temp_num, temp_pr = queue.popleft()
        if any(temp_pr < x[1] for x in queue):
            queue.append((temp_num, temp_pr))
        else:
            cnt += 1
            if temp_num == location:
                return cnt
"""


""" # 내 풀이
from collections import deque

def solution(priorities, location):
    stack = [[-1, -1]]
    temp = zip(priorities, range(len(priorities)))
    queue = deque(temp)
    while stack[-1][1] != location:
        value = queue.popleft()
        for pr, num in queue:
            if value[0] < pr:
                queue.append(value)
                break
        else:
            stack.append(value)
    
    return len(stack) - 1
"""

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))