# https://school.programmers.co.kr/learn/courses/30/lessons/133500
# 2 번째 풀이
from collections import defaultdict, deque

def solution(n, lighthouse):
    # start point를 잡는다 - 맨 끝에 있는 노드
    path = defaultdict(list)
    for a, b in lighthouse:
        path[a].append(b)
        path[b].append(a)

    light_list, visited = set(), set()
    
    start = -1
    for key, val in path.items():
        if len(val) == 1:
            start = key
            light_list.add(val[0])
            break
    
    queue = deque([start])

    while queue:
        temp = queue.popleft()
        visited.add(temp)
        state = True
        for i in path[temp]:
            if i in light_list:
                state = False
        for i in path[temp]:
            if i in visited:
                continue
            queue.append(i)
        if state and temp not in light_list:
            light_list.add(temp)
    
    return light_list

print(solution(8, [[1, 2], [1, 3], [1, 4], [1, 5], [5, 6], [5, 7], [5, 8]]))
print(solution(10, [[4, 1], [5, 1], [5, 6], [7, 6], [1, 2], [1, 3], [6, 8], [2, 9], [9, 10]]))